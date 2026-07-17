## Manejo de Rutas (Pathlib)

**¿Qué muestra este ejemplo?**
Cómo construir, validar y manipular rutas de archivos del sistema operativo usando el módulo moderno `pathlib` en lugar del antiguo `os.path`.

**¿Por qué es útil?**
Hace que el código que manipula archivos y carpetas sea legible y que funcione exactamente igual en Windows, macOS y Linux sin preocuparse por la dirección de las barras (`/` vs `\`).

**Cómo correrlo**
- No necesita instalar nada extra, todo es librería estándar de Python.
- Comando para ejecutarlo: `python ejemplo_pathlib.py`

**¿Qué retos usan esta base?**
- [#20 Python General 08 — Organizador automático de archivos](https://github.com/Kaia-Alenia/nerve-community/issues/20)

**Nota para principiantes**
Con `pathlib.Path`, puedes unir rutas usando el operador de división `/` (ej. `ruta_base / "carpeta" / "archivo.txt"`), lo cual es mucho más limpio que usar `os.path.join()`.