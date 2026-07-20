use std::time::Duration;

use nerveLogger::{self, start_logger};

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error + Send + Sync>> {
    
    let _ = start_logger().await?;
    
    println!("Press Ctrl+C to stop...");
    loop {
        tokio::time::sleep(Duration::from_millis(500)).await;
    };

    Ok(())
}