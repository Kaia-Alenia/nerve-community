# 02-pub-sub-basico

##  Propósito
Este ejemplo demuestra cómo usar `broadcast()` para emitir eventos a múltiples clientes de manera simultánea usando el patrón Publish / Subscribe (Pub-Sub).

## 💡 Utilidad
- A diferencia de `send()`, `broadcast()` reparte el mensaje a todos los clientes conectados.
- Muestra cómo el suscriptor filtra los mensajes que recibe basándose en algún dato del payload.

## ⚙️ Instalación / Requisitos
1. Asegúrate de tener el Hub encendido: `nerve start`
2. Abre dos terminales para simular a dos personas distintas y ejecuta:
   - Terminal 1: `python suscriptor.py usuario_1`
   - Terminal 2: `python suscriptor.py usuario_2`
3. Abre una tercera terminal e inicia el publicador: `python publicador.py`

## 🔗 Retos Relacionados
- [Reto 02 — Reloj sincronizado](https://github.com/Kaia-Alenia/nerve-community/issues/2)

## 🛡️ Buenas Prácticas
- Usa identificadores en el payload para filtrar mensajes si los clientes solo deben reaccionar a un tipo de transmisión.
- Evita saturar el Hub con `broadcast` si el mensaje es para un destinatario en particular.
