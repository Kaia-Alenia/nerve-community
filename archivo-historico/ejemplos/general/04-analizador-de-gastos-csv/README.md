## Lectura y Procesamiento de CSV

**¿Qué muestra este ejemplo?**
Cómo leer y escribir archivos CSV (Comma-Separated Values) usando el módulo `csv` de la librería estándar, especialmente usando `csv.DictReader` para mayor claridad.

**¿Por qué es útil?**
Es esencial para procesar exportaciones de bases de datos, hojas de cálculo, registros financieros y datos tabulares estructurados sin depender de librerías pesadas como Pandas.

**Cómo correrlo**
- No necesita instalar nada extra, todo es librería estándar de Python.
- Comando para ejecutarlo: `python ejemplo_csv.py`

**¿Qué retos usan esta base?**
- [#16 Python General 04 — Analizador de gastos personales (CSV)](https://github.com/Kaia-Alenia/nerve-community/issues/16)

**Nota para principiantes**
Presta mucha atención al parámetro `encoding="utf-8"` al abrir el archivo, especialmente en Windows, para evitar errores al leer acentos u otros caracteres especiales del idioma español.