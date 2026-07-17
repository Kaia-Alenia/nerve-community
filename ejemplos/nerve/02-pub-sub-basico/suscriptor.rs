use nerve::{NexusClient, Message};
use std::env;
use std::sync::mpsc;

fn main() {
    let args: Vec<String> = env::args().collect();
    let nombre_nodo = if args.len() > 1 {
        args[1].clone()
    } else {
        "suscriptor_default".to_string()
    }
    
    // Usar un Arc para compartir el nombre_nodo con el closure si es necesario, 
    // pero podemos capturarlo clonándolo
    let nodo_clone = nombre_nodo.clone();
    
    println!("Iniciando {}...", nombre_nodo);
    let mut cliente = NexusClient::new();
    cliente.connect(&nombre_nodo).expect("Error conectando");
    println!("✅ {} conectado. Escuchando el canal 'noticias_tech'...", nombre_nodo);

    let al_recibir_noticia = move |mensaje_crudo: Message| {
        if let Some(payload) = mensaje_crudo.payload {
            if let Some(canal) = payload.get("canal") {
                if canal == "noticias_tech" {
                    let titular = payload.get("titular").and_then(|t| t.as_str()).unwrap_or("Sin titular");
                    println!("[{}]  Nueva noticia interceptada: {}", nodo_clone, titular);
                }
            }
        }
    };

    cliente.listen(al_recibir_noticia);

    let (tx, rx) = mpsc::channel();
    ctrlc::set_handler(move || tx.send(()).expect("Error enviando señal"))
        .expect("Error al configurar ctrl+c");

    rx.recv().expect("Error esperando señal");
    
    println!("\nApagando {}...", nombre_nodo);
    cliente.disconnect();
}
