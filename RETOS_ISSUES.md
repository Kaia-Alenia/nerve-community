# Issues de los Retos (Plantillas para GitHub)

A continuación tienes el texto para copiar y pegar y crear los 10 issues de los retos en GitHub. Recuerda asignarles las etiquetas correctas a cada uno (ej. `good-first-issue`, `nivel-X`, `disponible`).

---

# Reto 01: chat-terminal

**Título:** Reto 01: chat-terminal

## 🎯 Objetivo
Construir dos scripts de Python que se envíen mensajes de texto en tiempo real usando NexusClient de Nerve para simular un chat en terminal.

## 📚 Qué vas a aprender
- Sockets básicos e inicialización de clientes Nerve.
- Ingreso y salida de datos estándar (input/output).
- Manejo de callbacks para recibir mensajes asíncronos.

## 🧩 Nivel
Principiante

## 🛠️ Tecnologías sugeridas
- Python 3.10+
- `alenia-nerve`

## 📋 Requisitos
- [ ] Debe existir un script `emisor.py` (o similar) que lea la consola con `input()` y envíe el texto.
- [ ] Debe existir un script `receptor.py` que imprima los mensajes que llegan.
- [ ] El código debe estar correctamente comentado.

## 💡 Pistas
- Usa `client.send()` para enviar el texto ingresado.
- Usa el decorador `@client.on("nombre_del_canal")` para definir qué hacer cuando llegue un mensaje.
- Recuerda usar un pequeño ciclo como `while True` para que el script no se cierre de inmediato.

## 📦 Entregable
- El código dentro de la carpeta `retos/nivel-1-principiante/01-chat-terminal/`.
- Un `README.md` corto del reto explicando cómo probarlo.
- Una captura de pantalla opcional.

