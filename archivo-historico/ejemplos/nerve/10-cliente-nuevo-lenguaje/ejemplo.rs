/**
 * Ejemplo: Cliente de Socket TCP en Rust
 * 
 * Qué enseña este ejemplo:
 *   - Conectarse a un servidor usando `std::net::TcpStream` de la librería estándar de Rust.
 *   - Escribir en el stream de red de forma segura.
 *   - Leer la respuesta del servidor en un buffer.
 * 
 * Para tu reto (Nuevo Cliente Nerve):
 *   Rust te obliga a ser muy preciso con la memoria y la pertenencia (ownership).
 *   En un cliente real, probablemente querrás usar `tokio::net::TcpStream` 
 *   (asíncrono) para poder separar la lógica de envío de la lógica de escucha, 
 *   o usar hilos (`std::thread::spawn`) para leer del socket continuamente 
 *   mientras otra parte del programa escribe.
 */

use std::io::{Read, Write};
use std::net::TcpStream;
use serde_json::json;

fn main() {
    let host = "127.0.0.1";
    let puerto = "5000";
    let direccion = format!("{}:{}", host, puerto);

    println!("🔄 Conectando a {}...", direccion);

    // 1. Intentar conectar (esto bloquea hasta conectar o fallar)
    match TcpStream::connect(&direccion) {
        Ok(mut stream) => {
            println!("✅ Conectado exitosamente");

            // 2. Preparar el payload usando la macro `json!` de serde_json
            let payload = json!({
                "tipo": "publicar",
                "canal": "test",
                "contenido": "Hola desde el nuevo cliente Rust!"
            });

            // 3. Convertir el JSON a String y agregar salto de línea
            let mut datos_str = payload.to_string();
            datos_str.push('\n');

            // 4. Enviar los datos escribiendo en el stream de red
            // as_bytes() convierte el String en &[u8] que es lo que espera write_all
            if let Err(e) = stream.write_all(datos_str.as_bytes()) {
                println!("Error enviando los datos: {}", e);
                return;
            }
            println!("⬆️ Enviado: {}", datos_str.trim());

            // 5. Preparar un buffer (arreglo de 1024 bytes) para recibir la respuesta
            let mut buffer = [0; 1024];

            // 6. Leer la respuesta del servidor
            match stream.read(&mut buffer) {
                Ok(bytes_leidos) => {
                    if bytes_leidos == 0 {
                        println!("⚠️ El servidor cerró la conexión sin responder.");
                    } else {
                        // Convertir los bytes leídos de vuelta a String
                        // Solo tomamos el "slice" de los bytes que realmente se leyeron
                        let respuesta = String::from_utf8_lossy(&buffer[0..bytes_leidos]);
                        println!("⬇️ Recibido: {}", respuesta.trim());
                    }
                }
                Err(e) => {
                    println!("Error leyendo respuesta: {}", e);
                }
            }
        }
        Err(e) => {
            println!("❌ No se pudo conectar. ¿Está el servidor encendido?");
            println!("Detalle: {}", e);
        }
    }
}
