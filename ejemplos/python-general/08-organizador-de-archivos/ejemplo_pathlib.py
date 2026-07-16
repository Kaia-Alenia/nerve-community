from pathlib import Path
import shutil

# 1. Trabajar con rutas usando pathlib (es más moderno que os.path)
directorio_actual = Path.cwd()
carpeta_nueva = directorio_actual / "mi_carpeta_temporal"
archivo_origen = directorio_actual / "archivo_prueba.txt"
archivo_destino = carpeta_nueva / "archivo_movido.txt"

# 2. Crear una carpeta (exist_ok=True evita errores si ya existe)
carpeta_nueva.mkdir(exist_ok=True)
print(f"Carpeta lista: {carpeta_nueva}")

# 3. Crear un archivo de texto de prueba
archivo_origen.write_text("Hola, soy un archivo temporal.", encoding="utf-8")

# 4. Mover / Renombrar el archivo de forma segura
if archivo_origen.exists() and not archivo_destino.exists():
    # shutil.move mueve el archivo de origen al destino
    shutil.move(str(archivo_origen), str(archivo_destino))
    print(f"Archivo movido a: {archivo_destino}")

# 5. Leer el archivo desde su nueva ubicación
print("Contenido:", archivo_destino.read_text(encoding="utf-8"))