## 🙋 ¿Primera vez contribuyendo?
Lee nuestra guía [Cómo hacer tu primer PR](https://github.com/Kaia-Alenia/nerve-community/blob/main/COMO-HACER-TU-PRIMER-PR.md), ¡no hay preguntas tontas!

## 🎓 ¿Sabías que...?
Las soluciones más pulidas y completas de este reto pueden ser invitadas a integrarse directamente al repositorio de producción [zenith-nerve-tools](https://github.com/Kaia-Alenia/zenith-nerve-tools), con crédito total para ti como autor/a. ¡Esfuérzate, tu código puede terminar siendo una herramienta real que otros usen!

---

# Reto 02: reloj-sincronizado

**Título:** Reto 02: reloj-sincronizado

## 🎯 Objetivo
Un script actuará como el "reloj maestro" transmitiendo la hora cada segundo a través de Nerve, y otro script la recibirá y mostrará con colores bonitos en la terminal.

## 📚 Qué vas a aprender
- Uso de ciclos infinitos controlados (`time.sleep`).
- Formateo de texto en terminal con colores.
- Integración de librerías externas (`rich`).

## 🧩 Nivel
Principiante

## 🛠️ Tecnologías sugeridas
- Python 3.10+
- `alenia-nerve`
- `rich` (o `colorama`)

## 📋 Requisitos
- [ ] El script emisor debe enviar la hora actual cada 1 segundo (usando `datetime`).
- [ ] El script receptor debe actualizar la pantalla o imprimir la hora con algún color llamativo.
- [ ] El código debe manejar interrupciones de teclado (Ctrl+C) de forma limpia.

## 💡 Pistas
- Puedes usar `from datetime import datetime` para obtener la hora.
- Instala `rich` con `pip install rich` y usa `from rich import print` para imprimir en colores súper fácil.

## 📦 Entregable
- El código dentro de la carpeta `retos/nivel-1-principiante/02-reloj-sincronizado/`.
- Un `README.md` corto del reto explicando cómo probarlo y qué dependencias instalar.
- Un gif o captura del reloj funcionando.

## 🙋 ¿Primera vez contribuyendo?
Lee nuestra guía [Cómo hacer tu primer PR](https://github.com/Kaia-Alenia/nerve-community/blob/main/COMO-HACER-TU-PRIMER-PR.md), ¡no hay preguntas tontas!

## 🎓 ¿Sabías que...?
Las soluciones más pulidas y completas de este reto pueden ser invitadas a integrarse directamente al repositorio de producción [zenith-nerve-tools](https://github.com/Kaia-Alenia/zenith-nerve-tools), con crédito total para ti como autor/a. ¡Esfuérzate, tu código puede terminar siendo una herramienta real que otros usen!

---

# Reto 03: traductor-de-mensajes

**Título:** Reto 03: traductor-de-mensajes

## 🎯 Objetivo
Recibir un texto en un script a través de Nerve, traducirlo al inglés (usando una API o diccionario) y enviarlo de regreso o imprimirlo.

## 📚 Qué vas a aprender
- Consumo de APIs externas (ej. Google Translate API no oficial o MyMemory).
- Manejo de objetos JSON y respuestas de red.
- Comunicación bidireccional simple en IPC.

## 🧩 Nivel
Principiante

## 🛠️ Tecnologías sugeridas
- Python 3.10+
- `alenia-nerve`
- `requests` o `deep-translator`

## 📋 Requisitos
- [ ] Un script ingresa una frase en español y la envía a través de Nerve.
- [ ] El otro script la intercepta, la traduce usando una API o librería, y muestra el resultado.
- [ ] Debe contemplar el manejo de errores (ej. si no hay internet).

## 💡 Pistas
- La librería `deep-translator` es muy sencilla de usar sin necesidad de llaves de API.
- Puedes mandar los datos usando diccionarios: `{"texto": "Hola", "idioma": "en"}`.

## 📦 Entregable
- El código dentro de la carpeta `retos/nivel-1-principiante/03-traductor-de-mensajes/`.
- Un `README.md` explicando cómo probarlo y qué instalar.

## 🙋 ¿Primera vez contribuyendo?
Lee nuestra guía [Cómo hacer tu primer PR](https://github.com/Kaia-Alenia/nerve-community/blob/main/COMO-HACER-TU-PRIMER-PR.md), ¡no hay preguntas tontas!

## 🎓 ¿Sabías que...?
Las soluciones más pulidas y completas de este reto pueden ser invitadas a integrarse directamente al repositorio de producción [zenith-nerve-tools](https://github.com/Kaia-Alenia/zenith-nerve-tools), con crédito total para ti como autor/a. ¡Esfuérzate, tu código puede terminar siendo una herramienta real que otros usen!

---

# Reto 04: vigilante-de-carpetas

**Título:** Reto 04: vigilante-de-carpetas

## 🎯 Objetivo
Un script monitoreará una carpeta por archivos nuevos creados, y notificará vía Nerve a otro script que actuará como un "panel de control" de alertas.

## 📚 Qué vas a aprender
- Manejo de eventos del sistema de archivos.
- Patrón Productor/Consumidor.
- Ejecución de procesos en segundo plano.

## 🧩 Nivel
Intermedio

## 🛠️ Tecnologías sugeridas
- Python 3.10+
- `alenia-nerve`
- `watchdog`

## 📋 Requisitos
- [ ] El "vigilante" debe usar `watchdog` para detectar cuando un archivo nuevo se crea en una carpeta.
- [ ] Al detectar un archivo, se debe enviar el nombre del archivo y la hora al "panel".
- [ ] El "panel" debe imprimir la alerta.

## 💡 Pistas
- La documentación de `watchdog` tiene un ejemplo rápido en su README que puedes adaptar.
- El mensaje de Nerve puede ser un JSON conteniendo `nombre_archivo`, `tipo_evento`, etc.

## 📦 Entregable
- El código dentro de la carpeta `retos/nivel-2-intermedio/04-vigilante-de-carpetas/`.
- Un `README.md` corto del reto.

## 🙋 ¿Primera vez contribuyendo?
Lee nuestra guía [Cómo hacer tu primer PR](https://github.com/Kaia-Alenia/nerve-community/blob/main/COMO-HACER-TU-PRIMER-PR.md), ¡no hay preguntas tontas!

## 🎓 ¿Sabías que...?
Las soluciones más pulidas y completas de este reto pueden ser invitadas a integrarse directamente al repositorio de producción [zenith-nerve-tools](https://github.com/Kaia-Alenia/zenith-nerve-tools), con crédito total para ti como autor/a. ¡Esfuérzate, tu código puede terminar siendo una herramienta real que otros usen!

---

# Reto 05: logger-distribuido

**Título:** Reto 05: logger-distribuido

## 🎯 Objetivo
Varios scripts (clientes) mandan sus mensajes de "log" (info, warning, error) a un nodo central que los guarda en una base de datos SQLite y permite consultarlos.

## 📚 Qué vas a aprender
- Bases de datos simples (SQLite 3).
- Inserción y agregación de datos relacionales.
- Manejo concurrente de mensajes.

## 🧩 Nivel
Intermedio

## 🛠️ Tecnologías sugeridas
- Python 3.10+
- `alenia-nerve`
- `sqlite3` (built-in de Python)

## 📋 Requisitos
- [ ] El "servidor de logs" debe crear una tabla en SQLite si no existe al arrancar.
- [ ] Debe recibir mensajes por Nerve de al menos dos clientes distintos.
- [ ] Los logs deben guardarse con su marca de tiempo (timestamp), nivel de severidad y el texto.

## 💡 Pistas
- Recuerda hacer `.commit()` en sqlite3 después de hacer un INSERT, o los datos no se guardarán en el disco.
- Prueba simulando clientes con un pequeño ciclo que mande un log aleatorio cada X segundos.

## 📦 Entregable
- El código dentro de la carpeta `retos/nivel-2-intermedio/05-logger-distribuido/`.
- Un `README.md` corto del reto explicando cómo iniciar el servidor y los clientes.

## 🙋 ¿Primera vez contribuyendo?
Lee nuestra guía [Cómo hacer tu primer PR](https://github.com/Kaia-Alenia/nerve-community/blob/main/COMO-HACER-TU-PRIMER-PR.md), ¡no hay preguntas tontas!

## 🎓 ¿Sabías que...?
Las soluciones más pulidas y completas de este reto pueden ser invitadas a integrarse directamente al repositorio de producción [zenith-nerve-tools](https://github.com/Kaia-Alenia/zenith-nerve-tools), con crédito total para ti como autor/a. ¡Esfuérzate, tu código puede terminar siendo una herramienta real que otros usen!

---

# Reto 06: puente-de-progreso-gif

**Título:** Reto 06: puente-de-progreso-gif

## 🎯 Objetivo
Un script se encarga de procesar una imagen pesada (o aplicar un filtro usando Pillow) de forma lenta, y reporta su porcentaje de progreso a través de Nerve a un segundo script que muestra una barra de carga.

## 📚 Qué vas a aprender
- Procesamiento de imágenes en Python.
- Reporte de estado / telemetría en tiempo real.
- Diseño de interfaces de terminal avanzadas (ej. con tqdm).

## 🧩 Nivel
Intermedio

## 🛠️ Tecnologías sugeridas
- Python 3.10+
- `alenia-nerve`
- `Pillow`
- `tqdm` (para la barra de progreso)

## 📋 Requisitos
- [ ] Un script debe aplicar un filtro a una imagen (por iteraciones) y calcular qué porcentaje lleva avanzado.
- [ ] Este script debe mandar el % a Nerve.
- [ ] El script visualizador debe actualizar una barra de progreso de `tqdm` basada en el porcentaje recibido.

## 💡 Pistas
- Puedes simular que el procesamiento es más lento poniendo `time.sleep(0.05)` dentro de tu ciclo de la imagen.
- En `tqdm`, puedes usar `bar.update(x)` manual para subir el porcentaje de la barra en la terminal.

## 📦 Entregable
- El código dentro de la carpeta `retos/nivel-2-intermedio/06-puente-de-progreso-gif/`.
- Un `README.md` y un pequeño `.gif` mostrando cómo se ve tu barra de carga.

## 🙋 ¿Primera vez contribuyendo?
Lee nuestra guía [Cómo hacer tu primer PR](https://github.com/Kaia-Alenia/nerve-community/blob/main/COMO-HACER-TU-PRIMER-PR.md), ¡no hay preguntas tontas!

## 🎓 ¿Sabías que...?
Las soluciones más pulidas y completas de este reto pueden ser invitadas a integrarse directamente al repositorio de producción [zenith-nerve-tools](https://github.com/Kaia-Alenia/zenith-nerve-tools), con crédito total para ti como autor/a. ¡Esfuérzate, tu código puede terminar siendo una herramienta real que otros usen!

---

# Reto 07: bot-discord-nerve

**Título:** Reto 07: bot-discord-nerve

## 🎯 Objetivo
Crear un bot de Discord que, al recibir un comando en un canal (como `!estado`), mande una señal por Nerve a un script local en tu computadora y responda en Discord con la información local que obtuvo.

## 📚 Qué vas a aprender
- Integración de bots y APIs asíncronas de Discord.
- Arquitectura cliente-servidor puenteando internet y procesos locales.
- Manejo de corrutinas (`async`/`await`).

## 🧩 Nivel
Intermedio

## 🛠️ Tecnologías sugeridas
- Python 3.10+
- `alenia-nerve`
- `discord.py`

## 📋 Requisitos
- [ ] El bot de Discord debe estar en un script y conectarse al servidor correctamente.
- [ ] Cuando alguien escribe un comando específico, el bot debe comunicarse con tu otro script de Python (vía Nerve).
- [ ] El bot debe esperar la respuesta del script local, y enviarla en el canal de Discord.

## 💡 Pistas
- `discord.py` usa `asyncio`. Si usas Nerve de manera sincrónica dentro de un evento de Discord, ¡cuidado de no bloquear el hilo! (Puedes usar el cliente Nerve en un hilo secundario).
- Nunca subas tu Token de Discord al repositorio, usa variables de entorno (`.env`).

## 📦 Entregable
- El código dentro de la carpeta `retos/nivel-2-intermedio/07-bot-discord-nerve/`.
- Un `README.md` explicando que el usuario necesita su propio token para probarlo.
- Archivo `.gitignore` para ignorar el `.env`.

## 🙋 ¿Primera vez contribuyendo?
Lee nuestra guía [Cómo hacer tu primer PR](https://github.com/Kaia-Alenia/nerve-community/blob/main/COMO-HACER-TU-PRIMER-PR.md), ¡no hay preguntas tontas!

## 🎓 ¿Sabías que...?
Las soluciones más pulidas y completas de este reto pueden ser invitadas a integrarse directamente al repositorio de producción [zenith-nerve-tools](https://github.com/Kaia-Alenia/zenith-nerve-tools), con crédito total para ti como autor/a. ¡Esfuérzate, tu código puede terminar siendo una herramienta real que otros usen!

---

# Reto 08: puente-http

**Título:** Reto 08: puente-http

## 🎯 Objetivo
Exponer un endpoint HTTP usando FastAPI. Cuando el endpoint reciba un POST, traducirá la petición a un mensaje de Nerve IPC, lo enviará al ecosistema, obtendrá la respuesta, y la regresará como respuesta HTTP.

## 📚 Qué vas a aprender
- Integración de protocolos (HTTP a IPC).
- Diseño de APIs RESTful usando FastAPI.
- Desacoplamiento de sistemas.

## 🧩 Nivel
Avanzado

## 🛠️ Tecnologías sugeridas
- Python 3.10+
- `alenia-nerve`
- `FastAPI`, `uvicorn`

## 📋 Requisitos
- [ ] El servidor FastAPI debe tener al menos una ruta POST (ej. `/enviar-mensaje`).
- [ ] Al recibir la solicitud HTTP, debe conectarse como cliente de Nerve (o tener la conexión ya abierta) y despachar el dato.
- [ ] Si la operación tiene éxito, devolver HTTP 200 al usuario.

## 💡 Pistas
- Inicializa tu cliente Nerve en los eventos de "startup" (lifespan) de FastAPI.
- Puedes probar tus peticiones HTTP desde el "Docs" interactivo que FastAPI te genera gratis en `http://localhost:8000/docs`.

## 📦 Entregable
- El código dentro de la carpeta `retos/nivel-3-avanzado/08-puente-http/`.
- Un `README.md` corto explicando los comandos de inicio.

## 🙋 ¿Primera vez contribuyendo?
Lee nuestra guía [Cómo hacer tu primer PR](https://github.com/Kaia-Alenia/nerve-community/blob/main/COMO-HACER-TU-PRIMER-PR.md), ¡no hay preguntas tontas!

## 🎓 ¿Sabías que...?
Las soluciones más pulidas y completas de este reto pueden ser invitadas a integrarse directamente al repositorio de producción [zenith-nerve-tools](https://github.com/Kaia-Alenia/zenith-nerve-tools), con crédito total para ti como autor/a. ¡Esfuérzate, tu código puede terminar siendo una herramienta real que otros usen!

---

# Reto 09: probador-de-carga

**Título:** Reto 09: probador-de-carga

## 🎯 Objetivo
Lanzar N clientes simulados y medir la latencia o el *throughput* (mensajes por segundo) del Hub de Nerve.

## 📚 Qué vas a aprender
- Pruebas de rendimiento (load testing).
- Concurrencia y multithreading/multiprocessing en Python.
- Recolección de métricas.

## 🧩 Nivel
Avanzado

## 🛠️ Tecnologías sugeridas
- Python 3.10+
- `alenia-nerve`
- `threading` o `multiprocessing`

## 📋 Requisitos
- [ ] Un script debe spawnear (crear) múltiples hilos (threads) o procesos, cada uno simulando ser un cliente de Nerve.
- [ ] Deben mandar una "bomba" de cientos de mensajes a un canal específico en el menor tiempo posible.
- [ ] Al finalizar, se debe imprimir cuánto tardó en procesarse todo y calcular los "Mensajes por Segundo".

## 💡 Pistas
- Es probable que necesites un cliente que actúe como "Monitor" para contar cuántos mensajes llegan.
- Juega con el valor de `time.time()` al inicio y al final de la recepción para calcular la latencia.

## 📦 Entregable
- El código dentro de la carpeta `retos/nivel-3-avanzado/09-probador-de-carga/`.
- Un `README.md` mostrando los resultados de tu computadora (qué puntaje de mensajes/s lograste).

## 🙋 ¿Primera vez contribuyendo?
Lee nuestra guía [Cómo hacer tu primer PR](https://github.com/Kaia-Alenia/nerve-community/blob/main/COMO-HACER-TU-PRIMER-PR.md), ¡no hay preguntas tontas!

## 🎓 ¿Sabías que...?
Las soluciones más pulidas y completas de este reto pueden ser invitadas a integrarse directamente al repositorio de producción [zenith-nerve-tools](https://github.com/Kaia-Alenia/zenith-nerve-tools), con crédito total para ti como autor/a. ¡Esfuérzate, tu código puede terminar siendo una herramienta real que otros usen!

---

# Reto 10: cliente-nuevo-lenguaje

**Título:** Reto 10: cliente-nuevo-lenguaje

## 🎯 Objetivo
Portar un cliente súper básico de Nerve (solo capacidad de conectar, hacer handshake, y enviar/recibir) a un lenguaje en el que Nerve aún no tenga cliente oficial (ejemplo: Dart, Kotlin, PHP, C#).

## 📚 Qué vas a aprender
- Diseño e implementación de protocolos a bajo nivel.
- Uso crudo de Unix Domain Sockets o Sockets TCP en tu lenguaje favorito.
- Serialización/deserialización de estructuras JSON.

## 🧩 Nivel
Avanzado

## 🛠️ Tecnologías sugeridas
- El lenguaje de tu elección.
- Conocimiento sobre la especificación de protocolo de Nerve (JSON por línea y handshakes).

## 📋 Requisitos
- [ ] Debe poder leer la ruta de conexión a Nerve (socket path o puerto local).
- [ ] Debe enviar el JSON de saludo (handshake) `{"cmd": "hello", ...}`.
- [ ] Debe poder publicar al menos un mensaje sencillo.
- [ ] El código debe estar documentado para el lenguaje seleccionado.

## 💡 Pistas
- Usa un Hub de Nerve en Python corriendo en tu computadora, e intenta conectarte a él usando la clase Socket genérica de tu lenguaje.
- ¡Asegúrate de agregar `\n` al final de cada JSON que mandes por el socket!

## 📦 Entregable
- El código dentro de la carpeta `retos/nivel-3-avanzado/10-cliente-nuevo-lenguaje/` con el nombre de la subcarpeta que refleje tu lenguaje (ej. `solucion-dart`).
- Un `README.md` indicando cómo compilar o correr tu código.

## 🙋 ¿Primera vez contribuyendo?
Lee nuestra guía [Cómo hacer tu primer PR](https://github.com/Kaia-Alenia/nerve-community/blob/main/COMO-HACER-TU-PRIMER-PR.md), ¡no hay preguntas tontas!

## 🎓 ¿Sabías que...?
Las soluciones más pulidas y completas de este reto pueden ser invitadas a integrarse directamente al repositorio de producción [zenith-nerve-tools](https://github.com/Kaia-Alenia/zenith-nerve-tools), con crédito total para ti como autor/a. ¡Esfuérzate, tu código puede terminar siendo una herramienta real que otros usen!
