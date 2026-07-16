# Ejemplo 03: Petición - Respuesta (Request-Reply)

Este ejemplo demuestra cómo realizar comunicación bidireccional estructurada: un cliente solicita un dato a un servidor específico y espera su respuesta de vuelta.

## Patrón que demuestra: Request / Reply (Petición - Respuesta)
Para lograr este patrón, el **cliente** envía un mensaje usando `send()` al servidor, incluyendo un comando (la acción). El **servidor** escucha peticiones con `listen()`, procesa la tarea y al finalizar extrae la variable `"from"` (el ID del cliente que mandó el mensaje) del payload crudo devuelto por Nerve, para mandarle de regreso el resultado exacto.

## Retos que utilizan esta base:
- `retos/nivel-2-intermedio/`: Muchos de los retos de nivel intermedio o avanzado que involucran bases de datos remotas, validación, autenticación, o donde un nodo actúa de "orquestador" utilizan este patrón.

## Cómo ejecutarlo:
1. Asegúrate de tener el Hub encendido: `nerve start`
2. Abre una terminal y corre el servidor para que esté a la escucha: `python servidor.py`
3. Abre otra terminal y ejecuta al cliente: `python cliente.py`
4. Verás cómo el cliente manda la petición de cálculo de "5 + 7", el servidor la procesa y manda el "12" de regreso, y el cliente cierra sesión tras haber recibido su respuesta exitosamente.
