# 🛠️ Glosario: Conceptos de Software

Términos generales de desarrollo de software que aparecen en los retos, documentación y conversaciones del día a día en Nerve Community. Aquí nada se da por sabido.

---

## Tipos de Archivos y Formatos de Datos

| Término | 🔍 ¿Qué es? | 🎯 ¿Para qué sirve? | 💻 Ejemplo | ⚠️ Error común | 🔗 Relacionado |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Markdown (.md)** | Lenguaje de marcado simple | Formato de texto con una sintaxis sencilla (`**negrita**`, `# Título`) que se convierte en HTML. GitHub lo renderiza automáticamente. | Este mismo archivo que estás leyendo | N/A | - |
| **TXT** | Archivo de texto plano | El formato más básico. Sin formato, sin colores, solo caracteres. | `notas.txt`, `requirements.txt` | N/A | - |
| **YAML (.yml / .yaml)** | Yet Another Markup Language | Formato de configuración muy legible para humanos. Usado en archivos de CI/CD como GitHub Actions. | Los workflows en `.github/workflows/` | N/A | - |

---

## Arquitectura y Diseño de Software

| Término | 🔍 ¿Qué es? | 🎯 ¿Para qué sirve? | 💻 Ejemplo | ⚠️ Error común | 🔗 Relacionado |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **CLI (Command Line Interface)** | Interfaz de línea de comandos | Un programa que se usa desde la terminal escribiendo texto, en vez de clicando botones. La mayoría de los retos son CLIs. | `python3 lista_tareas.py --agregar "Estudiar"` | N/A | - |
| **Librería / Biblioteca** | Código reutilizable empaquetado | Colección de funciones y clases escritas por otros que puedes importar para no reinventar la rueda. | `import requests` | N/A | - |
| **Framework** | Estructura base para construir apps | Un esqueleto con reglas y herramientas que te dice cómo organizar tu proyecto. Más opinionado que una librería. | FastAPI (para APIs), discord.py (para bots) | N/A | - |
| **Módulo** | Unidad básica de código reutilizable | Un archivo `.py` con funciones que puedes importar en otros archivos de tu proyecto. | `from conversiones import celsius_a_fahrenheit` | N/A | - |
| **Dependencia** | Librería de la que depende tu código | Una librería externa que tu proyecto necesita para funcionar. Si no está instalada, el programa falla. | `requests` es una dependencia del reto 02 | N/A | - |
| **Open Source (Código Abierto)** | Software con código público y libre | Software cuyo código fuente es público, gratuito y puede ser modificado y redistribuido. Nerve y este repo son Open Source. | Licencia GNU GPL v3 | N/A | - |
| **GNU GPL v3** | Licencia de Nerve Community | Una licencia Open Source que garantiza que el software es libre, y que cualquier derivado también debe serlo. | El archivo `LICENSE.md` en el repo | N/A | - |
| **multiplataforma** | Funciona en varios sistemas operativos | Software que funciona en Linux, macOS y Windows sin cambios. Nerve es multiplataforma. | Nerve usa Unix Sockets en Linux/macOS y TCP en Windows | N/A | - |
| **offline-first** | Funciona sin internet | Diseñado para funcionar sin conexión a internet. Nerve se conecta localmente, no usa la nube. | Nerve solo necesita que los procesos estén en la misma máquina | N/A | - |

---

## Calidad, Bugs y Proceso de Desarrollo

