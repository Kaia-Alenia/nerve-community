## Manejo de Archivos JSON

**¿Qué muestra este ejemplo?**
Cómo leer y escribir archivos JSON de forma segura usando el módulo `json` de la librería estándar, incluyendo cómo manejar el caso donde el archivo no existe en la primera ejecución.

**¿Por qué es útil?**
Sirve para guardar configuración de un programa, cachear datos, o persistir información simple entre diferentes ejecuciones sin necesitar una base de datos completa.

**Cómo correrlo**
- No necesita instalar nada extra, todo es librería estándar de Python.
- Comando para ejecutarlo: `python ejemplo_json.py`

**¿Qué retos usan esta base?**
- [#13 Python General 01 — Lista de tareas (to-do list) en terminal](https://github.com/Kaia-Alenia/nerve-community/issues/13)
- [#21 Python General 09 — Recordatorios en terminal](https://github.com/Kaia-Alenia/nerve-community/issues/21)

**Nota para principiantes**
Recuerda que `json.dump` reescribe el archivo completo. Si quieres agregar un solo elemento a una lista, primero debes cargar la lista con `json.load`, hacer el `.append()`, y volver a guardarla completa.