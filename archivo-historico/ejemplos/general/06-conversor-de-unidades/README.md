## Funciones Puras y Menús

**¿Qué muestra este ejemplo?**
Cómo diseñar funciones puras (que solo reciben parámetros y devuelven un resultado, sin modificar variables globales ni usar `print` dentro) y cómo armar un menú interactivo en la terminal usando bucles y `if/elif`.

**¿Por qué es útil?**
Dividir tu código en funciones pequeñas, especializadas y sin efectos secundarios hace que el programa sea mucho más fácil de probar, mantener y reutilizar.

**Cómo correrlo**
- No necesita instalar nada extra, todo es librería estándar de Python.
- Comando para ejecutarlo: `python ejemplo_funciones.py`

**¿Qué retos usan esta base?**
- [#18 Python General 06 — Conversor de unidades](https://github.com/Kaia-Alenia/nerve-community/issues/18)

**Nota para principiantes**
Evita poner llamadas a `print()` o `input()` dentro de tus funciones matemáticas o lógicas. La función debe encargarse solo de calcular y devolver (`return`) el resultado; el menú principal se encarga de mostrarlo al usuario.
