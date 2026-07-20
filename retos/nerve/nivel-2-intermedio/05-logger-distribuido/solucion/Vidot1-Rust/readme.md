
Mi solucion al reto #5, estoy todavia familiarizandome con Rust
asi que fue un proceso el ver y probar las librerias bien antes de siquiera empezar el programa.

En perspectiva es mas simple de lo que parece, recibe mensajes y los va despachando,
pero el ir entendiendo cada parte para al final juntar las piezas me tomo un poco de tiempo.

Todo esta implementado en `lib.rs`, `main.rs` solo inicializa
el logger y corre un loop de forma indefinida.

# Ejecutar
Asegurate de tener `cargo` instalado,

## Iniciar `nerve`

Inicializa nerve desde un entorno virtual en python:
```bash
python -m venv alenia-env

Linux   -> source alenia-env/bin/activate
Windows -> ./alenia-env/bin/activate

(alenia-env) pip install alenia-nerve
(alenia-env) nerve start --verbose
```

`nerve` debe estar ejecutandose para usar el programa.

## Ejecutar
```bash
cargo run
```
## Correr Tests
```bash
cargo test
```
