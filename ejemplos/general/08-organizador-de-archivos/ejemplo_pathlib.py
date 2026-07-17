from pathlib import Path

# 1. Trabajar con rutas usando pathlib (es más moderno que os.path)
directorio_actual = Path.cwd()
archivo_ejemplo = directorio_actual / "ejemplo.txt"

# 2. Verificar si el archivo existe
if archivo_ejemplo.exists():
    print(f"El archivo existe en: {archivo_ejemplo}")
else:
    print(f"El archivo NO existe en: {archivo_ejemplo}")

# 3. Leer la extensión de un archivo
ruta_inventada = Path("/una/ruta/falsa/documento.pdf")
print(f"La extensión del archivo inventado es: {ruta_inventada.suffix}")

# 4. Obtener solo el nombre del archivo
print(f"El nombre del archivo es: {ruta_inventada.name}")
