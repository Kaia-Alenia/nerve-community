/*
 * Ejemplo: Escritura de Logs en Rust
 * 
 * Qué enseña este ejemplo:
 *   - Cómo obtener la fecha y hora actual usando el crate externo `chrono`.
 *   - Cómo formatear una fecha en Rust.
 *   - Cómo abrir un archivo en modo Append usando `OpenOptions`.
 *   - Manejo seguro de errores de escritura usando `unwrap_or_else` o `if let Err`.
 * 
 * Para tu reto (Logger Distribuido con Nerve):
 *   En vez de llamar a `escribir_log` con datos estáticos, tu receptor de Nerve
 *   escuchará mensajes de otros nodos y llamará a tu función de log para 
 *   registrarlos en un archivo central.
 * 
 * Glosario:
 *   chrono::Local::now()    — Obtiene la fecha y hora local del sistema.
 *   format("%Y-%m-%d...")   — Da formato a la fecha (requiere el crate chrono).
 *   OpenOptions::new()      — Permite configurar cómo se abre un archivo.
 *   .append(true)           — Configura la apertura para añadir al final.
 *   .create(true)           — Crea el archivo si no existe.
 *   writeln!                — Macro que escribe texto en un archivo con un salto de línea al final.
 */

use chrono::Local;
use std::fs::OpenOptions;
use std::io::Write;

const ARCHIVO_LOG: &str = "sistema.log";

fn escribir_log(nivel: &str, mensaje: &str) {
    // 1. Obtenemos el timestamp actual y lo formateamos usando el crate `chrono`
    let ahora = Local::now();
    let timestamp_formateado = ahora.format("%Y-%m-%d %H:%M:%S").to_string();

    // 2. Construimos la línea de log final
    // Ejemplo: [2026-07-17 15:30:05] [INFO] El servidor ha iniciado correctamente
    let linea_log = format!("[{}] [{}] {}", timestamp_formateado, nivel, mensaje);

    // 3. Imprimimos en consola (opcional, para verlo en vivo)
    println!("{}", linea_log);

    // 4. Abrimos el archivo en modo "Append" (añadir al final) y creamos si no existe
    let archivo_resultado = OpenOptions::new()
        .create(true)
        .append(true)
        .open(ARCHIVO_LOG);

    // 5. Verificamos si se abrió correctamente y escribimos
    match archivo_resultado {
        Ok(mut f) => {
            if let Err(e) = writeln!(f, "{}", linea_log) {
                eprintln!("Error al escribir en el log: {}", e);
            }
        }
        Err(e) => {
            eprintln!("Error al abrir el archivo de log: {}", e);
        }
    }
}

fn main() {
    println!("Escribiendo logs en '{}'...\n", ARCHIVO_LOG);

    escribir_log("INFO", "Sistema iniciado.");
    escribir_log("DEBUG", "Conexión a la base de datos establecida en 14ms.");
    escribir_log("WARNING", "Poco espacio en disco (15% restante).");
    escribir_log("ERROR", "Fallo al procesar el archivo 'datos.csv': Archivo no encontrado.");
    escribir_log("INFO", "Apagando sistema de forma segura.");

    println!("\nRevisa el archivo '{}' para ver los resultados guardados.", ARCHIVO_LOG);
}
