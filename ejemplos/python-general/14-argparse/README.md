# Interfaz de Línea de Comandos (CLI) con argparse

## ¿Qué muestra este ejemplo?
Muestra cómo utilizar la librería estándar `argparse` para crear una mini-calculadora por línea de comandos que acepta argumentos como `--operacion`, `--a` y `--b`, validando sus tipos.

## ¿Por qué es útil?
Scripts profesionales de Python rara vez utilizan `input()` para pedir datos de forma interactiva. Usar argumentos por terminal permite automatizar herramientas y usarlas en tuberías (pipelines) sin requerir intervención humana, y proveen ayuda (`--help`) de forma automática.

## ¿Cómo correrlo?
Abre tu terminal, navega a esta carpeta y ejecuta:
```bash
python ejemplo_argparse.py --operacion suma --a 10 --b 5.5
python ejemplo_argparse.py --operacion multiplicacion --a 4 --b 2
```

Puedes ver el menú de ayuda integrado corriendo:
```bash
python ejemplo_argparse.py --help
```

## ¿Qué retos usan esta base?
-  **[Ver Issue #28 en GitHub: Python General 14 - CLI del Clima (APIs y argparse)](https://github.com/Kaia-Alenia/nerve-community/issues/28)**

## Nota para principiantes
Nota cómo definimos los tipos en `add_argument(..., type=float)`. `argparse` se encarga de convertir automáticamente el texto que introduces en la terminal al tipo de dato que programaste, e incluso lanzará un error limpio si el usuario pasa letras en vez de números.
