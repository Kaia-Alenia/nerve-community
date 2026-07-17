import discord
from discord.ext import commands
from discord import app_commands
import os
from dotenv import load_dotenv
from google import genai
from groq import Groq
from github import Github
from github import Auth
from collections import defaultdict, deque
import time
import datetime
import aiosqlite
import csv
import io
import re

# Cargar variables de entorno
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')
GROQ_API_KEY = os.getenv('GROQ_API_KEY')
GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')

# Configurar APIs
try:
    gemini_client = genai.Client(api_key=GEMINI_API_KEY)
except Exception as e:
    print(f"Error inicializando Gemini: {e}")
    gemini_client = None

groq_client = Groq(api_key=GROQ_API_KEY) if GROQ_API_KEY else None
gh = Github(auth=Auth.Token(GITHUB_TOKEN)) if GITHUB_TOKEN else Github()
repo_name = "Kaia-Alenia/nerve-community"

# Configurar Intents
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix=commands.when_mentioned_or('!'), intents=intents)

# Memoria conversacional por usuario (hasta 10 turnos por usuario)
MAX_HISTORY = 10
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "data", "kaia.db")

# Configuración de Moderación
BAD_WORDS = {'spamword', 'badword', 'insulto', 'groseria'}
SPAM_THRESHOLD_MSGS = 5
SPAM_THRESHOLD_SECONDS = 5
WARN_TIMEOUT_LIMIT = 3
TIMEOUT_DURATION = datetime.timedelta(minutes=5)

user_warns: dict[int, list[dict]] = defaultdict(list)
user_message_times: dict[int, deque] = defaultdict(lambda: deque(maxlen=SPAM_THRESHOLD_MSGS))

SYSTEM_PROMPT = (
    "Eres Kaia (Kaia Alenia Intelligent Assistant), la IA del servidor de Discord "
    "de Nerve Community. Tienes personalidad amigable, directa y un poco ingeniosa. "
    "Respondes de forma natural como en un chat, nunca robótica. "
    "Si te preguntan algo técnico (Python, Ren'Py, bases de datos, ecosistema Nerve), "
    "das ejemplos de código cuando ayuda. Nunca revelas que eres una IA de Google o que "
    "usas Gemini; si te preguntan, dices que eres Kaia, la IA de Alenia Studios."
)

# Cargar documentos del repo para RAG simple
BASE_DIR_REPO = os.path.dirname(BASE_DIR)
RAG_DOCS = {}
for doc_path in ["README.md", "COMO-HACER-TU-PRIMER-PR.md", "docs/ruta-de-aprendizaje.md", "docs/Porque.md"]:
    full_path = os.path.join(BASE_DIR_REPO, doc_path)
    try:
        with open(full_path, "r", encoding="utf-8") as f:
            RAG_DOCS[doc_path] = f.read()
    except Exception as e:
        print(f"No se pudo cargar {doc_path} para RAG: {e}")

RAG_CONTEXT = "\n\n".join([f"--- CONTENIDO DE {name} ---\n{content}" for name, content in RAG_DOCS.items()])
RAG_INSTRUCTION = (
    "Instrucción especial: Si la pregunta es sobre cómo contribuir, "
    "hacer un PR, o sobre el propósito y aprendizaje del proyecto, básate ÚNICAMENTE en la "
    "información de estos documentos. Si la pregunta es de programación general "
    "sin relación con el repo, responde con tu conocimiento normal.\n\n"
    + RAG_CONTEXT
)

# Saludos que activan respuesta sin mención (solo si son ≤2 palabras)
SALUDOS = {'hola', 'hello', 'hey', 'hi', 'buenas', 'buenos', 'ola', 'sup', 'ey'}


