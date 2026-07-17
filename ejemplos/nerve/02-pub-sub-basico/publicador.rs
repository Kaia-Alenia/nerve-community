use nerve::NexusClient;
use serde_json::json;
use std::sync::{atomic::{AtomicBool, Ordering}, Arc};
use std::thread;
use std::time::Duration;

fn main() {
    println!("Iniciando publicador (estación de radio)...");
    let mut cliente = NexusClient::new();
    cliente.connect("publicador_noticias").expect("Error conectando");
    println!("✅ Publicador conectado al Hub.");

    let running = Arc::new(AtomicBool::new(true));
    let r = running.clone();

    ctrlc::set_handler(move || {
        r.store(false, Ordering::SeqCst);
    }).expect("Error setting Ctrl-C handler");

    let mut contador = 1;

    while running.load(Ordering::SeqCst) {
        let titular = format!("Noticia #{}: Nerve Hub funciona genial", contador);
        let noticia = json!({
            "canal": "noticias_tech",
            "titular": titular,
            "timestamp": std::time::SystemTime::now().duration_since(std::time::UNIX_EPOCH).unwrap().as_secs()
        });

        println!(" Transmitiendo (broadcast): {}", titular);
        let _ = cliente.broadcast(noticia);

        contador += 1;
        thread::sleep(Duration::from_secs(3));
    }

    println!("\nApagando publicador...");
    cliente.disconnect();
}
