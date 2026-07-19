# 🐍 Glosario: Python

Todo lo que necesitas saber sobre Python para resolver los retos de Nerve Community, desde los conceptos más básicos hasta las librerías que usamos en los retos.

---

## El Lenguaje: Conceptos Base

| Término | 🔍 ¿Qué es? | 🎯 ¿Para qué sirve? | 💻 Ejemplo |
| :--- | :--- | :--- | :--- |
| **Python** | Lenguaje de programación | Un lenguaje de alto nivel, fácil de leer y muy popular. Es el lenguaje principal de casi todos los retos de Nerve Community. | `python3 mi_script.py` |
| **Python 3.10+** | Versión mínima requerida | Los retos exigen Python 3.10 o superior porque usan funciones modernas del lenguaje. Evita Python 2 (está muerto). | `python3 --version` |
| **Script** | Archivo de código ejecutable | Un archivo `.py` con instrucciones que Python ejecuta de arriba a abajo. Es la unidad básica de trabajo. | `calculadora.py`, `main.py` |
| **Librería estándar** | Módulos que vienen con Python | El conjunto de módulos incluidos con Python sin instalar nada extra. Son tu caja de herramientas básica. | `os`, `json`, `csv`, `random`, `datetime`, `pathlib` |
| **Módulo** | Archivo de Python importable | Un archivo `.py` o paquete que contiene funciones y clases que puedes reutilizar en otros scripts. | `import math` → usas `math.sqrt(16)` |
| **Paquete / Librería externa** | Módulo creado por la comunidad | Código que alguien más escribió y publicó. Se instala con `pip`. No vienen con Python por defecto. | `requests`, `beautifulsoup4`, `rich`, `Pillow` |
| **pip** | Gestor de paquetes de Python | La herramienta para instalar librerías externas desde el repositorio PyPI. Es como una tienda de apps para Python. | `pip install requests` |
| **PyPI** | Python Package Index | La "tienda oficial" de paquetes de Python. Pip descarga de aquí. Tiene más de 500,000 librerías. | `https://pypi.org/` |
| **Entorno virtual (venv)** | Espacio aislado para dependencias | Te permite instalar librerías para un solo proyecto sin que afecten a otros. Buena práctica para proyectos serios. | `python3 -m venv .venv` y luego `source .venv/bin/activate` |

---

## Sintaxis Fundamental

| Término | 🔍 ¿Qué es? | 🎯 ¿Para qué sirve? | 💻 Ejemplo |
| :--- | :--- | :--- | :--- |
| **print()** | Función para mostrar texto | Imprime valores en la terminal. La función más básica de Python. | `print("Hola, mundo")` |
| **input()** | Función para recibir datos del usuario | Detiene el programa y espera a que el usuario escriba algo. Devuelve siempre un texto (string). | `nombre = input("¿Cómo te llamas? ")` |
| **Variable** | Contenedor para guardar datos | Un nombre que apunta a un valor en memoria. En Python no se declara el tipo, se asigna directamente. | `edad = 25`, `nombre = "Carlos"` |
| **String (str)** | Cadena de texto | El tipo de dato para texto. Se escribe entre comillas simples o dobles. | `saludo = "Hola"` |
| **Integer (int)** | Número entero | El tipo de dato para números sin decimales. | `numero = 42` |
| **Float** | Número decimal | El tipo de dato para números con punto decimal. | `precio = 19.99` |
| **Boolean (bool)** | Verdadero o Falso | Solo puede ser `True` o `False`. Usado en condiciones. | `esta_activo = True` |
| **List (lista)** | Colección ordenada y modificable | Guarda varios valores en orden. Se puede agregar, quitar o cambiar elementos. | `tareas = ["comprar", "estudiar", "dormir"]` |
| **Dictionary (dict)** | Colección clave-valor | Guarda pares de "nombre: valor". Perfecto para estructurar datos. | `usuario = {"nombre": "Ana", "edad": 28}` |
| **Tuple** | Colección ordenada inmutable | Como una lista, pero no se puede modificar después de creada. | `colores = ("rojo", "verde", "azul")` |
| **None** | La ausencia de valor | El equivalente de Python a "vacío" o "nada". | `resultado = None` |

