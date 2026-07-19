# 🛠️ Glosario: Conceptos de Software

Términos generales de desarrollo de software que aparecen en los retos, documentación y conversaciones del día a día en Nerve Community. Aquí nada se da por sabido.

---

## Tipos de Archivos y Formatos de Datos

| Término | 🔍 ¿Qué es? | 🎯 ¿Para qué sirve? | 💻 Ejemplo |
| :--- | :--- | :--- | :--- |
| **JSON** | JavaScript Object Notation | El formato de texto más popular para guardar y transferir datos estructurados. Parece un diccionario de Python. | `{"nombre": "Ana", "edad": 28, "activa": true}` |
| **CSV** | Comma-Separated Values | Archivo de texto donde los datos están separados por comas. Funciona como una hoja de cálculo simple. Abre con Excel o Python. | `fecha,categoría,monto` / `2024-01-15,Comida,150.00` |
| **Markdown (.md)** | Lenguaje de marcado simple | Formato de texto con una sintaxis sencilla (`**negrita**`, `# Título`) que se convierte en HTML. GitHub lo renderiza automáticamente. | Este mismo archivo que estás leyendo |
| **TXT** | Archivo de texto plano | El formato más básico. Sin formato, sin colores, solo caracteres. | `notas.txt`, `requirements.txt` |
| **YAML (.yml / .yaml)** | Yet Another Markup Language | Formato de configuración muy legible para humanos. Usado en archivos de CI/CD como GitHub Actions. | Los workflows en `.github/workflows/` |
| **archivo .gitignore** | Lista de exclusiones de Git | Le dice a Git qué archivos o carpetas no debe rastrear. Protege claves y archivos temporales. | `*.pyc`, `.env`, `node_modules/` |
| **requirements.txt** | Lista de dependencias de Python | Un archivo de texto que lista las librerías externas que necesita un proyecto Python, con sus versiones. | `requests==2.31.0` / `beautifulsoup4==4.12.0` |
| **README.md** | Archivo de presentación | El primer archivo que ve alguien al entrar a un repositorio o carpeta de reto. Explica qué es y cómo usarlo. | Cada solución de reto debe incluir uno |
| **robots.txt** | Reglas de scraping de un sitio web | Archivo que le dice a los bots qué páginas pueden o no pueden visitar. Siempre revísalo antes de hacer web scraping. | `https://ejemplo.com/robots.txt` |

---

## Arquitectura y Diseño de Software

| Término | 🔍 ¿Qué es? | 🎯 ¿Para qué sirve? | 💻 Ejemplo |
| :--- | :--- | :--- | :--- |
| **CLI (Command Line Interface)** | Interfaz de línea de comandos | Un programa que se usa desde la terminal escribiendo texto, en vez de clicando botones. La mayoría de los retos son CLIs. | `python3 lista_tareas.py --agregar "Estudiar"` |
| **API (Application Programming Interface)** | Interfaz de programación | Un conjunto de reglas que permite que dos programas se comuniquen. Es el "menú" de funciones que un servicio ofrece. | La API de Discord que usa el bot del reto 07 |
| **Librería / Biblioteca** | Código reutilizable empaquetado | Colección de funciones y clases escritas por otros que puedes importar para no reinventar la rueda. | `import requests` |
| **Framework** | Estructura base para construir apps | Un esqueleto con reglas y herramientas que te dice cómo organizar tu proyecto. Más opinionado que una librería. | FastAPI (para APIs), discord.py (para bots) |
| **Módulo** | Unidad básica de código reutilizable | Un archivo `.py` con funciones que puedes importar en otros archivos de tu proyecto. | `from conversiones import celsius_a_fahrenheit` |
| **Dependencia** | Librería de la que depende tu código | Una librería externa que tu proyecto necesita para funcionar. Si no está instalada, el programa falla. | `requests` es una dependencia del reto 02 |
| **Open Source (Código Abierto)** | Software con código público y libre | Software cuyo código fuente es público, gratuito y puede ser modificado y redistribuido. Nerve y este repo son Open Source. | Licencia GNU GPL v3 |
| **GNU GPL v3** | Licencia de Nerve Community | Una licencia Open Source que garantiza que el software es libre, y que cualquier derivado también debe serlo. | El archivo `LICENSE.md` en el repo |
| **IPC (Inter-Process Communication)** | Comunicación entre procesos | Mecanismo para que dos programas en ejecución se manden mensajes. Es el concepto central de Nerve. | Nerve usando Unix Sockets en Linux |
| **multiplataforma** | Funciona en varios sistemas operativos | Software que funciona en Linux, macOS y Windows sin cambios. Nerve es multiplataforma. | Nerve usa Unix Sockets en Linux/macOS y TCP en Windows |
| **offline-first** | Funciona sin internet | Diseñado para funcionar sin conexión a internet. Nerve se conecta localmente, no usa la nube. | Nerve solo necesita que los procesos estén en la misma máquina |

---

## Calidad, Bugs y Proceso de Desarrollo

