# Ejemplos: Concurrencia y Pruebas de Carga (Load Tester)

Para crear un "Probador de carga" (Load Tester) efectivo, necesitas enviar muchas peticiones al mismo tiempo (concurrencia) en lugar de enviar una, esperar a que termine, y luego enviar la siguiente.

En el reto "Probador de carga para el Hub de Nerve", utilizarás estos conceptos de concurrencia para instanciar múltiples clientes Nerve o usar un solo cliente para bombardear la red de mensajes lo más rápido posible, midiendo cuánto tarda en responder.

Estos ejemplos muestran cómo ejecutar múltiples tareas "al mismo tiempo" en distintos lenguajes.

## 🐍 Python (asyncio)

Python usa `asyncio` para la concurrencia basada en eventos.

### Cómo ejecutarlo
```bash
python ejemplo.py
```

## 🟨 JavaScript (Promise.all)

JavaScript maneja la concurrencia a través de Promesas asíncronas y el Event Loop.

### Cómo ejecutarlo
```bash
node ejemplo.js
```

## 🐹 Go (Goroutines)

Go fue diseñado para la concurrencia. Las `goroutines` son hilos súper ligeros.

### Cómo ejecutarlo
```bash
go run ejemplo.go
```

## 🦀 Rust (Tokio)

Rust usa `tokio` como runtime asíncrono, permitiendo `tokio::spawn` para tareas concurrentes de muy alto rendimiento.

### Requisitos (Cargo.toml)
```toml
[dependencies]
tokio = { version = "1.0", features = ["full"] }
```

### Cómo ejecutarlo
```bash
cargo run
```
