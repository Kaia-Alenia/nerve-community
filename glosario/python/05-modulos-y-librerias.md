# 05 - Módulos y librerías

### `import / from...import`

**¿Qué es?**
La instrucción para traer código (módulos o librerías) a tu script actual para poder usarlo.

**¿Para qué se usa?**
Para no tener que reinventar la rueda y usar herramientas que ya están hechas, ya sean tuyas o de terceros.

**Ejemplo:**
```python
import math
from datetime import datetime
```

**Errores comunes de principiante:**
- Importaciones circulares (el archivo A importa a B, y B importa a A).
- Olvidar instalar un paquete antes de importarlo (`ModuleNotFoundError`).

**Términos relacionados:** [`pip install`](#pip-install)

### `pip install`

**¿Qué es?**
El comando para descargar e instalar librerías externas de internet (desde PyPI) hacia tu computadora.

**¿Para qué se usa?**
Para añadir superpoderes a tu proyecto, como `requests` para descargar webs o `fastapi` para hacer servidores.

**Ejemplo:**
```bash
pip install requests
```

**Errores comunes de principiante:**
- Correrlo fuera de un entorno virtual, ensuciando la instalación global de Python de tu computadora.

**Términos relacionados:** [`entornos virtuales (venv)`](#entornos-virtuales-venv)

### `requirements.txt`

**¿Qué es?**
Un archivo de texto plano que lista todas las librerías externas y sus versiones exactas que necesita tu proyecto para funcionar.

**¿Para qué se usa?**
Para que cuando otro desarrollador descargue tu código, pueda instalar todo rápidamente con `pip install -r requirements.txt`.

**Ejemplo:**
```text
requests==2.31.0
fastapi==0.104.1
```

**Errores comunes de principiante:**
- Olvidar actualizar este archivo cuando instalas una librería nueva en tu proyecto.

**Términos relacionados:** [`pip install`](#pip-install)

### `entornos virtuales (venv)`

**¿Qué es?**
Una carpeta aislada dentro de tu proyecto donde se instalan las librerías, sin afectar a otros proyectos de tu PC.

**¿Para qué se usa?**
Para evitar conflictos. El Proyecto A puede usar Django 3 y el Proyecto B puede usar Django 4 sin pelearse.

**Ejemplo:**
```bash
python -m venv env
source env/bin/activate # En Linux/Mac
```

**Errores comunes de principiante:**
- Olvidar activar el entorno virtual antes de instalar paquetes o ejecutar tu código.
- Subir la carpeta del entorno a GitHub (debe ignorarse en el `.gitignore`).

**Términos relacionados:** [`pip install`](#pip-install)

### `json`

**¿Qué es?**
Módulo estándar para procesar (serializar y deserializar) el formato de intercambio de datos JSON, transformando strings a diccionarios de Python y viceversa.

**¿Para qué se usa?**
Leer y escribir archivos JSON. Perfecto para guardar datos entre ejecuciones.

**Ejemplo:**
```python
import json
with open('datos.json', 'w') as f:
    json.dump({'clave': 'valor'}, f)
```

**Errores comunes de principiante:**
- Usar `json.loads` en vez de `json.load` al leer archivos.

**Términos relacionados:** `import`

### `csv`

**¿Qué es?**
Módulo estándar diseñado para leer y escribir archivos de texto delimitados por comas (CSV), facilitando el manejo de datos tabulares y hojas de cálculo.

**¿Para qué se usa?**
Leer y escribir archivos CSV (hojas de cálculo en texto plano). Usado en el reto 04.

**Ejemplo:**
```python
import csv
# Primero creamos un archivo de prueba
with open('datos.csv', mode='w', newline='') as f:
    f.write('id,nombre\n1,Test')

# Luego lo leemos
with open('datos.csv', mode='r') as f:
    lector = csv.reader(f)
```

**Errores comunes de principiante:**
- Olvidar especificar `newline=''` al abrir el archivo en modo escritura.

**Términos relacionados:** `import`

### `os`

**¿Qué es?**
Módulo estándar que provee una forma portable de interactuar con el sistema operativo subyacente, permitiendo leer/escribir variables de entorno, manipular rutas, crear carpetas y gestionar procesos.

**¿Para qué se usa?**
Interactuar con el sistema operativo: rutas de archivos, variables de entorno, carpetas.

**Ejemplo:**
```python
import os
carpeta = os.getcwd()
```

**Errores comunes de principiante:**
- Usar `os.path.join` incorrectamente o no manejar errores de permisos.

**Términos relacionados:** `pathlib`

### `pathlib`

**¿Qué es?**
Módulo estándar introducido en Python 3.4 que ofrece clases para manejar rutas del sistema de archivos con una sintaxis orientada a objetos (usando `/`), reemplazando las antiguas funciones de manipulación de strings de `os.path`.

**¿Para qué se usa?**
Manejo moderno de rutas de archivos. Más legible que `os.path`. Usado en el reto 08.

**Ejemplo:**
```python
from pathlib import Path
ruta = Path('.') / 'archivo.txt'
```

**Errores comunes de principiante:**
- Seguir usando `os` para rutas simples cuando `pathlib` es más limpio y seguro.

**Términos relacionados:** `os`

### `shutil`

**¿Qué es?**
Módulo estándar que provee operaciones de alto nivel sobre archivos y colecciones enteras, incluyendo funciones para copiar (shutil.copy), mover (shutil.move) y borrar recursivamente árboles de directorios (shutil.rmtree).

**¿Para qué se usa?**
Copiar, mover y eliminar archivos y carpetas. Usado en el reto 08 (organizador).

**Ejemplo:**
```python
import shutil
import os

# Creamos un archivo de origen para el ejemplo
with open('origen.txt', 'w') as f:
    f.write('hola')

shutil.move('origen.txt', 'destino.txt')

# Limpiamos el archivo de destino para no dejar basura
os.remove('destino.txt')
```

**Errores comunes de principiante:**
- Intentar mover un archivo a una carpeta que no existe sin crearla primero.

**Términos relacionados:** `os`, `pathlib`

### `random`

**¿Qué es?**
Módulo estándar que implementa generadores de números pseudoaleatorios para diversas distribuciones, útil para juegos, simulaciones y selecciones al azar. NO es seguro para uso criptográfico.

**¿Para qué se usa?**
Generar números aleatorios. Usado en el reto 03 (juego de adivinanza).

**Ejemplo:**
```python
import random
numero = random.randint(1, 10)
```

**Errores comunes de principiante:**
- Usarlo para contraseñas o datos criptográficos (es predecible).

**Términos relacionados:** `secrets`

### `secrets`

**¿Qué es?**
Módulo estándar diseñado para generar números aleatorios criptográficamente seguros. Es la herramienta adecuada y recomendada para gestionar datos sensibles como contraseñas, tokens de autenticación y claves.

**¿Para qué se usa?**
Generar números aleatorios criptográficamente seguros. Para contraseñas reales. Usado en el reto 05.

**Ejemplo:**
```python
import secrets
token = secrets.token_hex(16)
```

**Errores comunes de principiante:**
- Usarlo para simulaciones simples donde `random` es más rápido y suficiente.

**Términos relacionados:** `random`

### `string`

**¿Qué es?**
Módulo estándar que expone constantes de cadenas de texto muy útiles (como `string.ascii_letters`, `string.digits` o `string.punctuation`) y clases avanzadas para formatear texto.

**¿Para qué se usa?**
Contiene cadenas de caracteres predefinidas: letras, dígitos, puntuación, etc.

**Ejemplo:**
```python
import string
letras = string.ascii_letters
```

**Errores comunes de principiante:**
- Reinventar la rueda escribiendo a mano `abcdefg...` en lugar de usar `string.ascii_lowercase`.

**Términos relacionados:** `import`

### `argparse`

**¿Qué es?**
Módulo estándar para escribir interfaces de línea de comandos (CLI) complejas. Permite definir qué argumentos posicionales y banderas (flags) espera el programa y los parsea automáticamente desde sys.argv.

**¿Para qué se usa?**
Leer argumentos y flags desde la línea de comandos de forma elegante.

**Ejemplo:**
```python
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--nombre')
```

**Errores comunes de principiante:**
- Hacer lógica muy compleja antes de llamar a `parser.parse_args()`.

**Términos relacionados:** `import`

### `datetime`

**¿Qué es?**
Módulo estándar que provee clases para manipular fechas y horas (datetime, date, time, timedelta) soportando operaciones matemáticas de tiempo, formateo a strings (strftime) y parseo (strptime).

**¿Para qué se usa?**
Manejar fechas y horas. Usado en el reto 09 (recordatorios).

**Ejemplo:**
```python
from datetime import datetime
ahora = datetime.now()
```

**Errores comunes de principiante:**
- Confundir `datetime.datetime` con el módulo `datetime`, o no manejar zonas horarias (timezone naive).

**Términos relacionados:** `import`

### `re`

**¿Qué es?**
Módulo estándar que proporciona operaciones de expresiones regulares (regex). Permite buscar, extraer, reemplazar y validar patrones de texto muy específicos de manera eficiente.

**¿Para qué se usa?**
Expresiones regulares para buscar y validar patrones de texto. Usado en el reto 12 (validador de emails).

**Ejemplo:**
```python
import re
es_valido = re.match(r'^\w+@\w+\.\w+$', 'test@test.com')
```

**Errores comunes de principiante:**
- Escribir expresiones regulares demasiado complejas que son difíciles de leer y mantener.

**Términos relacionados:** `import`

### `requests`

**¿Qué es?**
Una librería externa muy popular que simplifica enormemente el proceso de enviar peticiones HTTP (como GET o POST) en Python, haciendo el código más legible.

**¿Para qué se usa?**
Hacer peticiones HTTP (GET, POST) para consumir APIs o descargar páginas web. Usado en los retos 02 y 03-nerve.

**Ejemplo:**
```python
import requests
res = requests.get('https://api.github.com')
print(res.json())
```

**Errores comunes de principiante:**
- No manejar posibles excepciones de conexión (`requests.exceptions.RequestException`) o time-outs.

**Términos relacionados:** `pip install`

### `BeautifulSoup (bs4)`

**¿Qué es?**
Una librería externa para extraer datos de archivos HTML y XML, facilitando el web scraping al permitir navegar y buscar en el árbol de elementos de forma intuitiva.

**¿Para qué se usa?**
Parsear (leer y navegar) el contenido HTML de una página web. Usado en el reto 02.

**Ejemplo:**
```python
from bs4 import BeautifulSoup
soup = BeautifulSoup('<html></html>', 'html.parser')
```

**Errores comunes de principiante:**
- Olvidar instalar el parser como `lxml` o usar selectores muy frágiles que se rompen si cambia la web.

**Términos relacionados:** `requests`, `pip install`

### `rich`

**¿Qué es?**
Una librería externa para escribir texto enriquecido (con colores y estilos) a la terminal, además de proveer componentes avanzados como tablas o barras de progreso.

**¿Para qué se usa?**
Mostrar texto bonito en la terminal: colores, tablas, barras de progreso. Usado en el reto 02-nerve.

**Ejemplo:**
```python
from rich.console import Console
console = Console()
console.print('[bold red]Error[/bold red]')
```

**Errores comunes de principiante:**
- Usar demasiados colores dificultando la lectura en algunas terminales.

**Términos relacionados:** `pip install`

### `Pillow`

**¿Qué es?**
Una librería externa que agrega soporte para abrir, manipular y guardar muchos formatos de archivos de imagen; es un "fork" moderno y mantenido de PIL.

**¿Para qué se usa?**
Crear, editar y manipular imágenes desde Python. Usado en el reto 06-nerve (GIFs).

**Ejemplo:**
```python
from PIL import Image

# Creamos una imagen de prueba temporal (100x100 píxeles, color rojo)
img = Image.new('RGB', (100, 100), color = 'red')
# img.show() # Muestra la imagen en el visor por defecto
```

**Errores comunes de principiante:**
- No cerrar los archivos de imagen después de procesarlos (mejor usar `with`).

**Términos relacionados:** `pip install`

### `black`

**¿Qué es?**
Una librería externa que funciona como un formateador de código Python "sin compromisos", asegurando un estilo consistente en todo el proyecto automáticamente.

**¿Para qué se usa?**
Formateador automático de código Python. El Linter Compasivo del repo lo usa para verificar el estilo.

**Ejemplo:**
```bash
# Instalación
pip install black

# Principalmente se usa en la terminal:
black mi_script.py
```

**Errores comunes de principiante:**
- Pelear contra las reglas de black en vez de aceptarlas; black es estricto por diseño.

**Términos relacionados:** `pip install`, `Linter`

### `discord.py`

**¿Qué es?**
Una librería externa robusta y moderna para interactuar asíncronamente con la API de Discord, permitiendo crear bots complejos con Python.

**¿Para qué se usa?**
Crear bots para Discord con Python. Usado en el reto 07-nerve.

**Ejemplo:**
```python
try:
    import discord
    cliente = discord.Client(intents=discord.Intents.default())
except ImportError:
    pass # Ignoramos el error si la librería no está instalada
```

**Errores comunes de principiante:**
- Bloquear el event loop principal usando funciones síncronas pesadas (como `time.sleep`).

**Términos relacionados:** `pip install`, `async/await`

### `FastAPI`

**¿Qué es?**
Un framework web externo, moderno y de alto rendimiento, para construir APIs en Python basándose en las sugerencias de tipos (type hints).

**¿Para qué se usa?**
Framework para crear APIs web de alta performance. Usado en el reto 08-nerve.

**Ejemplo:**
```python
from fastapi import FastAPI
app = FastAPI()
@app.get('/')
def read_root(): return {'Hola': 'Mundo'}
```

**Errores comunes de principiante:**
- No definir correctamente los modelos Pydantic o confundir rutas síncronas/asíncronas.

**Términos relacionados:** `pip install`

### `if __name__ == "__main__":`

**¿Qué es?**
Una condición especial que pregunta: "¿Este archivo fue ejecutado directamente o fue importado por otro?".

**¿Para qué se usa?**
Para poner código (como pruebas o llamadas a la función principal) que solo debe correr cuando tú ejecutas el script, pero que no debe ejecutarse si alguien más importa tu archivo para usar sus funciones.

**Ejemplo:**
```python
def sumar(a, b):
    return a + b

if __name__ == "__main__":
    print(sumar(2, 2)) # Solo se imprime si ejecutas este archivo directamente
```

**Errores comunes de principiante:**
- Poner todas las funciones dentro del `if __name__ == "__main__":`, haciéndolas inaccesibles para otros archivos que quieran importarlas.

**Términos relacionados:** [`import`](#import--fromimport)

### `main.py`

**¿Qué es?**
Por convención, es el archivo de punto de entrada o script principal de un proyecto en Python. Sirve como el coordinador central que importa y ejecuta el resto de módulos de tu aplicación.

**¿Para qué se usa?**
Por convención, el archivo de entrada del programa. Es el primero que se ejecuta para inicializar tu aplicación o script.

**Ejemplo:**
```python
# main.py
# Simulemos el módulo para el ejemplo
class MiModulo:
    def iniciar(self):
        print("Iniciado")
mi_modulo = MiModulo()

if __name__ == "__main__":
    print("Iniciando la aplicación...")
    mi_modulo.iniciar()
```

**Errores comunes de principiante:**
- Llenar el `main.py` de miles de líneas de lógica en lugar de importar funciones de otros módulos bien organizados.

**Términos relacionados:** [`if __name__ == "__main__":`](#if-__name__--__main__)
