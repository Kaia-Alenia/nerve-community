# Issues de los Retos de Python General (Plantillas para GitHub)

A continuación tienes el texto para copiar y pegar y crear los 10 issues de los retos de Python General en GitHub. Recuerda asignarles las etiquetas correctas a cada uno (ej. `good-first-issue`, `python-general`, `disponible`).

---

# Python General 01 — Lista de tareas (to-do list) en terminal

**Título:** Python General 01 — Lista de tareas (to-do list) en terminal

## 🎯 Objetivo
Construye una lista de tareas manejable 100% desde terminal: agregar, marcar como completada, eliminar y ver tareas pendientes. Sin usar Nerve ni librerías externas de terceros.

## 📚 Qué vas a aprender
- Manejo de archivos (guardar/leer un archivo de texto o JSON).
- Estructuras de datos básicas (listas, diccionarios).
- Diseño de un menú interactivo con `input()`.

## 🧩 Nivel
Principiante.

## 🛠️ Tecnologías sugeridas
Solo Python 3.10+ y su librería estándar (`json` o manejo de archivos de texto plano).

## 📋 Requisitos
- [ ] Menú con opciones: agregar tarea, ver tareas, marcar como completada, eliminar tarea, salir.
- [ ] Las tareas deben persistir entre ejecuciones (guardadas en un archivo).
- [ ] Manejo de errores si el archivo no existe la primera vez que se corre.
- [ ] `README.md` explicando cómo correr el script.

## 💡 Pistas
- `json.dump` / `json.load` son suficientes, no necesitas una base de datos.
- Piensa en qué pasa si el usuario intenta marcar como completada una tarea que no existe.

## 📦 Entregable
PR con tu código en `retos/python-general/01-lista-de-tareas-cli/tu-usuario/`.

## 🙋 ¿Primera vez contribuyendo?
Lee nuestra guía [Cómo hacer tu primer PR](../blob/main/COMO-HACER-TU-PRIMER-PR.md).

---

# Python General 02 — Web scraper simple

**Título:** Python General 02 — Web scraper simple

## 🎯 Objetivo
Extrae información simple (títulos, precios, o encabezados) de una página web pública usando `requests` y `BeautifulSoup`, y guárdala en un archivo CSV.

## 📚 Qué vas a aprender
- Peticiones HTTP con `requests`.
- Parsing de HTML con `BeautifulSoup`.
- Manejo de errores de red (timeouts, páginas caídas).
- Exportar datos a CSV.

## 🧩 Nivel
Principiante.

## 🛠️ Tecnologías sugeridas
Python 3.10+, `requests`, `beautifulsoup4`.

## 📋 Requisitos
- [ ] Elige una página pública simple y permitida para scraping (ej. una página de ejemplo como `books.toscrape.com`, hecha específicamente para practicar).
- [ ] Extrae al menos 2 campos de datos (ej. título y precio) de varios elementos de la página.
- [ ] Guarda los resultados en un archivo `resultados.csv`.
- [ ] Manejo de errores si la página no responde o cambia su estructura.
- [ ] `README.md` explicando qué página se scrapeó y por qué es válida para practicar (evitar sitios que prohíban scraping en su `robots.txt`).

## 💡 Pistas
- `books.toscrape.com` y `quotes.toscrape.com` existen específicamente para que la gente practique scraping sin problemas éticos ni legales.
- Siempre revisa el archivo `robots.txt` del sitio antes de scrapear cualquier página real.

## 📦 Entregable
PR con tu código en `retos/python-general/02-web-scraper-simple/tu-usuario/`.

## 🙋 ¿Primera vez contribuyendo?
Lee nuestra guía [Cómo hacer tu primer PR](../blob/main/COMO-HACER-TU-PRIMER-PR.md).

---

# Python General 03 — Juego de adivina el número

**Título:** Python General 03 — Juego de adivina el número

## 🎯 Objetivo
El clásico juego donde la computadora piensa un número al azar y el usuario debe adivinarlo con pistas de "más alto" o "más bajo", contando sus intentos.

## 📚 Qué vas a aprender
- Loops y condicionales.
- El módulo `random`.
- Validación de entradas del usuario (que no meta letras donde va un número, por ejemplo).

## 🧩 Nivel
Principiante (ideal si nunca has programado nada interactivo).

## 🛠️ Tecnologías sugeridas
Solo Python 3.10+ y su librería estándar.