| Término | 🔍 ¿Qué es? | 🎯 ¿Para qué sirve? | 💻 Ejemplo | ⚠️ Error común | 🔗 Relacionado |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Bug** | Error en el software | Fallo en el código que hace que el programa no funcione como se esperaba. | "El conversor de divisas dice que 1 USD = 0 MXN. Es un bug." | N/A | - |
| **Debugging** | Depuración — proceso de encontrar bugs | El arte de investigar y corregir errores en el código. Puede ser con herramientas o simplemente leyendo y pensando. | Usar `print()` para ver el valor de una variable | N/A | - |
| **Refactoring** | Mejorar código sin cambiar su comportamiento | Reescribir el código para que sea más limpio, legible o eficiente, sin que haga cosas diferentes. | Dividir una función gigante en varias funciones pequeñas | N/A | - |
| **Linter** | Analizador automático de estilo | Herramienta que revisa tu código buscando errores de formato, malas prácticas o inconsistencias de estilo. | `black` (Python), que usamos en el CI del repo | N/A | - |
| **CI/CD** | Integración y entrega continua | Automatizaciones que se ejecutan con cada PR: corren tests, verifican formato, despliegan código. | El Linter Compasivo que corre en cada PR de Nerve Community | N/A | - |
| **Test / Prueba** | Código que verifica que tu código funciona | Pequeños programas automáticos que comprueban si tus funciones devuelven los resultados esperados. | `assert suma(2, 3) == 5` | N/A | - |
| **edge case** | Caso borde o extremo | Una entrada o situación inusual que puede romper tu programa. Pensar en ellos es parte del desarrollo robusto. | ¿Qué pasa si el usuario escribe una letra donde va un número? | N/A | - |
| **hardcoded** | Valor fijo escrito directamente en el código | Un valor que no se puede cambiar sin editar el código fuente. Es mala práctica para configuraciones y rutas. | ❌ `ruta = "/home/user/Descargas"` | N/A | - |
| **dry-run** | Modo de simulación sin cambios reales | Ejecutar un script para que muestre qué haría, sin modificar nada. Fundamental en scripts que mueven archivos. | `python organizador.py --dry-run` | N/A | - |
| **logging** | Registro de eventos del programa | Guardar mensajes sobre lo que hace el programa mientras corre. Útil para diagnosticar problemas. | `logging.info("Archivo procesado: datos.csv")` | N/A | - |

---

## Conceptos de Seguridad

| Término | 🔍 ¿Qué es? | 🎯 ¿Para qué sirve? | 💻 Ejemplo | ⚠️ Error común | 🔗 Relacionado |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Criptografía** | Ciencia de proteger información | Técnicas para cifrar datos y hacer comunicaciones seguras. | HTTPS cifra los datos entre tu navegador y el servidor | N/A | - |
| **random vs secrets** | Diferencia crucial en Python | `random` genera números predecibles (no seguros para contraseñas). `secrets` genera números impredecibles, criptográficamente seguros. | ✓ `secrets.token_urlsafe(16)` para contraseñas reales | N/A | - |
| **Token de acceso** | Llave de autenticación | Una cadena de texto larga y aleatoria que actúa como contraseña para autenticar accesos a una API o servicio. | Token de GitHub para usar `gh auth login` | N/A | - |

---

## El Ecosistema Alenia / Nerve

| Término | 🔍 ¿Qué es? | 🎯 ¿Para qué sirve? | 💻 Ejemplo | ⚠️ Error común | 🔗 Relacionado |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Nerve** | Motor IPC de Alenia Studios | El sistema de comunicación entre procesos que es el tema central de este repo. Los retos de nivel Core giran en torno a él. | [alenia-nerve en GitHub](https://github.com/Kaia-Alenia/alenia-nerve) | N/A | - |
| **Zenith** | Framework principal de Alenia Studios | El framework de Alenia donde viven las herramientas más maduras. Las mejores soluciones de este repo pueden "graduarse" a Zenith. | `zenith-nerve-tools` | N/A | - |
| **nerve-community** | Este repositorio | El espacio de aprendizaje y contribución para construir herramientas y scripts usando Nerve, de forma abierta y colaborativa. | `https://github.com/Kaia-Alenia/nerve-community` | N/A | - |
| **Premio Trimestral** | Reconocimiento a la mejor contribución | La contribución más destacada del trimestre recibe 4 meses gratis de Google AI Pro. | Ver sección "Premio Trimestral" en el README | N/A | - |
| **TRANSPARENCIA.md** | Informe de uso de donaciones | Documento público donde se detalla cómo se usaron los fondos de donaciones de la comunidad. | [TRANSPARENCIA.md](../TRANSPARENCIA.md) | N/A | - |

---

> 💡 **Regla de oro del desarrollo:** Antes de instalar una librería o escribir código complejo, pregúntate: ¿ya existe algo en la librería estándar que haga esto? La mayoría de las veces, ¡la respuesta es sí!

---

← [Volver al Índice del Glosario](README.md)
