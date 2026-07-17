/**
 * Ejemplo: Bot básico con serenity
 * 
 * Qué enseña este ejemplo:
 *   - Cómo configurar e iniciar un cliente de serenity en Rust.
 *   - Implementar el trait EventHandler para manejar eventos.
 *   - El uso de "GatewayIntents" para especificar qué eventos quieres.
 * 
 * Para tu reto (Bot Discord Nerve):
 *   En vez de solo responder con "¡Hola!", conectarás el bot de Discord con
 *   tu cliente Nerve. Cuando llegue un mensaje a Discord, usarás tu cliente 
 *   Nerve para notificar a la red, y viceversa.
 * 
 * Glosario:
 *   serenity::Client::builder() — Constructor del cliente de Discord.
 *   GatewayIntents              — Sistema de permisos. Necesitas GUILD_MESSAGES y MESSAGE_CONTENT.
 *   EventHandler                — Trait que implementas para recibir eventos.
 *   ctx.say(&msg.content)       — Método conveniente para responder en el mismo canal.
 */

use serenity::async_trait;
use serenity::model::channel::Message;
use serenity::model::gateway::Ready;
use serenity::prelude::*;
use std::env;

// 1. Definir nuestra estructura Handler que manejará los eventos
struct Handler;

// 2. Implementar el trait EventHandler para nuestra estructura
#[async_trait]
impl EventHandler for Handler {
    // Evento message: Se llama cada vez que se envía un mensaje
    async fn message(&self, ctx: Context, msg: Message) {
        // Ignorar mensajes enviados por nuestro propio bot (u otros bots)
        if msg.author.bot {
            return;
        }

        // Si el mensaje es "ping", respondemos "pong"
        if msg.content.to_lowercase() == "ping" {
            println!("[{}] dijo ping, respondiendo...", msg.author.name);
            
            // Enviar un mensaje de respuesta
            if let Err(why) = msg.reply(&ctx.http, "pong 🏓").await {
                println!("Error enviando mensaje: {:?}", why);
            }
        }
    }

    // Evento ready: Se llama cuando el bot se conecta exitosamente
    async fn ready(&self, _: Context, ready: Ready) {
        println!("✅ Conectado exitosamente como {}", ready.user.name);
    }
}

#[tokio::main]
async fn main() {
    // 3. Obtener el token. Reemplaza esto o usa variables de entorno
    let mut token = env::var("DISCORD_TOKEN").unwrap_or_else(|_| "TU_TOKEN_AQUI".to_string());

    if token == "TU_TOKEN_AQUI" {
        println!("⚠️ ADVERTENCIA: Reemplaza 'TU_TOKEN_AQUI' con el token de tu bot de Discord.");
        println!("Puedes obtenerlo en: https://discord.com/developers/applications");
        return;
    }

    // 4. Configurar los Intents (permisos)
    // GUILD_MESSAGES para recibir los eventos y MESSAGE_CONTENT para leer el texto
    let intents = GatewayIntents::GUILD_MESSAGES
        | GatewayIntents::MESSAGE_CONTENT
        | GatewayIntents::GUILDS;

    // 5. Crear el cliente con el token, los intents y nuestro Handler
    let mut client = Client::builder(&token, intents)
        .event_handler(Handler)
        .await
        .expect("Error creando el cliente");

    println!("Iniciando bot...");

    // 6. Iniciar la conexión
    if let Err(why) = client.start().await {
        println!("Error en el cliente: {:?}", why);
    }
}