## 📋 Requisitos
- [ ] El rango de números debe ser configurable (ej. entre 1 y 100).
- [ ] Debe dar pistas ("más alto"/"más bajo") después de cada intento incorrecto.
- [ ] Debe contar y mostrar el número de intentos al finalizar.
- [ ] Manejo de errores si el usuario escribe algo que no es un número.
- [ ] `README.md` explicando cómo jugar.

## 💡 Pistas
- Usa un `try/except` para capturar cuando el usuario no escribe un número válido.
- Piensa en agregar un límite máximo de intentos como mejora opcional.

## 📦 Entregable
PR con tu código en `retos/python-general/03-juego-de-adivinanza/tu-usuario/`.

## 🙋 ¿Primera vez contribuyendo?
Lee nuestra guía [Cómo hacer tu primer PR](../blob/main/COMO-HACER-TU-PRIMER-PR.md).

---

# Python General 04 — Analizador de gastos personales (CSV)

**Título:** Python General 04 — Analizador de gastos personales (CSV)

## 🎯 Objetivo
Lee un archivo CSV con gastos personales (fecha, categoría, monto) y genera un resumen: total gastado, total por categoría, promedio, y el gasto más alto.

## 📚 Qué vas a aprender
- El módulo `csv` de la librería estándar.
- Agregación de datos (sumas, promedios, máximos).
- Formateo de reportes legibles en terminal.

## 🧩 Nivel
Principiante.

## 🛠️ Tecnologías sugeridas
Solo Python 3.10+ y su librería estándar (`csv`).

## 📋 Requisitos
- [ ] Incluye un archivo CSV de ejemplo con al menos 15 gastos ficticios (fecha, categoría, monto).
- [ ] El script debe calcular: total general, total por categoría, promedio de gasto, y el gasto individual más alto (con su categoría y fecha).
- [ ] El reporte debe imprimirse ordenado y legible en terminal.
- [ ] Manejo de errores si el CSV tiene filas mal formadas o vacías.
- [ ] `README.md` explicando el formato esperado del CSV.

## 💡 Pistas
- `csv.DictReader` facilita mucho leer filas con nombres de columna.
- Considera qué pasa si un monto viene con "$" o comas como separador de miles.

## 📦 Entregable
PR con tu código en `retos/python-general/04-analizador-de-gastos-csv/tu-usuario/`.

## 🙋 ¿Primera vez contribuyendo?
Lee nuestra guía [Cómo hacer tu primer PR](../blob/main/COMO-HACER-TU-PRIMER-PR.md).

---

# Python General 05 — Generador de contraseñas seguras

**Título:** Python General 05 — Generador de contraseñas seguras

## 🎯 Objetivo
Genera contraseñas seguras y configurables: longitud, si incluye símbolos, mayúsculas, números, etc.

## 📚 Qué vas a aprender
- Los módulos `random` y `secrets` (y por qué `secrets` es mejor para seguridad).
- Validación de parámetros de entrada.
- Diseño de una herramienta configurable por línea de comandos.

## 🧩 Nivel
Principiante.

## 🛠️ Tecnologías sugeridas
Solo Python 3.10+ y su librería estándar (`secrets`, `string`, opcionalmente `argparse`).

## 📋 Requisitos
- [ ] Debe permitir elegir la longitud de la contraseña.
- [ ] Debe permitir activar/desactivar: símbolos, números, mayúsculas.
- [ ] Debe garantizar que, si se piden ciertos tipos de caracteres, la contraseña generada realmente los incluya al menos una vez.
- [ ] Manejo de errores si se piden parámetros imposibles (ej. longitud 0, o ningún tipo de carácter activado).
- [ ] `README.md` explicando las opciones disponibles y por qué se usa `secrets` en vez de `random` para esto.

## 💡 Pistas
- `random` NO es seguro para contraseñas reales porque es predecible; `secrets` sí lo es. Investiga la diferencia y explícala en tu README.
- Puedes usar `argparse` para que el script se use así: `python generador.py --longitud 16 --simbolos`.

## 📦 Entregable
PR con tu código en `retos/python-general/05-generador-de-contrasenas/tu-usuario/`.

## 🙋 ¿Primera vez contribuyendo?
Lee nuestra guía [Cómo hacer tu primer PR](../blob/main/COMO-HACER-TU-PRIMER-PR.md).

---

# Python General 06 — Conversor de unidades

**Título:** Python General 06 — Conversor de unidades

## 🎯 Objetivo
Un conversor de unidades desde un menú de terminal: temperatura (Celsius/Fahrenheit/Kelvin), distancia (km/millas/metros), y peso (kg/libras).

