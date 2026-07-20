use std::{time::Duration};

use nerveLogger::{self, nerve};
use serde_json::json;

async fn send_mock_logs() -> Result<(), Box<dyn std::error::Error + Send + Sync>> {
    
    let sender = nerve::make_client("TestSender1").await?;
    
    sender.send(
        nerveLogger::LABEL, 
        json!({
            "nivel": "WARN",
            "mensaje": "Defectos procesando mensajes",
        })
    )?;
    
    sender.send(
        nerveLogger::LABEL, 
        json!({
            "nivel": "INFO",
            "mensaje": "Inicializado proceso #422",
        })
    )?;

    sender.send(
        nerveLogger::LABEL, 
        json!({
            "nivel": "ERROR",
            "mensaje": "Proceso inexistente, cerrando...",
        })
    )?;

    Ok(())
}

async fn send_invalid_logs()  -> Result<(), Box<dyn std::error::Error + Send + Sync>> {

    let sender = nerve::make_client("TestSender2").await?;
    
    sender.send(
        nerveLogger::LABEL, 
        json!({
            "nivel": true,
            "mensaje": false,
        })
    )?;
    
    sender.send(
        nerveLogger::LABEL, 
        json!({
            "nivel": ["no", "valido"],
            "mensaje": 32,
        })
    )?;

    sender.send(
         nerveLogger::LABEL, 
        json!({
            "nivel": 34.4,
            "mensaje": 'd',
        })
    )?;

    Ok(())
}

#[tokio::test]
async fn test_send_msg() {

    let _ =  nerveLogger::start_logger().await;

    // Estos deberian quedar en logs.db
    match send_mock_logs().await {
        Ok(_) => println!("TestSender1 terminado con exito"),
        Err(e) => println!("{}", e),
    }
    
    // Estos deberias bloquearse, mal formados
    match send_invalid_logs().await {
        Ok(_) => println!("TestSender2 terminado con exito"),
        Err(e) => println!("{}", e),
    };
    
    // Dale tiempo para que los mensajes puedan enviarse desde nerve a su destino
    tokio::time::sleep(Duration::from_millis(1000)).await;
}