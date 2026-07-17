# Expresiones Regulares (Regex)

## ¿Qué muestra este ejemplo?
Muestra cómo usar el módulo `re` de Python y expresiones regulares (regex) para validar que un número de teléfono mexicano tenga un formato estricto (`+52 XXXXXXXXXX`).

## ¿Por qué es útil?
Validar entradas de usuario es una de las tareas más comunes en la programación. Usar expresiones regulares te permite describir formatos muy específicos de texto en una sola línea de código, evitando tener que hacer múltiples condicionales y ciclos manuales.

## ¿Cómo correrlo?
Abre tu terminal, navega a esta carpeta y ejecuta:
```bash
python ejemplo_regex.py
```

## ¿Qué retos usan esta base?
-  **[Ver Issue #26 en GitHub: Python General 12 - Validador de Emails con Regex](https://github.com/Kaia-Alenia/nerve-community/issues/26)**

## Nota para principiantes
Los strings de las expresiones regulares suelen llevar una `r` antes de las comillas (ej. `r'^\+52'`). Esto indica que es un "raw string", evitando que Python interprete caracteres como `\n` o `\t` de forma especial, dejándolos intactos para que el motor regex los procese.