async def setup_hook():
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute('''
            CREATE TABLE IF NOT EXISTS participantes_retos (
                user_id INTEGER,
                reto_id TEXT,
                estado TEXT,
                fecha_inicio TEXT,
                fecha_fin TEXT,
                pr_url TEXT,
                metodo_verificacion TEXT DEFAULT 'ninguno',
                PRIMARY KEY (user_id, reto_id)
            )
        ''')
        # Add column to existing databases if missing
        try:
            await db.execute('ALTER TABLE participantes_retos ADD COLUMN metodo_verificacion TEXT DEFAULT "ninguno"')
        except Exception:
            pass
        await db.execute('''
            CREATE TABLE IF NOT EXISTS usuarios_github (
                discord_id INTEGER PRIMARY KEY,
                github_username TEXT
            )
        ''')
        await db.execute('''
            CREATE TABLE IF NOT EXISTS memoria_conversacion (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                role TEXT,
                content TEXT,
                timestamp TEXT
            )
        ''')
        await db.commit()

bot.setup_hook = setup_hook


async def _add_warn(member: discord.Member, reason: str):
    """Añade un warning a un usuario y aplica timeout si supera el límite."""
    warns = user_warns[member.id]
    warns.append({
        "reason": reason,
        "timestamp": datetime.datetime.now(datetime.timezone.utc).isoformat()
    })
    
    if len(warns) >= WARN_TIMEOUT_LIMIT:
        try:
            await member.timeout(TIMEOUT_DURATION, reason="Demasiadas advertencias automáticas.")
            try:
                await member.send(f"Has sido silenciado por {TIMEOUT_DURATION.seconds // 60} minutos debido a múltiples advertencias.")
            except discord.Forbidden:
                pass
            user_warns[member.id].clear()
        except Exception as e:
            print(f"Error al aplicar timeout: {e}")


@bot.event
async def on_ready():
    print("=" * 40)
    print(f'✅ Bot conectado exitosamente como: {bot.user.name}')
    print("=" * 40)
    try:
        synced = await bot.tree.sync()
        print(f"🔄 Sincronizados {len(synced)} comandos de aplicación.")
    except Exception as e:
        print(f"❌ Error al sincronizar comandos: {e}")
    await bot.change_presence(activity=discord.Game(name="Ayudando a la comunidad Nerve"))


@bot.event
async def on_member_join(member):
    """Bienvenida generada con IA al entrar al servidor."""
    channel = discord.utils.find(lambda c: "bienvenida" in c.name.lower(), member.guild.text_channels)
    if not channel:
        channel = member.guild.system_channel
    if not channel and member.guild.text_channels:
        channel = member.guild.text_channels[0]

    if not channel:
        return

    prompt_bienvenida = (
        f"Genera un mensaje de bienvenida corto, entusiasta y conversacional para {member.name}. "
        "Invítalo a leer las reglas y a presentarse. Máximo 3 oraciones."
    )

    try:
        if groq_client:
            res = groq_client.chat.completions.create(
                messages=[
                    {"role": "system", "content": SYSTEM_PROMPT},
                    {"role": "user", "content": prompt_bienvenida}
                ],
                model="llama-3.1-8b-instant",
                max_tokens=120
            )
            respuesta = res.choices[0].message.content
        else:
            respuesta = (
                f'¡Bienvenido/a a la comunidad, **{member.name}**! 👋 '
                'Pasa a leer las reglas y preséntate cuando quieras.'
            )

        await channel.send(f"{member.mention} {respuesta}")

    except Exception as e:
        print(f"Error en bienvenida: {e}")
        await channel.send(f'¡Hola {member.mention}! 👋 Bienvenido/a a Nerve Community.')


