## Validación de Inputs

**¿Qué muestra este ejemplo?**
Cómo pedir datos al usuario usando `input()` y validarlos correctamente con bucles `while` y bloques `try/except` hasta que ingrese un tipo de dato válido.

**¿Por qué es útil?**
Previene que un programa interactivo de consola colapse cuando un usuario ingresa texto en lugar de números o presiona "Enter" en lugar de elegir una opción válida de un menú.

**Cómo correrlo**
- No necesita instalar nada extra, todo es librería estándar de Python.
- Comando para ejecutarlo: `python ejemplo_validacion.py`

**¿Qué retos usan esta base?**
- [#15 Python General 03 — Juego de adivina el número](https://github.com/Kaia-Alenia/nerve-community/issues/15)
- [#18 Python General 06 — Conversor de unidades](https://github.com/Kaia-Alenia/nerve-community/issues/18)
- [#19 Python General 07 — Calculadora de IMC](https://github.com/Kaia-Alenia/nerve-community/issues/19)

**Nota para principiantes**
El valor devuelto por `input()` siempre es una cadena de texto (`str`). No olvides convertirlo explícitamente a `int` o `float` antes de hacer operaciones matemáticas.