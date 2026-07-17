"""
Ejemplo: Organizar archivos de prueba en subcarpetas según su extensión

Qué enseña este ejemplo:
  - Cómo usar pathlib.Path para manejar rutas de forma moderna
  - Cómo listar todos los archivos de una carpeta con iterdir()
  - Cómo leer la extensión de un archivo con .suffix
  - Cómo mover archivos con shutil.move()
  - Cómo crear subcarpetas si no existen con mkdir(parents=True, exist_ok=True)

Para tu reto (organizador de archivos):
  Aplica el mismo patrón: recibe una ruta por argumento,
  itera los archivos, clasifica por extensión, y muévelos.
  Agrega el modo --dry-run para simular sin mover nada.

Glosario de términos "raros" (pathlib y shutil):
  Path("ruta")          — crea un objeto Path (más potente que un string de ruta)
  Path.cwd()            — devuelve la carpeta de trabajo actual
  ruta.iterdir()        — genera todos los archivos y carpetas dentro de 'ruta'
  archivo.is_file()     — True si es un archivo, False si es carpeta o symlink
  archivo.suffix        — la extensión: ".py", ".txt", ".jpg", etc. (con el punto)
  archivo.name          — nombre completo: "foto.jpg"
  archivo.stem          — nombre sin extensión: "foto"
  ruta.mkdir(...)       — crea la carpeta (parents=True crea carpetas intermedias)
                          (exist_ok=True no falla si ya existe)

Glosario de shutil:
  shutil.move(origen, destino) — mueve un archivo o carpeta de una ruta a otra
"""

import shutil
from pathlib import Path

# Mapa de extensiones → nombre de subcarpeta
EXTENSIONES = {
    ".jpg": "Imagenes",
    ".jpeg": "Imagenes",
    ".png": "Imagenes",
    ".gif": "Imagenes",
    ".pdf": "Documentos",
    ".docx": "Documentos",
    ".txt": "Documentos",
    ".mp3": "Audio",
    ".wav": "Audio",
    ".py": "Scripts",
    ".js": "Scripts",
}


def organizar_carpeta(ruta_carpeta: str, dry_run: bool = False):
    """
    Organiza los archivos de 'ruta_carpeta' en subcarpetas según extensión.

    dry_run=True → solo imprime qué haría, sin mover nada.
    dry_run=False → ejecuta los movimientos realmente.
    """
    carpeta = Path(ruta_carpeta)

    if not carpeta.exists() or not carpeta.is_dir():
        print(f"Error: '{ruta_carpeta}' no es una carpeta válida.")
        return

    modo = "[SIMULACIÓN]" if dry_run else "[EJECUTANDO]"
    print(f"\n{modo} Organizando: {carpeta}\n")

    movidos = 0
    ignorados = 0

    # iterdir() genera todos los elementos dentro de la carpeta
    for archivo in carpeta.iterdir():
        # Solo procesamos archivos (ignoramos subcarpetas)
        if not archivo.is_file():
            continue

        # .suffix devuelve la extensión en minúsculas con el punto (ej: ".jpg")
        extension = archivo.suffix.lower()

        if extension not in EXTENSIONES:
            print(f"  ⚠ Sin categoría: {archivo.name} (ignorado)")
            ignorados += 1
            continue

        # Determinar la subcarpeta destino
        nombre_subcarpeta = EXTENSIONES[extension]
        carpeta_destino = carpeta / nombre_subcarpeta

        print(f"  → {archivo.name} → {nombre_subcarpeta}/")

        if not dry_run:
            # Crear la subcarpeta si no existe
            carpeta_destino.mkdir(parents=True, exist_ok=True)
            # Mover el archivo
            shutil.move(str(archivo), carpeta_destino / archivo.name)

        movidos += 1

    print(f"\nResumen: {movidos} archivo(s) {'a mover' if dry_run else 'movidos'}, {ignorados} ignorados.")


if __name__ == "__main__":
    import tempfile
    import os

    # Crear carpeta temporal con archivos de ejemplo para demostrar
    with tempfile.TemporaryDirectory() as tmp:
        archivos_prueba = [
            "foto_verano.jpg", "presentacion.pdf", "notas.txt",
            "cancion.mp3", "script_util.py", "archivo_raro.xyz"
        ]
        for nombre in archivos_prueba:
            (Path(tmp) / nombre).touch()

        print("Archivos de prueba creados:")
        for f in os.listdir(tmp):
            print(f"  {f}")

        # Primero simulamos (dry_run=True)
        organizar_carpeta(tmp, dry_run=True)

        # Luego ejecutamos
        print("\n--- Ahora ejecutamos realmente ---")
        organizar_carpeta(tmp, dry_run=False)

        print("\nEstructura resultante:")
        for item in sorted(Path(tmp).rglob("*")):
            nivel = len(item.relative_to(tmp).parts) - 1
            print("  " * nivel + item.name)