async def _responder_con_gemini(message: discord.Message, pregunta: str) -> str:
    """Responde usando Gemini 2.5 Flash con memoria de conversación por usuario en SQLite."""
    user_id = message.author.id
    
    seven_days_ago = (datetime.datetime.now(datetime.timezone.utc) - datetime.timedelta(days=7)).isoformat()
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute("DELETE FROM memoria_conversacion WHERE timestamp < ?", (seven_days_ago,))
        
        async with db.execute(
            "SELECT role, content FROM memoria_conversacion WHERE user_id = ? ORDER BY id DESC LIMIT ?",
            (user_id, MAX_HISTORY * 2)
        ) as cursor:
            rows = await cursor.fetchall()
            hist = [{"role": r[0], "content": r[1]} for r in reversed(rows)]

    # Construir contexto de conversación previa
    historial_texto = "\n".join(
        f"{'Kaia' if m['role'] == 'assistant' else message.author.name}: {m['content']}"
        for m in hist
    )
    bloques = [SYSTEM_PROMPT, RAG_INSTRUCTION]
    if historial_texto:
        bloques.append(f"Conversación previa:\n{historial_texto}")
    bloques.append(f"{message.author.name}: {pregunta}")

    prompt_completo = "\n\n".join(bloques)

    response = gemini_client.models.generate_content(
        model='gemini-2.5-flash',
        contents=prompt_completo
    )
    respuesta = response.text

    # Guardar turno en memoria
    now_iso = datetime.datetime.now(datetime.timezone.utc).isoformat()
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute("INSERT INTO memoria_conversacion (user_id, role, content, timestamp) VALUES (?, ?, ?, ?)", (user_id, "user", pregunta, now_iso))
        await db.execute("INSERT INTO memoria_conversacion (user_id, role, content, timestamp) VALUES (?, ?, ?, ?)", (user_id, "assistant", respuesta, now_iso))
        
        await db.execute("""
            DELETE FROM memoria_conversacion 
            WHERE id NOT IN (
                SELECT id FROM (
                    SELECT id FROM memoria_conversacion 
                    WHERE user_id = ? 
                    ORDER BY id DESC LIMIT ?
                )
            ) AND user_id = ?
        """, (user_id, MAX_HISTORY * 2, user_id))
        
        await db.commit()

    return respuesta


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    # Moderación automática
    if isinstance(message.author, discord.Member) and not message.author.guild_permissions.manage_messages:
        # 1. Filtro de palabras
        content_lower = message.content.lower()
        if any(bad_word in content_lower for bad_word in BAD_WORDS):
            await message.delete()
            await _add_warn(message.author, "Uso de lenguaje inapropiado")
            await message.channel.send(f"⚠️ {message.author.mention}, tu mensaje ha sido eliminado por usar lenguaje inapropiado.")
            return
            
        # 2. Sistema Anti-spam
        now = time.time()
        user_times = user_message_times[message.author.id]
        user_times.append(now)
        
        if len(user_times) == SPAM_THRESHOLD_MSGS:
            time_diff = user_times[-1] - user_times[0]
            if time_diff <= SPAM_THRESHOLD_SECONDS:
                user_times.clear()
                await _add_warn(message.author, "Spam de mensajes")
                await message.channel.send(f"🚨 {message.author.mention}, deja de hacer spam.")
                return

    # Procesar comandos con prefijo (si los hay)
    ctx = await bot.get_context(message)
    if ctx.valid:
        await bot.process_commands(message)
        return

    content = message.content.strip()
    content_lower = content.lower()
    es_mencion = bot.user.mentioned_in(message)

    # --- RAMA 1: Mención directa → Gemini con memoria por usuario ---
    if es_mencion:
        pregunta = content.replace(f'<@{bot.user.id}>', '').strip()
        if not pregunta:
            await message.reply("¡Aquí estoy! ¿En qué te puedo ayudar?")
            return

        try:
            if gemini_client:
                respuesta = await _responder_con_gemini(message, pregunta)
                if len(respuesta) > 2000:
                    respuesta = respuesta[:1996] + "..."
                await message.reply(respuesta)
            else:
                await message.reply("No tengo acceso a mi modelo principal ahora mismo. Intenta más tarde.")
        except Exception as e:
            print(f"Error Gemini: {e}")
            await message.reply("Lo siento, algo salió mal. Intenta de nuevo en un momento.")
        return

    # --- RAMA 2: Saludo corto sin mención → Groq (respuesta rápida) ---
    palabras = content_lower.split()
    es_saludo_corto = len(palabras) <= 2 and any(p in SALUDOS for p in palabras)

    if es_saludo_corto:
        try:
            if groq_client:
                res = groq_client.chat.completions.create(
                    messages=[
                        {"role": "system", "content": SYSTEM_PROMPT},
                        {"role": "user", "content": (
                            f"{message.author.name} acaba de escribir '{content}'. "
                            "Respóndele el saludo de forma natural y breve."
                        )}
                    ],
                    model="llama-3.1-8b-instant",
                    max_tokens=80
                )
                await message.reply(res.choices[0].message.content)
            else:
                await message.reply(f'¡Hola {message.author.mention}! 👋 ¿Cómo estás?')
        except Exception as e:
            print(f"Error Groq: {e}")
            await message.reply(f'¡Hola {message.author.mention}!')


