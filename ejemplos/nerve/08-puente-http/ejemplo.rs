/**
 * Ejemplo: Servidor HTTP con Axum
 * 
 * Qué enseña este ejemplo:
 *   - Crear un servidor HTTP moderno y rápido en Rust usando axum.
 *   - Usar 'serde' para deserializar un cuerpo JSON automáticamente.
 *   - Configurar una ruta POST y enviar una respuesta JSON.
 * 
 * Para tu reto (Puente HTTP para Nerve):
 *   Cuando la ruta reciba los datos, deberás usar el cliente Nerve 
 *   para retransmitir la información hacia el hub de Nerve. Para compartir
 *   el cliente Nerve con Axum, necesitarás usar el sistema de "State" de Axum
 *   con un Arc<Mutex<...>>.
 */

use axum::{
    routing::{get, post},
    Router,
    Json,
};
use serde::{Deserialize, Serialize};

// 1. Estructura para lo que ESPERAMOS recibir
// 'Deserialize' permite a Axum convertir automáticamente el JSON entrante a este struct
#[derive(Deserialize)]
struct MensajePayload {
    mensaje: String,
}

// 2. Estructura para lo que VAMOS a responder
// 'Serialize' permite a Axum convertir el struct a JSON para responder
#[derive(Serialize)]
struct RespuestaPayload {
    status: String,
    recibido: String,
}

#[tokio::main]
async fn main() {
    // 3. Crear el enrutador de la aplicación y definir las rutas
    let app = Router::new()
        .route("/", get(ruta_raiz))
        .route("/enviar", post(recibir_y_reenviar));

    // 4. Iniciar el servidor
    let puerto = "0.0.0.0:3000";
    let listener = tokio::net::TcpListener::bind(puerto).await.unwrap();
    
    println!("Servidor Rust (Axum) escuchando en http://localhost:3000");
    axum::serve(listener, app).await.unwrap();
}

// Ruta GET básica
async fn ruta_raiz() -> &'static str {
    "Servidor funcionando"
}

// 5. Ruta POST que será nuestro "puente"
// Axum se encarga de verificar que el POST tenga un JSON válido y lo mapea a `payload`
async fn recibir_y_reenviar(Json(payload): Json<MensajePayload>) -> Json<RespuestaPayload> {
    
    // En la terminal veremos lo que llegó
    println!("📩 Recibido por HTTP: {}", payload.mensaje);

    // ¡Aquí es donde integrarías Nerve! 
    // Ejemplo: state.cliente_nerve.publicar("canal_http", &payload.mensaje).await;

    // Retornamos un JSON de respuesta
    let respuesta = RespuestaPayload {
        status: "ok".to_string(),
        recibido: payload.mensaje,
    };

    Json(respuesta)
}
