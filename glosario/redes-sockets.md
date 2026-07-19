# 🌐 Glosario: Redes y Sockets (Nerve)

Estos son los conceptos de redes y comunicación que usa **Nerve** para conectar scripts entre sí. No te asustes, se explican desde cero.

---

## Conceptos Fundamentales de Redes

| Término | 🔍 ¿Qué es? | 🎯 ¿Para qué sirve? | 💻 Ejemplo |
| :--- | :--- | :--- | :--- |
| **Red (Network)** | Sistema de conexión entre computadoras | Permite que diferentes programas o máquinas se comuniquen e intercambien datos. Internet es una red de redes. | Tu WiFi conecta tu celular con el router |
| **Protocolo** | Reglas de comunicación acordadas | Un "idioma en común" que dos partes usan para entenderse. Como las reglas del correo postal. | TCP, UDP, HTTP, WebSocket |
| **Puerto (Port)** | Número de "puerta" de un servicio | Un número (0–65535) que identifica un servicio específico dentro de una computadora. Es como el número de apartamento dentro de un edificio. | Puerto 80 → HTTP, Puerto 443 → HTTPS, Puerto 8080 → Servidor de desarrollo |
| **IP (Dirección IP)** | Identificador de una computadora en la red | Un número único que identifica cada dispositivo en una red. Como la dirección de un edificio. | `127.0.0.1` = tu propia computadora (localhost) |
| **localhost / 127.0.0.1** | Tu propia máquina | Cuando un programa se conecta a "localhost", se conecta a sí mismo. Usado para probar servidores sin internet. | `http://localhost:8080` |
| **TCP (Transmission Control Protocol)** | Protocolo de comunicación confiable | Garantiza que los datos lleguen completos y en orden. Si se pierde algo, lo reenvía. Más lento pero seguro. Nerve lo usa en Windows. | Transferencias de archivos, navegación web |
| **UDP** | Protocolo rápido sin garantías | Envía datos sin verificar que lleguen. Más rápido que TCP pero puede perder paquetes. Ideal para videollamadas o juegos. | Streaming de video, juegos online |

---

## Sockets y IPC (Lo que hace Nerve)

| Término | 🔍 ¿Qué es? | 🎯 ¿Para qué sirve? | 💻 Ejemplo |
| :--- | :--- | :--- | :--- |
| **Socket** | Punto de conexión entre procesos | Es como un "enchufe" que dos programas usan para mandarse mensajes. Un socket tiene dos lados: quien envía y quien recibe. | `import socket` en Python |
| **IPC (Inter-Process Communication)** | Comunicación entre procesos | Forma en que dos programas corriendo al mismo tiempo (procesos) se mandan mensajes entre sí. Es el concepto central de Nerve. | Un script Python le habla a un script Go a través de Nerve |
| **Unix Socket** | Socket de archivo en Linux/macOS | Un tipo especial de socket que usa un archivo en el sistema (en vez de TCP) para comunicación local. Más rápido que TCP en Linux/macOS. Nerve los usa en Linux/macOS. | `/tmp/nerve.sock` |
| **Socket TCP** | Socket de red usando TCP | Socket que usa el protocolo TCP y una dirección IP + puerto para comunicarse. Funciona también entre diferentes computadoras. Nerve los usa en Windows. | `socket.connect(("127.0.0.1", 7878))` |
| **Servidor (Server)** | El que escucha y responde | En una arquitectura cliente-servidor, el servidor está siempre corriendo y espera que los clientes se conecten. | El proceso de Nerve que escucha conexiones |
| **Cliente (Client)** | El que inicia la conexión | Se conecta al servidor para enviarle datos o pedirle algo. | Tu script Python que se conecta a Nerve |
| **bind()** | Asignar dirección al socket del servidor | El servidor "ata" su socket a una dirección y puerto específicos para que los clientes sepan dónde conectarse. | `server.bind(("127.0.0.1", 7878))` |
| **listen()** | Poner el socket a escuchar | El servidor entra en modo de espera, listo para aceptar conexiones entrantes. | `server.listen(5)` (acepta hasta 5 en cola) |
| **accept()** | Aceptar una conexión entrante | El servidor acepta la conexión de un cliente que llamó a la puerta. Devuelve un nuevo socket para hablar con ese cliente específico. | `conn, addr = server.accept()` |
| **connect()** | Conectarse al servidor (desde el cliente) | El cliente llama a la puerta del servidor. | `client.connect(("127.0.0.1", 7878))` |
| **send() / recv()** | Enviar y recibir datos | Las funciones básicas para mandarse bytes a través del socket. | `socket.send(b"Hola!")` / `data = socket.recv(1024)` |