# --- Comandos Slash ---

@bot.tree.command(name='ping', description="Comprueba la latencia del bot.")
async def ping_command(interaction: discord.Interaction):
    latencia = round(bot.latency * 1000)
    await interaction.response.send_message(f'¡Pong! 🏓 Latencia: **{latencia}ms**')


@bot.tree.command(name='issues', description="Muestra los últimos issues abiertos del repositorio.")
async def issues_command(interaction: discord.Interaction):
    await interaction.response.defer()
    try:
        repo = gh.get_repo(repo_name)
        open_issues = repo.get_issues(state='open', sort='created', direction='desc')
        real_issues = [i for i in open_issues if not i.pull_request]

        if not real_issues:
            await interaction.followup.send("¡No hay issues abiertos ahora mismo! Todo en orden. 🎉")
            return

        msg = f"🔍 **Últimos Issues Abiertos en `{repo_name}`**\n\n"
        for issue in real_issues[:5]:
            msg += f"• [#{issue.number}] {issue.title} — <{issue.html_url}>\n"

        await interaction.followup.send(msg)

    except Exception as e:
        await interaction.followup.send(f"❌ Error al conectar con GitHub: {e}")


@bot.tree.command(name='reto', description="Busca o lista retos en la carpeta retos/ del repo.")
@app_commands.describe(num="Nombre o número del reto a buscar")
async def reto_command(interaction: discord.Interaction, num: str = None):
    await interaction.response.defer()
    try:
        repo = gh.get_repo(repo_name)
        contents = repo.get_contents("retos")

        if not num:
            lista = "\n".join(
                f"• `{c.name}`" for c in contents
                if c.type == "dir" or c.name.endswith('.md')
            )
            await interaction.followup.send(f"📚 **Retos Disponibles:**\n{lista}\n\nUsa `/reto [nombre]` para más info.")
            return

        encontrado = next((c for c in contents if num.lower() in c.name.lower()), None)
        if encontrado:
            await interaction.followup.send(f"🚀 **Reto: {encontrado.name}**\n<{encontrado.html_url}>")
        else:
            await interaction.followup.send(f"❌ No encontré un reto llamado `{num}`.")

    except Exception as e:
        await interaction.followup.send(f"❌ Error al conectar con GitHub: {e}")


@bot.tree.command(name='ayuda', description="Muestra los comandos disponibles.")
async def ayuda_command(interaction: discord.Interaction):
    embed = discord.Embed(
        title="Kaia — Comandos disponibles",
        description="Puedo responder cualquier pregunta si me **mencionas** en el chat.",
        color=discord.Color.purple()
    )
    embed.add_field(name="/ping", value="Comprueba si estoy en línea y mi latencia.", inline=False)
    embed.add_field(name="/issues", value="Lista los últimos issues abiertos en GitHub.", inline=False)
    embed.add_field(name="/reto [nombre]", value="Busca o lista los retos de la comunidad.", inline=False)
    embed.add_field(
        name="@Kaia [pregunta]",
        value="Hazme cualquier pregunta — tengo memoria de nuestra conversación. 🧠",
        inline=False
    )
    embed.set_footer(text="Kaia · Alenia Studios")
    await interaction.response.send_message(embed=embed)


