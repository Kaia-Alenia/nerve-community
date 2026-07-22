# 01-hola-nerve

##  Propósito
Este es el ejemplo más básico ("Hello World") para entender cómo funciona la comunicación con `alenia-nerve`. Demuestra el patrón de Envío Directo (Point-to-Point).

## 💡 Utilidad
- Enseña cómo un emisor puede enviar un mensaje directamente a un receptor específico usando el método `send()`.
- Muestra cómo un receptor puede usar `listen()` para quedarse a la escucha de mensajes.

## ⚙️ Instalación / Requisitos
1. Asegúrate de tener el Hub encendido en una terminal: `nerve start`
2. Abre una terminal y corre el receptor: `python receptor.py`
3. Abre otra terminal y corre el emisor: `python emisor.py`

## 🔗 Retos Relacionados
- [Reto 01 — Chat de terminal](https://github.com/Kaia-Alenia/nerve-community/issues/1)
- [Reto 03 — Traductor de mensajes](https://github.com/Kaia-Alenia/nerve-community/issues/3)

## 🛡️ Buenas Prácticas
- Siempre inicializa el cliente de Nerve con un nombre de cliente único para evitar colisiones.
- Utiliza estructuras simples para los mensajes iniciales al explorar la API de `alenia-nerve`.
