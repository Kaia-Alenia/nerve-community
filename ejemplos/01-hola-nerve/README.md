# Ejemplo 01: Hola Nerve

Este es el ejemplo más básico ("Hello World") para entender cómo funciona la comunicación con `alenia-nerve`.

## Patrón que demuestra: Envío Directo (Point-to-Point)
Un **emisor** conoce exactamente a quién le quiere mandar el mensaje (en este caso al `receptor_01`) y usa el método `send()` para enviarlo directamente a ese nodo.
El **receptor** usa `listen()` para quedarse a la escucha de cualquier mensaje que llegue dirigido hacia él.

## Retos que utilizan esta base:
- `retos/nivel-1-principiante/01-chat-terminal/`: El concepto es el mismo, pero bidireccional y manejando el input del usuario.
- `retos/nivel-1-principiante/03-traductor-de-mensajes/`: El emisor manda el texto y el receptor lo procesa de manera idéntica a este ejemplo.

## Cómo ejecutarlo:
1. Asegúrate de tener el Hub encendido en una terminal: `nerve start`
2. Abre una terminal y corre el receptor: `python receptor.py`
3. Abre otra terminal y corre el emisor: `python emisor.py`
