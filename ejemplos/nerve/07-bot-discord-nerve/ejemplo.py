"""
Ejemplo: Bot básico con discord.py

Qué enseña este ejemplo:
  - Cómo configurar y arrancar un bot de Discord.
  - Cómo escuchar eventos (`on_ready`, `on_message`).
  - El uso de `async`/`await` para programación asíncrona (requerido por Discord).

Para tu reto (Bot Discord Nerve):
  En vez de solo responder con "¡Hola!", conectarás el bot de Discord con
  tu cliente Nerve. Cuando llegue un mensaje a Discord, usarás `cliente.send()`
  para mandarlo a la red Nerve, y viceversa.

Glosario:
  discord.Client()      — La clase base que maneja la conexión con los servidores de Discord.
  discord.Intents       — Los permisos que le pides a Discord. message_content es obligatorio 
                          para poder leer el texto de los mensajes.
  @client.event         — Un decorador que le dice a la librería que esa función manejará un evento.
  async def             — Declara una función asíncrona.
  await                 — Espera a que una tarea asíncrona (como enviar un mensaje a internet) termine.
"""

import discord
import os

# 1. Configurar los "intents" (permisos de qué eventos queremos recibir)
intents = discord.Intents.default()
intents.message_content = True  # ¡Importante para poder leer lo que escriben!

# 2. Inicializar el cliente del bot
client = discord.Client(intents=intents)

# 3. Definir qué pasa cuando el bot se conecta exitosamente
@client.event
async def on_ready():
    print(f'✅ Conectado exitosamente como {client.user}')

# 4. Definir qué pasa cuando alguien envía un mensaje en un canal
@client.event
async def on_message(message):
    # Ignorar mensajes del propio bot para evitar bucles infinitos
    if message.author == client.user:
        return

    # Si alguien dice "ping", el bot responde "pong"
    if message.content.lower() == 'ping':
        print(f"[{message.author}] dijo ping, respondiendo...")
        # 'await' es necesario siempre que interactuemos con la API de Discord
        await message.channel.send('pong 🏓')

def main():
    # Debes reemplazar esto con tu token real o usar una variable de entorno
    token = os.environ.get("DISCORD_TOKEN", "TU_TOKEN_AQUI")
    
    if token == "TU_TOKEN_AQUI":
        print("⚠️ ADVERTENCIA: Reemplaza 'TU_TOKEN_AQUI' con el token de tu bot de Discord.")
        print("Puedes obtenerlo en: https://discord.com/developers/applications")
        return
        
    print("Iniciando bot...")
    client.run(token)

if __name__ == "__main__":
    main()
