# Reto 14: El Diario del Explorador 📓

Vas a crear un programa que guarde entradas de un diario en un archivo de texto.

## Instrucciones

Crea tu archivo en `solucion/` con el nombre `tu-usuario-14.py` y sigue los pasos:

1. Define una función llamada `guardar_entrada` que reciba dos parámetros: `nombre_archivo` (texto) y `entrada` (texto). Dentro, usa `with open(nombre_archivo, "a") as f` para abrir en modo añadir, y escribe `entrada` seguida de `"\n"`.

2. Define una función llamada `leer_diario` que reciba `nombre_archivo`. Dentro, usa un `try / except FileNotFoundError` para intentar abrir y leer el archivo completo con `.read()`. Si existe, devuelve el contenido. Si no existe, devuelve el texto `"El diario está vacío."`.

3. Fuera de las funciones:
   - Crea una lista `entradas` con 3 textos (escríbelos tú: frases cortas de explorador).
   - Usa un `for` para recorrer `entradas` y llamar a `guardar_entrada("diario.txt", entrada)` en cada vuelta.
   - Llama a `leer_diario("diario.txt")` e imprime el resultado.
   - Llama a `leer_diario("archivo_que_no_existe.txt")` e imprime el resultado.

**Resultado esperado en tu terminal:**
```text
--- Guardando entradas ---
3 entradas guardadas.
--- Contenido del diario ---
Día 1: Llegamos a la selva.
Día 2: Encontramos un río.
Día 3: Acampamos en la montaña.

--- Leyendo archivo inexistente ---
El diario está vacío.
```

> El archivo `diario.txt` se creará en la carpeta desde donde ejecutes el script.

Ejecuta desde la raíz del proyecto:
- **macOS / Linux:** `python3 python/Modulo-03-Exterior/04-archivos/solucion/tu-usuario-14.py`
- **Windows:** `python python/Modulo-03-Exterior/04-archivos/solucion/tu-usuario-14.py`