---

## Control de Flujo

| Término | 🔍 ¿Qué es? | 🎯 ¿Para qué sirve? | 💻 Ejemplo |
| :--- | :--- | :--- | :--- |
| **if / elif / else** | Condicional | Ejecuta código diferente según si una condición es verdadera o falsa. | `if x > 5: print("mayor")` |
| **for** | Bucle para iterar | Recorre cada elemento de una lista, rango u otro iterable. | `for tarea in tareas: print(tarea)` |
| **while** | Bucle con condición | Repite un bloque de código mientras una condición sea verdadera. | `while intentos < 3: ...` |
| **break** | Salir del bucle | Interrumpe un bucle `for` o `while` inmediatamente. | `if x == 0: break` |
| **continue** | Saltar al siguiente ciclo | Salta la iteración actual del bucle y pasa a la siguiente sin salir del bucle. | `if linea == "": continue` |
| **range()** | Generador de secuencias de números | Crea un rango de números para usar en un `for`. | `for i in range(10):` → del 0 al 9 |
| **try / except** | Manejo de errores | Ejecuta código "peligroso" y captura los errores para que el programa no se caiga. | `try: numero = int(input())` / `except ValueError: print("No es un número")` |
| **raise** | Lanzar un error manualmente | Fuerza que ocurra un error desde tu propio código, con un mensaje personalizado. | `raise ValueError("El valor no puede ser negativo")` |

---

## Funciones y Organización del Código

| Término | 🔍 ¿Qué es? | 🎯 ¿Para qué sirve? | 💻 Ejemplo |
| :--- | :--- | :--- | :--- |
| **def** | Definir una función | Crea un bloque de código reutilizable con un nombre. Se llama cuando lo necesitas. | `def saludar(nombre): print("Hola", nombre)` |
| **return** | Devolver un valor | Termina la función y devuelve un resultado al lugar que la llamó. | `def suma(a, b): return a + b` |
| **Parámetros / Argumentos** | Entradas de una función | Los datos que le pasas a una función para que trabaje con ellos. | `def calcular_imc(peso, estatura):` |
| **import** | Importar un módulo | Carga un módulo (de la librería estándar o externo) para usar sus funciones. | `import json`, `from pathlib import Path` |
| **Función pura** | Función sin efectos secundarios | Una función que solo depende de sus argumentos y siempre devuelve el mismo resultado para los mismos datos. Ideal para conversiones. | `def celsius_a_fahrenheit(c): return c * 9/5 + 32` |
| **main.py** | Archivo principal del proyecto | Por convención, el archivo de entrada del programa. Es el primero que se ejecuta. | `python3 main.py` |
| **if __name__ == "__main__":** | Punto de entrada del script | Permite que el código solo se ejecute si el archivo se corre directamente (no si se importa como módulo). | `if __name__ == "__main__": main()` |

---

## Librerías Usadas en los Retos