---

## Conceptos de HTTP y APIs

| Término | 🔍 ¿Qué es? | 🎯 ¿Para qué sirve? | 💻 Ejemplo |
| :--- | :--- | :--- | :--- |
| **HTTP** | Protocolo de la Web | El protocolo que usan los navegadores para pedir páginas web. "La lengua de internet". | `http://` al inicio de una URL |
| **HTTPS** | HTTP Seguro (con cifrado) | Versión cifrada de HTTP. Tus datos viajan encriptados. GitHub y casi todos los sitios modernos lo usan. | `https://github.com` |
| **API (Application Programming Interface)** | Interfaz para comunicar programas | Un conjunto de reglas para que dos programas se hablen. Una API web te permite pedirle datos a un servicio sin necesidad de una interfaz visual. | API de OpenWeatherMap para obtener el clima (reto 14) |
| **REST API** | Tipo de API que usa HTTP | El estilo más común de APIs web. Usa URLs y métodos HTTP (GET, POST, etc.) para hacer operaciones. | `requests.get("https://api.ejemplo.com/datos")` |
| **GET** | Solicitar/leer datos | El método HTTP para pedir información a un servidor sin modificar nada. | `requests.get("https://api.clima.com/ciudad/monterrey")` |
| **POST** | Enviar datos al servidor | El método HTTP para enviar datos nuevos al servidor (crear algo). | `requests.post(url, json={"nombre": "Ana"})` |
| **JSON (JavaScript Object Notation)** | Formato de intercambio de datos | El formato más común para enviar y recibir datos en APIs. Parece un diccionario de Python. | `{"temperatura": 28, "ciudad": "Monterrey"}` |
| **FastAPI** | Framework web para Python | Librería para crear APIs REST de forma rápida en Python. Usada en el reto 08-nerve (Puente HTTP). | `pip install fastapi` |
| **WebSocket** | Conexión bidireccional persistente | A diferencia de HTTP (donde tú preguntas y el servidor responde), un WebSocket mantiene la conexión abierta para que ambos puedan hablar cuando quieran. | Chat en tiempo real |
| **Endpoint** | Dirección de un recurso en una API | La URL específica de un recurso dentro de una API. Cada endpoint sirve para una operación distinta. | `GET /api/clima` o `POST /api/usuarios` |
| **timeout** | Límite de tiempo de espera | El tiempo máximo que tu programa esperará una respuesta de la red antes de rendirse y reportar error. | `requests.get(url, timeout=5)` → espera máx. 5 segundos |

---

## Conceptos de Concurrencia (Reto 09)

| Término | 🔍 ¿Qué es? | 🎯 ¿Para qué sirve? | 💻 Ejemplo |
| :--- | :--- | :--- | :--- |
| **Proceso** | Programa en ejecución | Una instancia de tu programa corriendo. Tiene su propia memoria independiente. | Tu script de Python = un proceso |
| **Hilo (Thread)** | Unidad de ejecución dentro de un proceso | Un proceso puede tener varios hilos corriendo "en paralelo" (o casi). Comparten memoria. | `import threading` en Python |
| **Concurrencia** | Manejar varias tareas a la vez | La capacidad de un programa de avanzar en varias tareas al mismo tiempo, aunque no sea literalmente simultáneo. | El servidor Nerve atendiendo a 10 clientes a la vez |
| **Carga (Load)** | Nivel de trabajo de un servidor | Cuántas peticiones está manejando un servidor en un momento dado. El reto 09 prueba cuánta carga puede soportar Nerve. | 1000 peticiones por segundo = alta carga |

---

> 💡 **Dato clave sobre Nerve:** Nerve abstrae toda esta complejidad. Tú no tienes que saber de sockets para usar Nerve, pero saber cómo funcionan te ayuda a entender *por qué* Nerve existe y qué problema resuelve. Los retos de nivel Avanzado (08, 09, 10) sí requieren entender estos conceptos. 🚀

---

← [Volver al Índice del Glosario](README.md)