| Término | 🔍 ¿Qué es? | 🎯 ¿Para qué sirve? | 💻 Ejemplo |
| :--- | :--- | :--- | :--- |
| **Bug** | Error en el software | Fallo en el código que hace que el programa no funcione como se esperaba. | "El conversor de divisas dice que 1 USD = 0 MXN. Es un bug." |
| **Debugging** | Depuración — proceso de encontrar bugs | El arte de investigar y corregir errores en el código. Puede ser con herramientas o simplemente leyendo y pensando. | Usar `print()` para ver el valor de una variable |
| **Refactoring** | Mejorar código sin cambiar su comportamiento | Reescribir el código para que sea más limpio, legible o eficiente, sin que haga cosas diferentes. | Dividir una función gigante en varias funciones pequeñas |
| **Linter** | Analizador automático de estilo | Herramienta que revisa tu código buscando errores de formato, malas prácticas o inconsistencias de estilo. | `black` (Python), que usamos en el CI del repo |
| **CI/CD** | Integración y entrega continua | Automatizaciones que se ejecutan con cada PR: corren tests, verifican formato, despliegan código. | El Linter Compasivo que corre en cada PR de Nerve Community |
| **Test / Prueba** | Código que verifica que tu código funciona | Pequeños programas automáticos que comprueban si tus funciones devuelven los resultados esperados. | `assert suma(2, 3) == 5` |
| **edge case** | Caso borde o extremo | Una entrada o situación inusual que puede romper tu programa. Pensar en ellos es parte del desarrollo robusto. | ¿Qué pasa si el usuario escribe una letra donde va un número? |
| **hardcoded** | Valor fijo escrito directamente en el código | Un valor que no se puede cambiar sin editar el código fuente. Es mala práctica para configuraciones y rutas. | ❌ `ruta = "/home/user/Descargas"` |
| **dry-run** | Modo de simulación sin cambios reales | Ejecutar un script para que muestre qué haría, sin modificar nada. Fundamental en scripts que mueven archivos. | `python organizador.py --dry-run` |
| **logging** | Registro de eventos del programa | Guardar mensajes sobre lo que hace el programa mientras corre. Útil para diagnosticar problemas. | `logging.info("Archivo procesado: datos.csv")` |

---

## Conceptos de Seguridad

| Término | 🔍 ¿Qué es? | 🎯 ¿Para qué sirve? | 💻 Ejemplo |
| :--- | :--- | :--- | :--- |
| **Criptografía** | Ciencia de proteger información | Técnicas para cifrar datos y hacer comunicaciones seguras. | HTTPS cifra los datos entre tu navegador y el servidor |
| **random vs secrets** | Diferencia crucial en Python | `random` genera números predecibles (no seguros para contraseñas). `secrets` genera números impredecibles, criptográficamente seguros. | ✓ `secrets.token_urlsafe(16)` para contraseñas reales |
| **Token de acceso** | Llave de autenticación | Una cadena de texto larga y aleatoria que actúa como contraseña para autenticar accesos a una API o servicio. | Token de GitHub para usar `gh auth login` |
| **.env** | Archivo de secrets local | Archivo que guarda claves y contraseñas localmente. **NUNCA** debe subirse a GitHub (en `.gitignore`). | `DISCORD_TOKEN=mi_token_secreto` |
| **robots.txt** | Política de scraping del sitio | Indica qué partes de un sitio web no deberían ser rastreadas por bots. Respetarlo es ética y, en algunos países, ley. | Revisa `https://sitio.com/robots.txt` antes de scrapear |

---

## El Ecosistema Alenia / Nerve

| Término | 🔍 ¿Qué es? | 🎯 ¿Para qué sirve? | 💻 Ejemplo |
| :--- | :--- | :--- | :--- |
| **Nerve** | Motor IPC de Alenia Studios | El sistema de comunicación entre procesos que es el tema central de este repo. Los retos de nivel Core giran en torno a él. | [alenia-nerve en GitHub](https://github.com/Kaia-Alenia/alenia-nerve) |
| **Zenith** | Framework principal de Alenia Studios | El framework de Alenia donde viven las herramientas más maduras. Las mejores soluciones de este repo pueden "graduarse" a Zenith. | `zenith-nerve-tools` |
| **nerve-community** | Este repositorio | El espacio de aprendizaje y contribución para construir herramientas y scripts usando Nerve, de forma abierta y colaborativa. | `https://github.com/Kaia-Alenia/nerve-community` |
| **Premio Trimestral** | Reconocimiento a la mejor contribución | La contribución más destacada del trimestre recibe 4 meses gratis de Google AI Pro. | Ver sección "Premio Trimestral" en el README |
| **TRANSPARENCIA.md** | Informe de uso de donaciones | Documento público donde se detalla cómo se usaron los fondos de donaciones de la comunidad. | [TRANSPARENCIA.md](../TRANSPARENCIA.md) |

---

> 💡 **Regla de oro del desarrollo:** Antes de instalar una librería o escribir código complejo, pregúntate: ¿ya existe algo en la librería estándar que haga esto? La mayoría de las veces, ¡la respuesta es sí!

---

← [Volver al Índice del Glosario](README.md)
