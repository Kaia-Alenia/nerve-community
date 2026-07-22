# Ejemplos: Sockets TCP Base (Nuevo Cliente)

Para crear un cliente de Nerve en un lenguaje completamente nuevo, la pieza fundamental es entender cómo conectarse a un **Socket TCP** para enviar y recibir datos. Nerve internamente funciona pasando objetos JSON sobre TCP (IPC).

Estos ejemplos no utilizan ninguna librería de Nerve, sino las librerías estándar de cada lenguaje para abrir un Socket TCP, enviar un mensaje "Hola" (o un JSON simulado), y esperar una respuesta.

A partir de estas piezas básicas, en el reto "Cliente en Nuevo Lenguaje", construirás las clases o estructuras para encapsular esta conexión, manejar la reconexión y proveer una API amigable (`conectar()`, `publicar()`, `suscribir()`).

## 🐍 Python (socket)

### Cómo ejecutarlo
```bash
# Primero levanta un servidor TCP de prueba (como netcat) en otra terminal:
# nc -l 5000
python ejemplo.py
```

## 🟨 JavaScript (net)

### Cómo ejecutarlo
```bash
# Primero levanta un servidor TCP de prueba:
# nc -l 5000
node ejemplo.js
```

## 🐹 Go (net)

### Cómo ejecutarlo
```bash
# Primero levanta un servidor TCP de prueba:
# nc -l 5000
go run ejemplo.go
```

## 🦀 Rust (std::net)

### Cómo ejecutarlo
```bash
# Primero levanta un servidor TCP de prueba:
# nc -l 5000
cargo run
```