## 📚 Qué vas a aprender
- Diseño de funciones puras (una función = una conversión, sin efectos secundarios).
- Validación de entradas numéricas.
- Diseño de menús interactivos con submenús.

## 🧩 Nivel
Principiante.

## 🛠️ Tecnologías sugeridas
Solo Python 3.10+ y su librería estándar.

## 📋 Requisitos
- [ ] Al menos 3 categorías de conversión (temperatura, distancia, peso), cada una con al menos 2 unidades distintas.
- [ ] Cada conversión debe ser una función separada y reutilizable (no todo mezclado en un solo bloque de código).
- [ ] Manejo de errores si el usuario mete un valor no numérico.
- [ ] `README.md` con ejemplos de uso.

## 💡 Pistas
- Organiza tus funciones de conversión en un archivo separado (ej. `conversiones.py`) y el menú en otro (ej. `main.py`), para practicar cómo dividir un proyecto en módulos.

## 📦 Entregable
PR con tu código en `retos/python-general/06-conversor-de-unidades/tu-usuario/`.

## 🙋 ¿Primera vez contribuyendo?
Lee nuestra guía [Cómo hacer tu primer PR](../blob/main/COMO-HACER-TU-PRIMER-PR.md).

---

# Python General 07 — Calculadora de IMC

**Título:** Python General 07 — Calculadora de IMC

## 🎯 Objetivo
Calcula el Índice de Masa Corporal (IMC) a partir de peso y estatura, mostrando la categoría correspondiente (bajo peso, normal, sobrepeso, etc.) con mensajes claros.

## 📚 Qué vas a aprender
- Funciones con múltiples parámetros.
- Validación de datos numéricos (que el peso/estatura sean positivos y razonables).
- Formateo de salida clara para el usuario.

## 🧩 Nivel
Principiante.

## 🛠️ Tecnologías sugeridas
Solo Python 3.10+ y su librería estándar.

## 📋 Requisitos
- [ ] Debe pedir peso (kg) y estatura (metros), calcular el IMC, y mostrar la categoría según los rangos estándar.
- [ ] Manejo de errores si los valores son negativos, cero, o no numéricos.
- [ ] **Importante:** el mensaje de resultado debe ser informativo, no alarmista ni prescriptivo — evita frases como "debes bajar de peso"; usa un tono neutral tipo "tu IMC es X, lo cual se categoriza como Y según la OMS".
- [ ] `README.md` explicando la fórmula usada y aclarando que esto es una herramienta educativa, no un diagnóstico médico.

## 💡 Pistas
- La fórmula es: `IMC = peso (kg) / estatura (m) ** 2`.
- Este es un buen ejercicio para practicar cómo comunicar resultados de forma responsable cuando el tema toca la salud de alguien.

## 📦 Entregable
PR con tu código en `retos/python-general/07-calculadora-de-imc/tu-usuario/`.

## 🙋 ¿Primera vez contribuyendo?
Lee nuestra guía [Cómo hacer tu primer PR](../blob/main/COMO-HACER-TU-PRIMER-PR.md).

---

# Python General 08 — Organizador automático de archivos

**Título:** Python General 08 — Organizador automático de archivos

## 🎯 Objetivo
Un script que ordena automáticamente los archivos de una carpeta (por ejemplo, tu carpeta de Descargas) en subcarpetas según su tipo: imágenes, documentos, videos, comprimidos, etc.

## 📚 Qué vas a aprender
- Los módulos `os` y `shutil` para manejar archivos y carpetas.
- Manejo seguro de rutas de archivos (evitando sobrescribir accidentalmente algo importante).
- Buenas prácticas al automatizar algo que toca archivos reales del usuario.

## 🧩 Nivel
Principiante-intermedio.

## 🛠️ Tecnologías sugeridas
Solo Python 3.10+ y su librería estándar (`os`, `shutil`, `pathlib`).

## 📋 Requisitos
- [ ] El script debe recibir una ruta de carpeta como argumento (nunca hardcodeada).
- [ ] Debe clasificar archivos en subcarpetas según su extensión (ej. `.jpg/.png` → `Imagenes/`, `.pdf/.docx` → `Documentos/`, etc.).
- [ ] **Importante:** debe incluir un modo "simulación" (`--dry-run`) que muestre qué haría SIN mover ningún archivo todavía, para que el usuario pueda revisar antes de ejecutar de verdad.
- [ ] Manejo de errores si la carpeta no existe o si un archivo ya existe en el destino (no debe sobrescribir sin avisar).
- [ ] `README.md` con una advertencia clara de que se recomienda probar primero con `--dry-run` en una carpeta de prueba antes de usarlo en carpetas reales.

