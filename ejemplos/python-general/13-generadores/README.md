# Generadores en Python

## ¿Qué muestra este ejemplo?
Muestra cómo crear una función generadora usando la palabra clave `yield` para producir una secuencia de números de la serie de Fibonacci, bajo demanda.

## ¿Por qué es útil?
Los generadores permiten procesar o crear secuencias enormes de datos de forma perezosa (lazy). En lugar de calcular y almacenar 1 millón de elementos en una lista (lo que agotaría la memoria RAM), un generador calcula y entrega solo el elemento que necesitas en ese exacto instante.

## ¿Cómo correrlo?
Abre tu terminal, navega a esta carpeta y ejecuta:
```bash
python ejemplo_generadores.py
```

## ¿Qué retos usan esta base?
-  **[Ver Issue #27 en GitHub: Python General 13 - Lector de Archivos Gigantes (Generadores)](https://github.com/Kaia-Alenia/nerve-community/issues/27)**

## Nota para principiantes
Cuando una función tiene `yield` en lugar de `return`, Python sabe que es un generador. Al llamarla, no ejecuta el código inmediatamente, sino que devuelve un objeto iterador. El código solo avanza hasta el siguiente `yield` cada vez que usas un ciclo `for` o la función `next()`.
