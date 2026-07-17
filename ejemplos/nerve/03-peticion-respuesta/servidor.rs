use nerve::{NexusClient, Message};
use serde_json::json;
use std::sync::mpsc;
use std::sync::{Arc, Mutex};

struct ServidorCalculadora {
    cliente: Arc<Mutex<NexusClient>>,
}

impl ServidorCalculadora {
    fn new() -> Self {
        Self {
            cliente: Arc::new(Mutex::new(NexusClient::new())),
        }
    }

    fn iniciar(&mut self) {
        let mut cli = self.cliente.lock().unwrap();
        cli.connect("servidor_calculadora").expect("Error conectando");
        println!("✅ Servidor Calculadora en línea y esperando peticiones...");

        let cliente_clone = self.cliente.clone();

        cli.listen(move |mensaje_crudo: Message| {
            let remitente = mensaje_crudo.from.clone();
            
            if let Some(payload) = mensaje_crudo.payload {
                if let Some(accion) = payload.get("accion").and_then(|a| a.as_str()) {
                    if accion == "sumar" {
                        let a = payload.get("a").and_then(|v| v.as_f64()).unwrap_or(0.0);
                        let b = payload.get("b").and_then(|v| v.as_f64()).unwrap_or(0.0);
                        let resultado = a + b;

                        println!(" Solicitud de suma recibida de '{}': {} + {} = {}", remitente, a, b, resultado);

                        let respuesta = json!({
                            "accion": "respuesta_operacion",
                            "resultado": resultado
                        });

                        println!("Enviando resultado a '{}'...", remitente);
                        let mut cli_lock = cliente_clone.lock().unwrap();
                        let _ = cli_lock.send(&remitente, respuesta);
                    }
                }
            }
        });
        
        drop(cli);

        let (tx, rx) = mpsc::channel();
        ctrlc::set_handler(move || tx.send(()).expect("Error enviando señal"))
            .expect("Error al configurar ctrl+c");

        rx.recv().expect("Error esperando señal");
        
        println!("\nApagando servidor...");
        let mut cli = self.cliente.lock().unwrap();
        cli.disconnect();
    }
}

fn main() {
    let mut app = ServidorCalculadora::new();
    app.iniciar();
}
