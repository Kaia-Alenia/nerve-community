# Ejemplos: Servidor HTTP Básico (Puente HTTP)

Para construir un puente HTTP, necesitas levantar un servidor web que pueda escuchar peticiones (como un `POST`), leer un cuerpo en JSON, y luego hacer algo con él. En el reto "Puente HTTP para Nerve", tu servidor recibirá una petición HTTP y usará el cliente Nerve para enviar esa información a la red.

Estos ejemplos muestran cómo crear servidores HTTP muy simples y modernos en distintos lenguajes, sin añadir mucha complejidad, preparándote para integrarlos con tu cliente Nerve.

## 🐍 Python (FastAPI)

FastAPI es un framework moderno y rápido.

### Requisitos
```bash
pip install fastapi uvicorn
```

### Cómo ejecutarlo
```bash
# El archivo debe llamarse ejemplo.py
uvicorn ejemplo:app --reload
```
Para probarlo, puedes usar cURL:
```bash
curl -X POST -H "Content-Type: application/json" -d '{"mensaje": "Hola Mundo"}' http://localhost:8000/enviar
```

## 🟨 JavaScript (Express)

Express es el estándar de facto para servidores web rápidos en Node.js.

### Requisitos
```bash
npm install express
```

### Cómo ejecutarlo
```bash
node ejemplo.js
```
Para probarlo:
```bash
curl -X POST -H "Content-Type: application/json" -d '{"mensaje": "Hola Node"}' http://localhost:3000/enviar
```

## 🐹 Go (net/http estándar)

Go incluye un servidor HTTP de producción directamente en su librería estándar, no necesitas instalar nada.

### Cómo ejecutarlo
```bash
go run ejemplo.go
```
Para probarlo:
```bash
curl -X POST -H "Content-Type: application/json" -d '{"mensaje": "Hola Go"}' http://localhost:8080/enviar
```

## 🦀 Rust (Axum)

Axum es un framework web muy popular y rápido del ecosistema Tokio.

### Requisitos (Cargo.toml)
```toml
[dependencies]
axum = "0.7"
tokio = { version = "1.0", features = ["full"] }
serde = { version = "1.0", features = ["derive"] }
serde_json = "1.0"
```

### Cómo ejecutarlo
```bash
cargo run
```
Para probarlo:
```bash
curl -X POST -H "Content-Type: application/json" -d '{"mensaje": "Hola Rust"}' http://localhost:3000/enviar
```
