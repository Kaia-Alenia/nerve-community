# Ejemplo 02: Pub/Sub Básico (Publicador y Suscriptor)

Este ejemplo demuestra cómo usar `broadcast()` para emitir eventos a múltiples clientes de manera simultánea.

## Patrón que demuestra: Publish / Subscribe (Pub-Sub)
A diferencia de `send()`, donde se especifica a un cliente particular, `broadcast()` emite el payload al Hub, y el Hub lo reparte a **todos** los clientes conectados (excepto a quien lo mandó).
El patrón Pub/Sub se logra haciendo que el **suscriptor** filtre los mensajes que recibe en su callback basándose en algún dato del payload (como un campo `canal` o `topic`). 

## Retos que utilizan esta base:
- `retos/nivel-1-principiante/02-reloj-sincronizado/`: Un reloj central (publicador) emite la hora y varios relojes clientes (suscriptores) la muestran.

## Cómo ejecutarlo:
1. Asegúrate de tener el Hub encendido: `nerve start`
2. Abre dos terminales para simular a dos personas distintas y ejecuta:
   - Terminal 1: `python suscriptor.py usuario_1`
   - Terminal 2: `python suscriptor.py usuario_2`
3. Abre una tercera terminal e inicia el publicador: `python publicador.py`
4. Verás cómo ambos suscriptores reaccionan al mismo tiempo a la transmisión del publicador.
