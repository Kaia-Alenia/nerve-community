"""
Ejemplo: Comprimir carpetas con filtro usando shutil.make_archive + pathlib

Qué enseña este ejemplo:
  - Cómo comprimir una carpeta completa con shutil.make_archive()
  - Cómo copiar solo archivos que cumplan un criterio (filtro por extensión)
  - Cómo usar pathlib.rglob() para buscar archivos de forma recursiva
  - Cómo dar nombre al backup con la fecha actual

Para tu reto (herramienta de backup):
  Aplica el mismo patrón: shutil.copy2() para copiar archivos con metadatos,
  y agrega la fecha al nombre para no sobreescribir backups anteriores.
  Usa pathlib para manejar las rutas.

Glosario:
  shutil.make_archive(nombre, formato, carpeta)
    → Comprime 'carpeta' en un archivo 'nombre.formato'
    → Formatos disponibles: "zip", "tar", "gztar" (tar.gz), "bztar", "xztar"
    → Devuelve la ruta del archivo creado

  shutil.copy2(origen, destino)
    → Copia un archivo preservando metadatos (fecha de modificación, permisos)
    → shutil.copy() solo copia contenido; copy2() también copia metadatos

  pathlib.rglob("*.ext")
    → Busca archivos recursivamente en TODAS las subcarpetas
    → rglob("*") → todos los archivos y carpetas
    → rglob("*.py") → solo archivos .py en cualquier profundidad
    → glob("*.py") → solo en la carpeta actual (no recursivo)

  datetime.now().strftime("%Y-%m-%d")
    → Devuelve la fecha de hoy como string: "2025-07-17"
    → Útil para nombrar backups: "backup_2025-07-17.zip"
"""

import shutil
import datetime
from pathlib import Path


def hacer_backup_completo(carpeta_origen: str, carpeta_destino: str) -> str:
    """
    Comprime toda la carpeta origen en un .zip con fecha en el nombre.
    Devuelve la ruta del archivo creado.
    """
    origen = Path(carpeta_origen)
    destino = Path(carpeta_destino)

    if not origen.exists():
        raise FileNotFoundError(f"No existe la carpeta: {carpeta_origen}")

    # Crear la carpeta destino si no existe
    destino.mkdir(parents=True, exist_ok=True)

    # Nombre del backup con fecha: "documentos_2025-07-17"
    fecha = datetime.datetime.now().strftime("%Y-%m-%d")
    nombre_backup = f"{origen.name}_{fecha}"
    ruta_salida = destino / nombre_backup

    print(f"Comprimiendo '{origen}' → '{ruta_salida}.zip'...")

    # shutil.make_archive devuelve la ruta del archivo creado (con extensión)
    archivo_creado = shutil.make_archive(
        str(ruta_salida),  # nombre de salida (sin extensión)
        "zip",  # formato de compresión
        str(origen),  # carpeta a comprimir
    )

    tamaño_kb = Path(archivo_creado).stat().st_size / 1024
    print(f"✓ Backup creado: {archivo_creado} ({tamaño_kb:.1f} KB)")
    return archivo_creado


def hacer_backup_filtrado(carpeta_origen: str, carpeta_destino: str, extensiones: list):
    """
    Copia solo los archivos con las extensiones indicadas,
    respetando la estructura de subcarpetas.

    rglob() permite buscar de forma recursiva en todas las subcarpetas.
    """
    origen = Path(carpeta_origen)
    destino = Path(carpeta_destino)

    if not origen.exists():
        raise FileNotFoundError(f"No existe la carpeta: {carpeta_origen}")

    destino.mkdir(parents=True, exist_ok=True)
    copiados = 0

    # rglob("*") → busca TODOS los archivos en origen y subcarpetas
    for archivo in origen.rglob("*"):
        if not archivo.is_file():
            continue

        # Filtrar por extensión
        if archivo.suffix.lower() not in extensiones:
            continue

        # Reconstruir la ruta relativa para mantener estructura de carpetas
        ruta_relativa = archivo.relative_to(origen)
        archivo_destino = destino / ruta_relativa

        # Crear subcarpetas intermedias si son necesarias
        archivo_destino.parent.mkdir(parents=True, exist_ok=True)

        # copy2 preserva fecha de modificación y permisos (más completo que copy)
        shutil.copy2(archivo, archivo_destino)
        print(f"  ✓ {ruta_relativa}")
        copiados += 1

    print(f"\nBackup filtrado completado: {copiados} archivo(s) copiado(s)")


if __name__ == "__main__":
    import tempfile
    import os

    # Crear carpeta de prueba con archivos de distintos tipos
    with tempfile.TemporaryDirectory() as tmp_origen:
        origen = Path(tmp_origen)

        # Crear estructura de ejemplo
        (origen / "docs").mkdir()
        (origen / "scripts").mkdir()
        (origen / "README.md").write_text("# Mi Proyecto")
        (origen / "docs" / "manual.pdf").write_bytes(b"contenido pdf")
        (origen / "docs" / "notas.txt").write_text("Notas importantes")
        (origen / "scripts" / "util.py").write_text("print('hola')")
        (origen / "imagen.jpg").write_bytes(b"datos imagen")

        print("Archivos de prueba:")
        for f in origen.rglob("*"):
            if f.is_file():
                print(f"  {f.relative_to(origen)}")

        with tempfile.TemporaryDirectory() as tmp_destino:
            # Demo 1: backup completo en zip
            print("\n--- Demo 1: Backup completo (.zip) ---")
            hacer_backup_completo(tmp_origen, tmp_destino)

            # Demo 2: backup filtrado (solo .txt y .md)
            print("\n--- Demo 2: Solo archivos .txt y .md ---")
            destino_filtrado = os.path.join(tmp_destino, "filtrado")
            hacer_backup_filtrado(tmp_origen, destino_filtrado, [".txt", ".md"])