@bot.tree.command(name='warns', description="Muestra las advertencias de un usuario (Solo Moderadores).")
@app_commands.describe(usuario="El usuario a consultar")
@app_commands.default_permissions(manage_messages=True)
async def warns_command(interaction: discord.Interaction, usuario: discord.Member):
    warns = user_warns.get(usuario.id, [])
    if not warns:
        await interaction.response.send_message(f"✅ {usuario.mention} no tiene ninguna advertencia.")
        return
        
    embed = discord.Embed(
        title=f"Advertencias de {usuario.display_name}",
        color=discord.Color.orange()
    )
    for i, w in enumerate(warns, 1):
        dt = datetime.datetime.fromisoformat(w["timestamp"])
        fecha = dt.strftime("%Y-%m-%d %H:%M:%S")
        embed.add_field(name=f"Warn #{i}", value=f"**Motivo:** {w['reason']}\n**Fecha:** {fecha}", inline=False)
        
    await interaction.response.send_message(embed=embed)


@bot.tree.command(name='vincular-github', description="Vincula tu cuenta de GitHub con Discord.")
@app_commands.describe(usuario_github="Tu nombre de usuario en GitHub")
async def vincular_github_command(interaction: discord.Interaction, usuario_github: str):
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute(
            "INSERT OR REPLACE INTO usuarios_github (discord_id, github_username) VALUES (?, ?)",
            (interaction.user.id, usuario_github)
        )
        await db.commit()
    await interaction.response.send_message(f"✅ ¡Cuenta de GitHub `{usuario_github}` vinculada con éxito!", ephemeral=True)


@bot.tree.command(name='tomar-reto', description="Empieza a trabajar en un reto.")
@app_commands.describe(reto_id="Identificador del reto (ej. 01-lista-tareas)")
async def tomar_reto_command(interaction: discord.Interaction, reto_id: str):
    now_iso = datetime.datetime.now(datetime.timezone.utc).isoformat()
    async with aiosqlite.connect(DB_PATH) as db:
        async with db.execute("SELECT estado FROM participantes_retos WHERE user_id = ? AND reto_id = ?", (interaction.user.id, reto_id)) as cursor:
            row = await cursor.fetchone()
            if row:
                if row[0] == 'en_progreso':
                    await interaction.response.send_message(f"⚠️ Ya estás trabajando en `{reto_id}`.", ephemeral=True)
                else:
                    await interaction.response.send_message(f"✅ Ya has completado el reto `{reto_id}`.", ephemeral=True)
                return
        
        await db.execute(
            "INSERT INTO participantes_retos (user_id, reto_id, estado, fecha_inicio) VALUES (?, ?, 'en_progreso', ?)",
            (interaction.user.id, reto_id, now_iso)
        )
        await db.commit()
    await interaction.response.send_message(f"🚀 ¡Has comenzado el reto `{reto_id}`! ¡Mucho éxito!")


@bot.tree.command(name='completar-reto', description="Marca un reto como completado con el link de tu PR.")
@app_commands.describe(reto_id="Identificador del reto", pr_url="URL de tu Pull Request en GitHub")
async def completar_reto_command(interaction: discord.Interaction, reto_id: str, pr_url: str):
    now_iso = datetime.datetime.now(datetime.timezone.utc).isoformat()
    async with aiosqlite.connect(DB_PATH) as db:
        async with db.execute("SELECT estado FROM participantes_retos WHERE user_id = ? AND reto_id = ?", (interaction.user.id, reto_id)) as cursor:
            row = await cursor.fetchone()
            if not row:
                await interaction.response.send_message(f"⚠️ No has empezado el reto `{reto_id}`. Usa `/tomar-reto` primero.", ephemeral=True)
                return
            if row[0] == 'completado':
                await interaction.response.send_message(f"✅ Ya habías completado el reto `{reto_id}`.", ephemeral=True)
                return
                
        # Auto-verificación con Github API
        nuevo_estado = 'pendiente-revision'
        metodo_verif = 'ninguno'
        
        pr_number = None
        try:
            if "pull/" in pr_url:
                pr_number = int(pr_url.split("pull/")[-1].split("/")[0])
        except Exception:
            pass
            
        if pr_number:
            try:
                repo = gh.get_repo(repo_name)
                pr = repo.get_pull(pr_number)
                if pr.is_merged():
                    nuevo_estado = 'completado'
                    metodo_verif = 'automatico'
            except Exception as e:
                print(f"Error comprobando PR {pr_number}: {e}")
                
        await db.execute(
            "UPDATE participantes_retos SET estado = ?, fecha_fin = ?, pr_url = ?, metodo_verificacion = ? WHERE user_id = ? AND reto_id = ?",
            (nuevo_estado, now_iso, pr_url, metodo_verif, interaction.user.id, reto_id)
        )
        await db.commit()
        
    if nuevo_estado == 'completado':
        await interaction.response.send_message(f"🎉 ¡Felicidades! Has completado el reto `{reto_id}` (Verificado automáticamente ✅).\n🔗 PR: <{pr_url}>")
    else:
        await interaction.response.send_message(f"⏳ Has marcado el reto `{reto_id}` para revisión.\nTu PR <{pr_url}> queda `pendiente-revision` hasta que un moderador lo valide o se integre.")


