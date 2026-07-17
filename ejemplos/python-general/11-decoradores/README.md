# Decoradores Básicos

## ¿Qué muestra este ejemplo?
Muestra cómo crear un decorador sencillo (`@log_ejecucion`) utilizando `functools.wraps` para añadir un comportamiento (imprimir mensajes de inicio y fin) alrededor de una función existente sin modificar su código interno.

## ¿Por qué es útil?
Los decoradores son una característica poderosa de Python para reutilizar código. Permiten extraer lógica repetitiva (como registros, validaciones, o comprobaciones de acceso) y aplicarla limpiamente a múltiples funciones con solo agregar un `@nombre_decorador` arriba de su definición.

## ¿Cómo correrlo?
Abre tu terminal, navega a esta carpeta y ejecuta:
```bash
python ejemplo_decorador.py
```

## ¿Qué retos usan esta base?
- 👉 **[Ver Issue #25 en GitHub: Python General 11 - Profiler de Funciones](https://github.com/Kaia-Alenia/nerve-community/issues/25)**

## Nota para principiantes
Recuerda siempre importar `functools` y usar `@functools.wraps(funcion)` dentro de tu decorador. Si no lo haces, la función perderá su nombre original (`__name__`) y su docstring, lo cual dificulta la depuración.