| Librería | 🔍 ¿Qué es? | 🎯 ¿Para qué sirve? | 💻 Cómo instalar |
| :--- | :--- | :--- | :--- |
| **json** | Módulo estándar | Leer y escribir archivos JSON. Perfecto para guardar datos entre ejecuciones. | Ya viene con Python (no instalar) |
| **csv** | Módulo estándar | Leer y escribir archivos CSV (hojas de cálculo en texto plano). Usado en el reto 04. | Ya viene con Python (no instalar) |
| **os** | Módulo estándar | Interactuar con el sistema operativo: rutas de archivos, variables de entorno, carpetas. | Ya viene con Python (no instalar) |
| **pathlib** | Módulo estándar | Manejo moderno de rutas de archivos. Más legible que `os.path`. Usado en el reto 08. | Ya viene con Python (no instalar) |
| **shutil** | Módulo estándar | Copiar, mover y eliminar archivos y carpetas. Usado en el reto 08 (organizador). | Ya viene con Python (no instalar) |
| **random** | Módulo estándar | Generar números aleatorios. Usado en el reto 03 (juego de adivinanza). ⚠️ NO usar para contraseñas reales. | Ya viene con Python (no instalar) |
| **secrets** | Módulo estándar | Generar números aleatorios *criptográficamente seguros*. Para contraseñas reales. Usado en el reto 05. | Ya viene con Python (no instalar) |
| **string** | Módulo estándar | Contiene cadenas de caracteres predefinidas: letras, dígitos, puntuación, etc. | Ya viene con Python (no instalar) |
| **argparse** | Módulo estándar | Leer argumentos y flags desde la línea de comandos de forma elegante. Ej: `--longitud 16 --simbolos`. | Ya viene con Python (no instalar) |
| **datetime** | Módulo estándar | Manejar fechas y horas. Usado en el reto 09 (recordatorios). | Ya viene con Python (no instalar) |
| **re** | Módulo estándar | Expresiones regulares para buscar y validar patrones de texto. Usado en el reto 12 (validador de emails). | Ya viene con Python (no instalar) |
| **requests** | Librería externa | Hacer peticiones HTTP (GET, POST) para consumir APIs o descargar páginas web. Usado en los retos 02 y 03-nerve. | `pip install requests` |
| **BeautifulSoup (bs4)** | Librería externa | Parsear (leer y navegar) el contenido HTML de una página web. Usado en el reto 02. | `pip install beautifulsoup4` |
| **rich** | Librería externa | Mostrar texto bonito en la terminal: colores, tablas, barras de progreso. Usado en el reto 02-nerve. | `pip install rich` |
| **Pillow** | Librería externa | Crear, editar y manipular imágenes desde Python. Usado en el reto 06-nerve (GIFs). | `pip install Pillow` |
| **black** | Librería externa | Formateador automático de código Python. El Linter Compasivo del repo lo usa para verificar el estilo. | `pip install black` |
| **discord.py** | Librería externa | Crear bots para Discord con Python. Usado en el reto 07-nerve. | `pip install discord.py` |
| **FastAPI** | Librería externa | Framework para crear APIs web de alta performance. Usado en el reto 08-nerve. | `pip install fastapi` |

---

## Conceptos de Calidad de Código

| Término | 🔍 ¿Qué es? | 🎯 ¿Para qué sirve? | 💻 Ejemplo |
| :--- | :--- | :--- | :--- |
| **Linter** | Analizador de estilo de código | Revisa tu código automáticamente en busca de errores de formato o malas prácticas. En este repo usamos `black`. | El "Linter Compasivo" que se ejecuta en cada PR |
| **black** | Formateador de Python | Reformatea tu código automáticamente para que siga el mismo estilo siempre. No tienes que pensar en espacios ni indentación. | `black mi_script.py` |
| **Indentación** | El espacio al inicio de las líneas | En Python, la indentación (4 espacios o 1 tab) NO es decorativa: define los bloques de código. Si está mal, el código falla. | `def suma():` ← sin indentar / `    return x` ← indentado (dentro de la función) |
| **dry-run (modo simulación)** | Ejecutar sin hacer cambios reales | Opción que simula lo que haría el script sin modificar nada. Fundamental en scripts que mueven o borran archivos. | `python organizador.py --dry-run` |
| **hardcoded** | Valor escrito directamente en el código | Un valor "quemado" en el código que no se puede cambiar sin editar el archivo. Es mala práctica para rutas y configuraciones. | ❌ `ruta = "/home/user/Descargas"` (hardcoded) ✓ `ruta = input("Ruta:")` |
| **Manejo de errores** | Anticipar y controlar fallos | Escribir código que no se "rompa" si algo sale mal (archivo inexistente, entrada inválida, red caída). Se hace con `try/except`. | `try: archivo = open("datos.csv")` / `except FileNotFoundError: print("El archivo no existe")` |

---

> 💡 **IMPORTANTE:** La librería estándar de Python ya incluye herramientas para hacer casi todo. Antes de instalar algo con `pip`, busca si ya existe en la librería estándar. ¡Muchas veces ya está todo ahí! 🐍

---

← [Volver al Índice del Glosario](README.md)
