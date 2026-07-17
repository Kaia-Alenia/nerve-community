use nerve::{NexusClient, Message};
use serde_json::json;
use std::sync::{Arc, Mutex};
use std::thread;
use std::time::Duration;

struct ClientePeticion {
    cliente: NexusClient,
    respuesta_recibida: Arc<Mutex<Option<f64>>>,
}

impl ClientePeticion {
    fn new() -> Self {
        Self {
            cliente: NexusClient::new(),
            respuesta_recibida: Arc::new(Mutex::new(None)),
        }
    }

    fn iniciar(&mut self) {
        self.cliente.connect("cliente_calculadora").expect("Error conectando");
        
        let respuesta_clone = self.respuesta_recibida.clone();
        
        self.cliente.listen(move |mensaje_crudo: Message| {
            if let Some(payload) = mensaje_crudo.payload {
                if let Some(accion) = payload.get("accion").and_then(|a| a.as_str()) {
                    if accion == "respuesta_operacion" {
                        if let Some(resultado) = payload.get("resultado").and_then(|r| r.as_f64()) {
                            let mut resp = respuesta_clone.lock().unwrap();
                            *resp = Some(resultado);
                            println!("✅ ¡El servidor respondió! El resultado es: {}", resultado);
                        }
                    }
                }
            }
        });

        println!("Enviando petición de suma al servidor (5 + 7)...");
        let peticion = json!({
            "accion": "sumar",
            "a": 5.0,
            "b": 7.0
        });
        self.cliente.send("servidor_calculadora", peticion).expect("Error al enviar");

        let mut tiempo_espera = 0;
        loop {
            let resp = self.respuesta_recibida.lock().unwrap();
            if resp.is_some() || tiempo_espera >= 5 {
                break;
            }
            drop(resp); // liberar el lock para el sleep

            println!("⏳ Esperando respuesta...");
            thread::sleep(Duration::from_secs(1));
            tiempo_espera += 1;
        }

        let resp = self.respuesta_recibida.lock().unwrap();
        if resp.is_none() {
            println!("❌ Tiempo de espera agotado. El servidor no contestó.");
        }

        self.cliente.disconnect();
    }
}

fn main() {
    let mut app = ClientePeticion::new();
    app.iniciar();
}
