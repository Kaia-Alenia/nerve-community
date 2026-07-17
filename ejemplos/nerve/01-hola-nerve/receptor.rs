use nerve::{NexusClient, Message};
use std::sync::mpsc;

fn procesar_mensaje(mensaje_crudo: Message) {
    println!(" ¡Mensaje recibido!: {:?}", mensaje_crudo);

    if let Some(payload) = mensaje_crudo.payload {
        if let Some(texto) = payload.get("texto") {
            println!("Texto extraído: {}", texto);
        }
    }
}

fn main() {
    println!("Iniciando receptor...");
    let mut cliente = NexusClient::new();

    // Nos conectamos como "receptor_01"
    cliente.connect("receptor_01").expect("Error al conectar");
    println!("✅ Receptor conectado. Esperando mensajes...");

    // Registramos la función que se llamará al recibir mensajes
    cliente.listen(procesar_mensaje);

    // Mantenemos el programa vivo para escuchar (ctrl+c para salir)
    let (tx, rx) = mpsc::channel();
    ctrlc::set_handler(move || tx.send(()).expect("Could not send signal on channel."))
        .expect("Error setting Ctrl-C handler");

    println!("Presiona Ctrl+C para salir.");
    rx.recv().expect("Could not receive from channel.");
    
    println!("\nSaliendo...");
    cliente.disconnect();
}
