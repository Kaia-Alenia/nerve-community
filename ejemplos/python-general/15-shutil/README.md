# Operaciones de Archivos con shutil

## ¿Qué muestra este ejemplo?
Muestra cómo usar la librería estándar `shutil` (utilidades de shell) para realizar operaciones de alto nivel sobre archivos y directorios, específicamente cómo empaquetar una carpeta completa en un archivo `.zip` usando `make_archive`.

## ¿Por qué es útil?
Mientras que la librería `os` o `pathlib` te sirven para interactuar con un solo archivo (leerlo, borrarlo), `shutil` está diseñado para operaciones masivas: copiar árboles completos de directorios, mover carpetas de un disco a otro, o comprimir proyectos enteros en una sola línea.

## ¿Cómo correrlo?
Abre tu terminal, navega a esta carpeta y ejecuta:
```bash
python ejemplo_shutil.py
```
Al finalizar, verás un nuevo archivo llamado `mi_backup.zip`.

## ¿Qué retos usan esta base?
-  **[Ver Issue #29 en GitHub: Python General 15 - Herramienta de Backup de Archivos](https://github.com/Kaia-Alenia/nerve-community/issues/29)**

## Nota para principiantes
El módulo `shutil` tiene muchas funciones útiles como `shutil.copy()` y `shutil.move()`. Son las equivalentes a usar los comandos `cp` y `mv` en una terminal de Linux o Mac, pero directamente desde Python.