@bot.tree.command(name='mi-progreso', description="Mira qué retos tienes en curso y cuáles has completado.")
async def mi_progreso_command(interaction: discord.Interaction):
    async with aiosqlite.connect(DB_PATH) as db:
        async with db.execute("SELECT reto_id, estado FROM participantes_retos WHERE user_id = ?", (interaction.user.id,)) as cursor:
            rows = await cursor.fetchall()
            
    if not rows:
        await interaction.response.send_message("Aún no has tomado ningún reto. ¡Anímate usando `/tomar-reto`!", ephemeral=True)
        return
        
    en_progreso = [r[0] for r in rows if r[1] == 'en_progreso']
    completados = [r[0] for r in rows if r[1] == 'completado']
    pendientes = [r[0] for r in rows if r[1] == 'pendiente-revision']
    
    embed = discord.Embed(title=f"Progreso de {interaction.user.display_name}", color=discord.Color.green())
    if completados:
        embed.add_field(name="✅ Completados", value="\n".join(f"• {r}" for r in completados), inline=False)
    if pendientes:
        embed.add_field(name="⏳ Pendientes de Revisión", value="\n".join(f"• {r}" for r in pendientes), inline=False)
    if en_progreso:
        embed.add_field(name="🚀 En progreso", value="\n".join(f"• {r}" for r in en_progreso), inline=False)
        
    await interaction.response.send_message(embed=embed)


@bot.tree.command(name='exportar-progreso', description="Exporta tu progreso en los retos a un archivo CSV.")
async def exportar_progreso_command(interaction: discord.Interaction):
    async with aiosqlite.connect(DB_PATH) as db:
        async with db.execute("SELECT reto_id, estado, fecha_inicio, fecha_fin, pr_url FROM participantes_retos WHERE user_id = ?", (interaction.user.id,)) as cursor:
            rows = await cursor.fetchall()
            
    if not rows:
        await interaction.response.send_message("Aún no tienes progreso que exportar. ¡Usa `/tomar-reto` para empezar!", ephemeral=True)
        return
        
    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow(['reto_id', 'estado', 'fecha_inicio', 'fecha_fin', 'pr_url'])
    for row in rows:
        writer.writerow(row)
        
    output.seek(0)
    file = discord.File(fp=io.BytesIO(output.getvalue().encode('utf-8')), filename="mi_progreso_nerve.csv")
    await interaction.response.send_message("Aquí tienes el archivo CSV con tu progreso en los retos de Nerve:", file=file, ephemeral=True)


