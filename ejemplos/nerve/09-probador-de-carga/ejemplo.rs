/**
 * Ejemplo: Concurrencia con tokio::spawn en Rust
 * 
 * Qué enseña este ejemplo:
 *   - Lanzar tareas concurrentes asíncronas con `tokio::spawn`.
 *   - Usar `tokio::time::sleep` de manera no bloqueante.
 *   - Esperar a que un conjunto de tareas terminen y recolectar sus resultados con `JoinSet` o `join_all`.
 *   - Medir el tiempo con `std::time::Instant`.
 * 
 * Para tu reto (Probador de Carga Nerve):
 *   Reemplazarás `simular_peticion()` con llamadas al cliente Nerve para 
 *   inundar la red de mensajes lo más rápido posible. Rust y Tokio son
 *   excelentes para lograr el máximo rendimiento en estas pruebas.
 */

use std::time::Instant;
use tokio::time::{sleep, Duration};
use tokio::task::JoinSet;

// 1. Definir una tarea asíncrona
async fn simular_peticion(id: usize) -> bool {
    // Simulamos que enviar un mensaje tarda 100 milisegundos
    sleep(Duration::from_millis(100)).await;
    // Retornamos true indicando éxito
    true
}

#[tokio::main]
async fn main() {
    let total_mensajes = 1000;
    println!("🚀 Iniciando prueba de carga: {} peticiones...", total_mensajes);

    // Guardar el tiempo de inicio
    let inicio = Instant::now();

    // 2. JoinSet es una estructura de Tokio ideal para manejar múltiples tareas
    // concurrentes y esperar a que terminen.
    let mut tareas = JoinSet::new();

    // 3. Lanzamos todas las tareas concurrentemente usando tokio::spawn implícito en JoinSet
    for i in 0..total_mensajes {
        tareas.spawn(async move {
            simular_peticion(i).await
        });
    }

    let mut exitosos = 0;

    // 4. Recolectar los resultados conforme van terminando
    // join_next() espera hasta que UNA de las tareas termine y nos da su resultado
    while let Some(resultado) = tareas.join_next().await {
        match resultado {
            Ok(fue_exito) => {
                if fue_exito {
                    exitosos += 1;
                }
            }
            Err(e) => println!("Error en una tarea: {:?}", e),
        }
    }

    // Calcular el tiempo transcurrido en segundos (con decimales)
    let tiempo_total = inicio.elapsed().as_secs_f64();

    // 5. Mostrar estadísticas
    println!("✅ Prueba finalizada en {:.2} segundos.", tiempo_total);
    println!("📊 Mensajes exitosos: {}/{}", exitosos, total_mensajes);
    println!(
        "⚡ Rendimiento: {:.2} peticiones/segundo",
        (total_mensajes as f64) / tiempo_total
    );
}
