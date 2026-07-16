## Conteo de Frecuencias (Counter)

**¿Qué muestra este ejemplo?**
Cómo usar la estructura de datos especializada `collections.Counter` para contar la frecuencia de elementos en un iterable (como palabras o letras) de manera eficiente.

**¿Por qué es útil?**
Evita escribir bucles largos y anidados con diccionarios para llevar la cuenta de repeticiones y permite obtener rápidamente los elementos más comunes (top N).

**Cómo correrlo**
- No necesita instalar nada extra, todo es librería estándar de Python.
- Comando para ejecutarlo: `python ejemplo_counter.py`

**¿Qué retos usan esta base?**
- [#22 Python General 10 — Analizador de texto](https://github.com/Kaia-Alenia/nerve-community/issues/22)

**Nota para principiantes**
`Counter` tiene un método interno muy útil llamado `.most_common(n)` que te devuelve automáticamente una lista ordenada con los `n` elementos más repetidos sin tener que ordenarla tú mismo.