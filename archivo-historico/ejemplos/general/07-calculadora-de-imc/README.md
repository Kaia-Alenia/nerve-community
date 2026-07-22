## Múltiples Parámetros y Formateo de Strings

**¿Qué muestra este ejemplo?**
Cómo crear funciones que aceptan múltiples parámetros y cómo usar `f-strings` para redondear y formatear salidas numéricas de forma amigable para el usuario.

**¿Por qué es útil?**
Cuando necesitas hacer cálculos que dependen de varios factores (como el IMC que usa peso y estatura) y quieres mostrar el resultado con un límite de decimales para que no se vea desordenado.

**Cómo correrlo**
- No necesita instalar nada extra, todo es librería estándar de Python.
- Comando para ejecutarlo: `python ejemplo_formateo.py`

**¿Qué retos usan esta base?**
- [#19 Python General 07 — Calculadora de IMC](https://github.com/Kaia-Alenia/nerve-community/issues/19)

**Nota para principiantes**
Para redondear un número flotante a 2 decimales dentro de un f-string, simplemente agrega `:.2f` después del nombre de la variable (ej. `f"El resultado es {valor:.2f}"`).
