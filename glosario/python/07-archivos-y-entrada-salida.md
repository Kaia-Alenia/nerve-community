# 07 - Archivos y entrada/salida

### `open() / with`

**¿Qué es?**
`open()` es la función para abrir un archivo. `with` es un 'gestor de contexto' que asegura que el archivo se cierre automáticamente cuando termines, pase lo que pase.

**¿Para qué se usa?**
Para leer o guardar información en el disco duro de forma segura sin dejar archivos 'bloqueados'.

**Ejemplo:**
```python
# Primero creamos el archivo
with open("datos.txt", "w") as archivo:
    archivo.write("Contenido de prueba")

with open("datos.txt", "r") as archivo:
    contenido = archivo.read()
```

**Errores comunes de principiante:**
- Olvidar el `with` y olvidar llamar a `archivo.close()`, causando fugas de memoria o que otros programas no puedan tocar el archivo.

**Términos relacionados:** [`CSV`](#csv)

### `lectura/escritura de archivos`

**¿Qué es?**
Los modos en los que abres un archivo: `'r'` para leer (read), `'w'` para escribir y borrar lo anterior (write), `'a'` para añadir al final (append).

**¿Para qué se usa?**
Para interactuar con el sistema de archivos.

**Ejemplo:**
```python
with open("log.txt", "a") as f:
    f.write("Nueva línea\n")
```

**Errores comunes de principiante:**
- Abrir un archivo en modo `'w'` pensando que vas a añadir datos, y terminar borrando todo su contenido original.

**Términos relacionados:** [`open() / with`](#open--with)

### `CSV`

**¿Qué es?**
Archivos de Valores Separados por Comas. Un formato muy sencillo para guardar tablas de datos (como un Excel simple en texto plano).

**¿Para qué se usa?**
Muy usado en el mundo real para importar y exportar reportes. En Python se usa la librería `csv` de la librería estándar.

**Ejemplo:**
```python
import csv

# Primero creamos el archivo
with open("datos.csv", "w", newline="") as f:
    f.write("a,b,c")

with open("datos.csv", "r") as f:
    lector = csv.reader(f)
```

**Errores comunes de principiante:**
- No especificar `newline=''` al abrir el archivo en Windows, lo que causa líneas en blanco extra.

**Términos relacionados:** [`JSON`](#json)

### `JSON`

**¿Qué es?**
JavaScript Object Notation. Un formato de texto estándar mundial para enviar y guardar datos estructurados. En Python, se ve idéntico a un diccionario.

**¿Para qué se usa?**
Es el idioma universal para que tu código hable con APIs de internet u otros lenguajes.

**Ejemplo:**
```python
import json
datos = json.loads('{"nombre": "Ana"}')
```

**Errores comunes de principiante:**
- Intentar serializar con `json.dumps()` cosas que no son nativas de JSON, como un objeto `datetime` de Python.

**Términos relacionados:** [`diccionarios`](../python/04-estructuras-de-datos.md#diccionarios-dicts)

