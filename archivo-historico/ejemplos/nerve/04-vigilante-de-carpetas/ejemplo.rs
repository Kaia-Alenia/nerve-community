/*
 * Ejemplo: Monitoreo de carpeta con notify en Rust
 * 
 * Qué enseña este ejemplo:
 *   - Cómo usar un crate externo (`notify`) para eventos de sistema de archivos.
 *   - Cómo manejar canales (mpsc) entre hilos para procesar eventos asíncronamente.
 *   - Manejo de errores con match y Result en el contexto de eventos continuos.
 * 
 * Para tu reto (Vigilante de carpetas con Nerve):
 *   Aplica esta misma estructura. En vez de solo hacer `println!`, cuando 
 *   ocurra un EventKind::Create o EventKind::Modify, enviarás un mensaje
 *   a los demás nodos usando el cliente Nerve.
 * 
 * Glosario:
 *   std::sync::mpsc::channel — Crea un canal de comunicación de Un Productor a Un Consumidor (MPSC).
 *                              Devuelve un (Sender, Receiver) (tx, rx).
 *   notify::Watcher          — El trait principal para iniciar el monitoreo.
 *   std::fs::create_dir_all  — Crea un directorio y todos sus padres si no existen (como mkdir -p).
 *   match                    — Estructura de control poderosa en Rust que evalúa todos los posibles 
 *                              casos de un enum o valor.
 */

use notify::{Event, EventKind, RecursiveMode, Watcher};
use std::fs;
use std::path::Path;
use std::sync::mpsc::channel;

fn main() {
    let carpeta_a_vigilar = "./carpeta_prueba";

    // Creamos la carpeta si no existe
    if !Path::new(carpeta_a_vigilar).exists() {
        if let Err(e) = fs::create_dir_all(carpeta_a_vigilar) {
            eprintln!("Error al crear carpeta: {}", e);
            return;
        }
        println!("Carpeta creada: {}", carpeta_a_vigilar);
    }

    // 1. Creamos un canal para recibir eventos.
    // 'tx' (transmisor) enviará los eventos, 'rx' (receptor) los leerá en nuestro hilo principal.
    let (tx, rx) = channel();

    // 2. Creamos el observador (watcher).
    // Usamos el "recommended_watcher" que elige el mejor método según el sistema operativo 
    // (inotify en Linux, FSEvents en macOS, ReadDirectoryChangesW en Windows).
    let mut watcher = match notify::recommended_watcher(tx) {
        Ok(w) => w,
        Err(e) => {
            eprintln!("Error creando el watcher: {:?}", e);
            return;
        }
    };

    // 3. Añadimos la ruta a vigilar.
    // RecursiveMode::NonRecursive indica que NO vigilaremos subcarpetas internas.
    if let Err(e) = watcher.watch(Path::new(carpeta_a_vigilar), RecursiveMode::NonRecursive) {
        eprintln!("Error al vigilar la ruta: {:?}", e);
        return;
    }

    println!("👀 Vigilando la carpeta '{}'...", carpeta_a_vigilar);
    println!("Crea, modifica o elimina archivos ahí para ver los eventos. Presiona Ctrl+C para salir.");

    // 4. Bucle infinito para recibir eventos a través del receptor (rx).
    // Esto bloqueará el hilo principal esperando eventos.
    loop {
        match rx.recv() {
            Ok(event_result) => {
                match event_result {
                    Ok(event) => procesar_evento(event),
                    Err(e) => eprintln!("❌ Error de evento: {:?}", e),
                }
            }
            Err(e) => {
                eprintln!("Error leyendo el canal: {:?}", e);
                break;
            }
        }
    }
}

fn procesar_evento(event: Event) {
    // Los eventos en `notify` tienen un `kind` (tipo) y `paths` (rutas afectadas).
    match event.kind {
        EventKind::Create(_) => {
            println!("📁 [CREADO] {:?}", event.paths);
        }
        EventKind::Modify(_) => {
            println!("✏️  [MODIFICADO] {:?}", event.paths);
        }
        EventKind::Remove(_) => {
            println!("🗑️  [ELIMINADO] {:?}", event.paths);
        }
        _ => {
            // Ignoramos otros eventos como accesos de lectura o cambios de metadatos (opcional).
        }
    }
}
