use std::time::Duration;
use alenia_nerve::{NexusClient};

const RETRY_INTERVAL:Duration = Duration::from_millis(250);
const CONFIG_PATH:&str = "";

pub async fn make_client(name: &str) -> Result<NexusClient, Box<dyn std::error::Error + Send + Sync>> {
    let mut client = NexusClient::new(RETRY_INTERVAL, CONFIG_PATH, None);
    
    let _response = client
        .connect(name)
        .await?;
    Ok(client)
}