@bot.tree.command(name='quien-esta-en', description="Mira quiénes están haciendo o ya completaron un reto.")
@app_commands.describe(reto_id="Identificador del reto")
async def quien_esta_en_command(interaction: discord.Interaction, reto_id: str):
    async with aiosqlite.connect(DB_PATH) as db:
        async with db.execute("SELECT user_id, estado FROM participantes_retos WHERE reto_id = ?", (reto_id,)) as cursor:
            rows = await cursor.fetchall()
            
    if not rows:
        await interaction.response.send_message(f"Nadie ha tomado el reto `{reto_id}` aún. ¡Puedes ser el primero!", ephemeral=True)
        return
        
    en_progreso = []
    completados = []
    pendientes = []
    for user_id, estado in rows:
        member = interaction.guild.get_member(user_id)
        name = member.display_name if member else f"Usuario {user_id}"
        if estado == 'en_progreso':
            en_progreso.append(name)
        elif estado == 'completado':
            completados.append(name)
        elif estado == 'pendiente-revision':
            pendientes.append(name)
            
    embed = discord.Embed(title=f"Participantes en: {reto_id}", color=discord.Color.blue())
    if completados:
        embed.add_field(name="✅ Completados", value="\n".join(f"• {name}" for name in completados), inline=False)
    if pendientes:
        embed.add_field(name="⏳ Pendientes de Revisión", value="\n".join(f"• {name}" for name in pendientes), inline=False)
    if en_progreso:
        embed.add_field(name="🚀 En progreso", value="\n".join(f"• {name}" for name in en_progreso), inline=False)
        
    await interaction.response.send_message(embed=embed)


@bot.tree.command(name='ranking', description="Muestra el top de usuarios con más retos completados.")
async def ranking_command(interaction: discord.Interaction):
    async with aiosqlite.connect(DB_PATH) as db:
        async with db.execute("""
            SELECT user_id, COUNT(*) as total 
            FROM participantes_retos 
            WHERE estado = 'completado' 
            GROUP BY user_id 
            ORDER BY total DESC 
            LIMIT 10
        """) as cursor:
            rows = await cursor.fetchall()
            
    if not rows:
        await interaction.response.send_message("El ranking está vacío. ¡Nadie ha completado retos aún!")
        return
        
    embed = discord.Embed(title="🏆 Ranking de Nerve Community", description="Top 10 usuarios con más retos completados:", color=discord.Color.gold())
    
    for i, (user_id, total) in enumerate(rows, 1):
        member = interaction.guild.get_member(user_id)
        name = member.display_name if member else f"Usuario {user_id}"
        medalla = "🥇" if i == 1 else "🥈" if i == 2 else "🥉" if i == 3 else f"{i}."
        embed.add_field(name=f"{medalla} {name}", value=f"{total} retos completados", inline=False)
        
    await interaction.response.send_message(embed=embed)


@bot.tree.command(name='limpiar', description="Limpia mensajes del canal (Solo Dueño/Admin).")
@app_commands.describe(cantidad="Número de mensajes a eliminar")
@app_commands.default_permissions(administrator=True)
async def limpiar_command(interaction: discord.Interaction, cantidad: int = 100):
    if interaction.user != interaction.guild.owner and not interaction.user.guild_permissions.administrator:
        await interaction.response.send_message("❌ Solo el dueño del servidor puede usar este comando.", ephemeral=True)
        return
        
    await interaction.response.defer(ephemeral=True)
    try:
        deleted = await interaction.channel.purge(limit=cantidad)
        await interaction.followup.send(f"✅ Se han eliminado {len(deleted)} mensajes.", ephemeral=True)
    except Exception as e:
        await interaction.followup.send(f"❌ Error al limpiar mensajes: {e}", ephemeral=True)


@bot.tree.command(name='verificar-reto', description="Modifica manualmente el estado de un reto (Solo Mods).")
@app_commands.describe(usuario="Usuario al que verificar", reto_id="ID del reto", estado="completado o pendiente-revision")
@app_commands.default_permissions(manage_messages=True)
async def verificar_reto_command(interaction: discord.Interaction, usuario: discord.Member, reto_id: str, estado: str):
    if estado not in ['completado', 'pendiente-revision']:
        await interaction.response.send_message("❌ El estado debe ser 'completado' o 'pendiente-revision'.", ephemeral=True)
        return
        
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute(
            "UPDATE participantes_retos SET estado = ?, metodo_verificacion = 'manual' WHERE user_id = ? AND reto_id = ?",
            (estado, usuario.id, reto_id)
        )
        await db.commit()
        
    await interaction.response.send_message(f"✅ Reto `{reto_id}` de {usuario.mention} cambiado a `{estado}` (verificado manualmente).")
    try:
        if estado == 'completado':
            await usuario.send(f"🎉 Tu reto `{reto_id}` ha sido verificado manualmente y ahora está completado.")
        else:
            await usuario.send(f"⚠️ Tu reto `{reto_id}` ha vuelto a estar `pendiente-revision` por decisión de un moderador.")
    except Exception:
        pass


