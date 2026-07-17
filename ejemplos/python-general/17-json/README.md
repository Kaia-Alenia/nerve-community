# Manejo de Archivos JSON

## ¿Qué muestra este ejemplo?
Muestra cómo utilizar la librería `json` integrada en Python para guardar (serializar) un diccionario en un archivo de texto, y posteriormente leer (deserializar) ese archivo de vuelta a un diccionario de Python.

## ¿Por qué es útil?
JSON (JavaScript Object Notation) es el formato de intercambio de datos más usado en la web. Es perfecto para guardar configuraciones de programas, estado de un juego, o para mandar información a APIs externas. Python traduce diccionarios a JSON de manera casi transparente.

## ¿Cómo correrlo?
Abre tu terminal, navega a esta carpeta y ejecuta:
```bash
python ejemplo_json.py
```
Pruébalo un par de veces consecutivas. Verás cómo el puntaje guardado es recordado en la siguiente ejecución. ¡Abre el archivo `score.json` generado para ver cómo luce!

## ¿Qué retos usan esta base?
-  **[Ver Issue #31 en GitHub: Python General 17 - Lector de Configuraciones (JSON/YAML)](https://github.com/Kaia-Alenia/nerve-community/issues/31)**

## Nota para principiantes
Fíjate siempre en la diferencia entre `json.dump()` (que escribe directamente en un archivo) y `json.dumps()` (que devuelve un *string* de JSON sin escribir nada). Lo mismo aplica para `load()` vs `loads()`. La letra "s" al final significa "string".
