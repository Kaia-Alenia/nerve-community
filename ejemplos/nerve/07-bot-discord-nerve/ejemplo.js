/**
 * Ejemplo: Bot básico con discord.js
 * 
 * Qué enseña este ejemplo:
 *   - Cómo configurar e iniciar un cliente de discord.js.
 *   - El uso de "GatewayIntents" para especificar qué eventos quieres.
 *   - Manejo de eventos con `.on` y `.once`.
 * 
 * Para tu reto (Bot Discord Nerve):
 *   En vez de solo responder con "¡Hola!", conectarás el bot de Discord con
 *   tu cliente Nerve. Cuando llegue un mensaje a Discord, usarás tu cliente 
 *   Nerve para notificar a la red, y viceversa.
 * 
 * Glosario:
 *   Client()                 — Instancia principal del bot de Discord.
 *   GatewayIntentBits        — Sistema de permisos de Discord. `GuildMessages` lee eventos de mensajes,
 *                              y `MessageContent` es necesario para leer el texto en sí.
 *   client.once('ready')     — Se ejecuta UNA SOLA VEZ cuando el bot termina de conectarse.
 *   client.on('messageCreate') — Se ejecuta CADA VEZ que se envía un mensaje.
 *   message.reply()          — Envía un mensaje respondiendo (etiquetando) al usuario original.
 */

const { Client, GatewayIntentBits } = require('discord.js');

// 1. Configurar el cliente y los Intents
const client = new Client({ 
    intents: [
        GatewayIntentBits.Guilds,           // Para poder estar en servidores
        GatewayIntentBits.GuildMessages,    // Para recibir eventos de mensajes
        GatewayIntentBits.MessageContent    // Para poder leer el contenido de los mensajes
    ] 
});

// 2. Evento 'ready': Cuando el bot se conecta exitosamente
client.once('ready', () => {
    console.log(`✅ Conectado exitosamente como ${client.user.tag}`);
});

// 3. Evento 'messageCreate': Cuando alguien envía un mensaje
client.on('messageCreate', async (message) => {
    // Ignorar mensajes enviados por bots (incluyendo el nuestro)
    if (message.author.bot) return;

    // Si alguien dice "ping", respondemos "pong"
    if (message.content.toLowerCase() === 'ping') {
        console.log(`[${message.author.tag}] dijo ping, respondiendo...`);
        // Usar await porque enviar un mensaje es una operación de red
        await message.reply('pong 🏓');
    }
});

// 4. Iniciar el bot
function main() {
    // Debes reemplazar esto con tu token real o usar variables de entorno
    const token = process.env.DISCORD_TOKEN || "TU_TOKEN_AQUI";

    if (token === "TU_TOKEN_AQUI") {
        console.log("⚠️ ADVERTENCIA: Reemplaza 'TU_TOKEN_AQUI' con el token de tu bot de Discord.");
        console.log("Puedes obtenerlo en: https://discord.com/developers/applications");
        return;
    }

    console.log("Iniciando bot...");
    client.login(token);
}

main();