# Lista de palabras clave para identificar los 13 retos principiantes
RETOS_PRINCIPIANTES_KEYWORDS = [
    "00", "01-chat", "02-reloj", "03-traductor", 
    "01-lista", "02-web", "03-juego", "04-analiza", 
    "05-genera", "06-conversor", "07-calculadora", "08-organiza", "10-analiza"
]

def contar_retos_principiantes(retos_completados_ids):
    encontrados = set()
    for reto in retos_completados_ids:
        r_lower = reto.lower()
        for i, kw in enumerate(RETOS_PRINCIPIANTES_KEYWORDS):
            if kw in r_lower:
                encontrados.add(i)
    return len(encontrados)

@bot.tree.command(name='mi-elegibilidad', description="Comprueba si ya puedes participar en el Mega Reto.")
async def mi_elegibilidad_command(interaction: discord.Interaction):
    async with aiosqlite.connect(DB_PATH) as db:
        async with db.execute("SELECT reto_id FROM participantes_retos WHERE user_id = ? AND estado = 'completado'", (interaction.user.id,)) as cursor:
            rows = await cursor.fetchall()
            
    completados = [r[0] for r in rows]
    total_requeridos = len(RETOS_PRINCIPIANTES_KEYWORDS)
    logrados = contar_retos_principiantes(completados)
    
    if logrados >= total_requeridos:
        msg = (
            f"🎉 **¡Felicidades {interaction.user.mention}!**\n"
            f"Has completado {logrados}/{total_requeridos} retos Principiante requeridos.\n"
            "🌟 **¡HAS DESBLOQUEADO EL MEGA RETO!** 🌟\n"
            "Consulta los detalles en el repositorio para participar por el Premio Trimestral: `MEGA_RETO.md`"
        )
        await interaction.response.send_message(msg)
    else:
        faltan = total_requeridos - logrados
        await interaction.response.send_message(f"📊 **Tu progreso para el Mega Reto:**\nLlevas {logrados} de {total_requeridos} retos Principiante requeridos. ¡Te faltan {faltan}! Sigue así 💪")


@bot.tree.command(name='elegibles-mega-reto', description="Lista a los usuarios que han desbloqueado el Mega Reto.")
async def elegibles_mega_reto_command(interaction: discord.Interaction):
    await interaction.response.defer()
    async with aiosqlite.connect(DB_PATH) as db:
        async with db.execute("SELECT user_id, reto_id FROM participantes_retos WHERE estado = 'completado'") as cursor:
            rows = await cursor.fetchall()
            
    # Agrupar por usuario
    user_retos = defaultdict(list)
    for user_id, reto_id in rows:
        user_retos[user_id].append(reto_id)
        
    elegibles = []
    total_requeridos = len(RETOS_PRINCIPIANTES_KEYWORDS)
    
    for user_id, retos in user_retos.items():
        if contar_retos_principiantes(retos) >= total_requeridos:
            member = interaction.guild.get_member(user_id)
            name = member.display_name if member else f"Usuario {user_id}"
            elegibles.append(name)
            
    if not elegibles:
        await interaction.followup.send("Aún no hay nadie elegible para el Mega Reto. ¡Se el primero!")
        return
        
    embed = discord.Embed(title="🌟 Elegibles para el Mega Reto 🌟", color=discord.Color.purple())
    embed.add_field(name="Han completado todos los retos principiantes:", value="\n".join(f"• {name}" for name in elegibles), inline=False)
    await interaction.followup.send(embed=embed)


if __name__ == "__main__":
    if not TOKEN:
        print("❌ Error: No se encontró DISCORD_TOKEN.")
    else:
        bot.run(TOKEN)
