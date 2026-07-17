use nerve::NexusClient;
use serde_json::json;
use std::time::Duration;
use std::thread;

fn main() {
    println!("Iniciando emisor...");
    // 1. Crear el cliente de Nerve
    let mut cliente = NexusClient::new();

    // 2. Conectarse al Hub con un identificador único
    cliente.connect("emisor_01").expect("Error al conectar");
    println!("✅ Emisor conectado al Nerve Hub.");

    // Esperamos un momento para asegurar que el receptor esté listo
    thread::sleep(Duration::from_secs(1));

    // 3. Preparar el mensaje (payload) y enviarlo al receptor
    let mensaje = json!({
        "texto": "¡Hola, Nerve!",
        "timestamp": std::time::SystemTime::now()
            .duration_since(std::time::UNIX_EPOCH)
            .unwrap()
            .as_secs()
    });

    println!("Enviando mensaje a 'receptor_01'...");
    cliente.send("receptor_01", mensaje).expect("Error al enviar");

    println!("Mensaje enviado. Terminando emisor...");
    // Desconectamos el cliente para liberar recursos
    cliente.disconnect();
}
