use rusqlite::{Connection, Result};

pub fn create_connection(path:&str) -> Result<Connection, rusqlite::Error>{
    match Connection::open(path) {
        Ok(c) => Ok(c),
        Err(e) => Err(e),
    }
}
