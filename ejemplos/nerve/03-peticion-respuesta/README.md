# 03-peticion-respuesta

##  Propósito
Demuestra cómo realizar comunicación bidireccional estructurada mediante el patrón Request / Reply (Petición - Respuesta).

##  Utilidad
- Un cliente solicita un dato a un servidor específico enviando un comando.
- El servidor escucha peticiones, procesa la tarea y usa el ID del cliente origen (`"from"`) para enviarle de regreso el resultado exacto.

##  Instalación / Requisitos
1. Asegúrate de tener el Hub encendido: `nerve start`
2. Abre una terminal y corre el servidor: `python servidor.py`
3. Abre otra terminal y ejecuta al cliente: `python cliente.py`

##  Retos Relacionados
- Múltiples retos de nivel-2-intermedio, por ejemplo, [Reto 07 — Bot de Discord](https://github.com/Kaia-Alenia/nerve-community/issues/7).

##  Buenas Prácticas
- Incluye un identificador de petición o la dirección del cliente en el payload original si no usas los metadatos de Nerve.
- Maneja tiempos de espera (timeouts) en el cliente en caso de que el servidor no responda.
