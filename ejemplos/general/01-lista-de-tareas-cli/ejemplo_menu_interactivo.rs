// Ejemplo: Mini gestor de contactos con menú interactivo y persistencia JSON en Rust
//
// Qué enseña este ejemplo:
//   - Cómo crear un loop con "loop {}"
//   - Cómo leer la entrada del usuario con std::io::stdin()
//   - Cómo leer y guardar archivos con std::fs
//   - Cómo usar serde_json para convertir structs de Rust a JSON y viceversa
//
// Glosario de términos "raros":
//   std::io::stdin().read_line — Lee una línea de texto que escribe el usuario.
//   std::fs::read_to_string    — Lee un archivo completo y lo guarda en un String.
//   serde_json::from_str       — Convierte un String con JSON en una estructura (Vector) de Rust.
//   serde_json::to_string_pretty — Convierte variables de Rust en texto JSON formateado.
//   #[derive(Serialize, Deserialize)] — Magia de Rust que le enseña a tu Struct cómo convertirse a JSON.

use serde::{Deserialize, Serialize};
use std::fs;
use std::io::{self, Write};

const ARCHIVO: &str = "contactos.json";

#[derive(Serialize, Deserialize, Clone)]
struct Contacto {
    nombre: String,
    telefono: String,
}

fn cargar_contactos() -> Vec<Contacto> {
    // Intentamos leer el archivo. Si falla (ej. no existe), devolvemos un vector vacío
    if let Ok(contenido) = fs::read_to_string(ARCHIVO) {
        if let Ok(contactos) = serde_json::from_str(&contenido) {
            return contactos;
        }
    }
    Vec::new()
}

fn guardar_contactos(contactos: &[Contacto]) {
    // Convertimos a JSON con formato bonito (pretty)
    if let Ok(json_str) = serde_json::to_string_pretty(contactos) {
        let _ = fs::write(ARCHIVO, json_str);
    }
}

fn mostrar_contactos(contactos: &[Contacto]) {
    if contactos.is_empty() {
        println!("No hay contactos guardados todavía.");
        return;
    }
    println!("\n--- Tus contactos ---");
    for (i, contacto) in contactos.iter().enumerate() {
        println!("  {}. {} — {}", i + 1, contacto.nombre, contacto.telefono);
    }
}

// Función auxiliar para preguntar algo en consola y obtener un String limpio
fn preguntar(prompt: &str) -> String {
    print!("{}", prompt);
    io::stdout().flush().unwrap(); // Asegura que el prompt se imprima antes de esperar el input
    
    let mut input = String::new();
    io::stdin().read_line(&mut input).unwrap_or_default();
    input.trim().to_string()
}

fn main() {
    let mut contactos = cargar_contactos();

    loop {
        println!("\n=== Gestor de Contactos ===");
        println!("1. Ver contactos");
        println!("2. Agregar contacto");
        println!("3. Actualizar teléfono");
        println!("4. Eliminar contacto");
        println!("5. Salir");

        let opcion = preguntar("\nElige una opción (1-5): ");

        match opcion.as_str() {
            "1" => mostrar_contactos(&contactos),
            "2" => {
                let nombre = preguntar("Nombre: ");
                let telefono = preguntar("Teléfono: ");

                if !nombre.is_empty() {
                    contactos.push(Contacto {
                        nombre: nombre.clone(),
                        telefono,
                    });
                    guardar_contactos(&contactos);
                    println!("✓ Contacto '{}' guardado.", nombre);
                } else {
                    println!("El nombre no puede estar vacío.");
                }
            }
            "3" => {
                mostrar_contactos(&contactos);
                if contactos.is_empty() {
                    continue;
                }

                let idx_str = preguntar("\nNúmero del contacto a actualizar: ");
                if let Ok(mut idx) = idx_str.parse::<usize>() {
                    idx -= 1; // Ajustamos a índice 0
                    if idx < contactos.len() {
                        let nuevo_tel = preguntar("Nuevo teléfono: ");
                        contactos[idx].telefono = nuevo_tel;
                        guardar_contactos(&contactos);
                        println!("✓ Contacto actualizado.");
                    } else {
                        println!("Número inválido.");
                    }
                } else {
                    println!("Por favor, ingresa un número válido.");
                }
            }
            "4" => {
                mostrar_contactos(&contactos);
                if contactos.is_empty() {
                    continue;
                }

                let idx_str = preguntar("\nNúmero del contacto a eliminar: ");
                if let Ok(mut idx) = idx_str.parse::<usize>() {
                    idx -= 1;
                    if idx < contactos.len() {
                        let eliminado = contactos.remove(idx); // Elimina y retorna el elemento
                        guardar_contactos(&contactos);
                        println!("✓ Contacto '{}' eliminado.", eliminado.nombre);
                    } else {
                        println!("Número inválido.");
                    }
                } else {
                    println!("Por favor, ingresa un número válido.");
                }
            }
            "5" => {
                println!("¡Hasta luego!");
                break;
            }
            _ => println!("Opción no reconocida, intenta de nuevo."),
        }
    }
}
