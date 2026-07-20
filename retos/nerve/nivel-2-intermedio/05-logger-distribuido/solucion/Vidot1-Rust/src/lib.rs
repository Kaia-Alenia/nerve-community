pub mod nerve;
mod db;

// Async en Rust es chistoso, MUY chistoso
// tremendo rabbit hole en que entre por usar await
//
// Fue mas divertido que continuar el curso

use rusqlite::{Connection, params};
use serde_json::{Value};
use chrono::Local;

pub const LABEL: &str = "loggerCentral";

// DEvuelve o el valor o el default establecido
fn get_str_param<'a>(msg:&'a Value, param:&str, default: &'a str) -> &'a str {

    // El default de serde_json es Value::Null
    // lo que produciria None a la siguiente funcion en cadena
    // y haria que se devuelva default al final
    msg.get(param)
            .unwrap_or_default()
            .as_str()
            .unwrap_or(default)
}

// Obten los string que nos interesan del mensaje
fn process_msg(notification: &Value) -> (&str, &str, &str) {
    
    // Nombre del nodo
    let origen = notification["from"].as_str().unwrap();

    // Nivel y origen
    let msg = &notification["payload"];

    let nivel = get_str_param(msg, "nivel", "NONE");
    let mensaje = get_str_param(msg, "mensaje", "");

    (origen, nivel, mensaje)
}

// Escribe a la db... duh
fn write_log_to_db(origen: &str, nivel: &str, mensaje: &str) -> Result<usize, rusqlite::Error> {

    let db_connection: Connection = db::create_connection("logs.db")?;
    let timestamp = Local::now().format("%d-%m-%Y %H:%M:%S").to_string();

    db_connection.execute(
        "INSERT INTO logs (origen, nivel, mensaje, timestamp) VALUES (?1, ?2, ?3, ?4)",
        params![origen, nivel, mensaje, timestamp]
    )
}

// Despachador
fn message_dispacher(msg: Value) {
    
    let (origen, nivel, mensaje) = process_msg(&msg);

    if nivel == "NONE" || mensaje.is_empty() {
        println!("Log sent by {} rejected: incorrect parameters", origen);
        return;
    }
    match write_log_to_db(origen, nivel, mensaje) {
        Ok(_) => {},
        Err(e) => println!("Couldn't write log to db: {e}"),
    }
}

pub async fn start_logger() -> Result<(), Box<dyn std::error::Error + Send + Sync>> {

    // Crea cliente
    let client = nerve::make_client(&LABEL).await?;

    // Configura la funcion para despachar mensajes
    client.listen(
        move |msg| { message_dispacher(msg); }, 
        None
    ).await;

    println!("Central logger started.");
    Ok(())
}