## 💡 Pistas
- `pathlib.Path` es más moderno y legible que `os.path` para este tipo de tareas.
- Piensa en un diccionario que mapee extensiones a nombres de carpeta, para que sea fácil agregar más tipos de archivo después.

## 📦 Entregable
PR con tu código en `retos/python-general/08-organizador-de-archivos/tu-usuario/`.

## 🙋 ¿Primera vez contribuyendo?
Lee nuestra guía [Cómo hacer tu primer PR](../blob/main/COMO-HACER-TU-PRIMER-PR.md).

---

# Python General 09 — Recordatorios en terminal

**Título:** Python General 09 — Recordatorios en terminal

## 🎯 Objetivo
Un script que permite guardar recordatorios con fecha/hora, y que avisa en terminal cuando llega el momento (mientras el script sigue corriendo).

## 📚 Qué vas a aprender
- El módulo `datetime` para manejar fechas y horas.
- Loops con espera (`time.sleep`) sin saturar el CPU.
- Persistencia simple de datos en un archivo.

## 🧩 Nivel
Intermedio.

## 🛠️ Tecnologías sugeridas
Solo Python 3.10+ y su librería estándar (`datetime`, `json`, `time`).

## 📋 Requisitos
- [ ] Permite agregar un recordatorio con texto + fecha/hora exacta.
- [ ] El script, mientras corre, debe revisar periódicamente si algún recordatorio ya se cumplió y avisar en pantalla (con sonido de terminal opcional, `\a`).
- [ ] Los recordatorios deben persistir en un archivo, para no perderlos si se cierra el script.
- [ ] Manejo de errores si el usuario mete una fecha/hora inválida o ya pasada.
- [ ] `README.md` explicando el formato de fecha esperado y cómo correr el script en segundo plano si se desea.

## 💡 Pistas
- No revises cada milisegundo; con revisar cada 10-30 segundos es suficiente y no satura el CPU.
- Piensa en qué pasa con recordatorios que ya pasaron su fecha antes de que el script se vuelva a abrir.

## 📦 Entregable
PR con tu código en `retos/python-general/09-recordatorios-en-terminal/tu-usuario/`.

## 🙋 ¿Primera vez contribuyendo?
Lee nuestra guía [Cómo hacer tu primer PR](../blob/main/COMO-HACER-TU-PRIMER-PR.md).

---

# Python General 10 — Analizador de texto

**Título:** Python General 10 — Analizador de texto

## 🎯 Objetivo
Recibe un archivo de texto (ej. un `.txt`) y genera estadísticas: palabras más frecuentes, número de líneas, número de palabras, y promedio de palabras por línea.

## 📚 Qué vas a aprender
- Manejo de strings (limpieza, división, conteo).
- Diccionarios para contar frecuencias.
- Ordenar resultados (ej. top 10 palabras más usadas).

## 🧩 Nivel
Principiante.

## 🛠️ Tecnologías sugeridas
Solo Python 3.10+ y su librería estándar (opcionalmente `collections.Counter`).

## 📋 Requisitos
- [ ] Debe recibir la ruta de un archivo `.txt` como argumento.
- [ ] Debe reportar: total de líneas, total de palabras, promedio de palabras por línea, y las 10 palabras más frecuentes (ignorando mayúsculas/minúsculas y signos de puntuación).
- [ ] Debe ignorar palabras "vacías" comunes en español si se quiere un análisis más útil (ej. "el", "la", "de", "que") — esto puede ser una lista simple hardcodeada.
- [ ] Manejo de errores si el archivo no existe o está vacío.
- [ ] `README.md` con un ejemplo de archivo de prueba y su resultado esperado.

## 💡 Pistas
- `collections.Counter` hace el conteo de frecuencias en una sola línea.
- Usa expresiones regulares (`re`) o `str.strip(string.punctuation)` para limpiar signos de puntuación antes de contar.

## 📦 Entregable
PR con tu código en `retos/python-general/10-analizador-de-texto/tu-usuario/`.

## 🙋 ¿Primera vez contribuyendo?
Lee nuestra guía [Cómo hacer tu primer PR](../blob/main/COMO-HACER-TU-PRIMER-PR.md).
