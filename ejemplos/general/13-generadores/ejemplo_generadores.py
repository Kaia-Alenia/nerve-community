"""
Ejemplo: Leer un archivo grande línea a línea con yield (generadores)

Qué enseña este ejemplo:
  - Qué es un generador y por qué ahorra memoria en archivos grandes
  - La diferencia entre yield y return
  - Cómo crear un archivo de prueba grande y procesarlo sin cargarlo completo
  - Cómo usar next() y for directamente sobre un generador

Para tu reto (lector de archivos gigantes):
  Aplica el mismo patrón: una función generadora que haga yield línea a línea.
  Luego usa el generador para procesar (contar, buscar, filtrar) sin listas.

Glosario:
  yield         — como return, pero pausa la función en vez de terminarla.
                  La próxima vez que se pida un valor, continúa desde donde pausó.
                  Convierte automáticamente la función en un generador.

  generador     — objeto que produce valores uno a uno, bajo demanda.
                  No calcula todos los valores de una vez (perezoso = lazy).
                  Ventaja: si el archivo tiene 10 GB, solo una línea ocupa
                  memoria a la vez.

  next(gen)     — pide el siguiente valor del generador. Lanza StopIteration
                  cuando se agotan los valores.

  for x in gen  — forma más cómoda de consumir un generador (maneja StopIteration)

  Diferencia clave:
    Con lista:   lineas = archivo.readlines()  → carga TODO en RAM
    Con yield:   for linea in leer_lineas(archivo) → una línea a la vez en RAM
"""

from pathlib import Path


def leer_lineas(ruta_archivo: str):
    """
    Generador que entrega una línea a la vez del archivo.
    El archivo nunca se carga completo en memoria.
    """
    ruta = Path(ruta_archivo)
    if not ruta.exists():
        print(f"Error: '{ruta_archivo}' no existe.")
        return  # En un generador, return sin valor termina la iteración

    with open(ruta, "r", encoding="utf-8") as f:
        for linea in f:
            # yield pausa aquí y entrega la línea al que llamó al generador
            # La próxima vez que se pida un valor, el loop continúa
            yield linea.rstrip("\n")  # eliminamos el salto de línea


def contar_lineas(ruta_archivo: str) -> int:
    """Cuenta líneas sin cargar el archivo completo."""
    return sum(1 for _ in leer_lineas(ruta_archivo))


def buscar_palabra(ruta_archivo: str, palabra: str) -> list:
    """
    Devuelve los números de línea donde aparece la palabra.
    Solo procesa una línea a la vez gracias al generador.
    """
    resultados = []
    for numero, linea in enumerate(leer_lineas(ruta_archivo), start=1):
        if palabra.lower() in linea.lower():
            resultados.append((numero, linea))
    return resultados


def crear_archivo_prueba(ruta: str, num_lineas: int = 100_000):
    """Crea un archivo grande para probar el generador."""
    with open(ruta, "w", encoding="utf-8") as f:
        for i in range(1, num_lineas + 1):
            if i % 5_000 == 0:
                f.write(f"Línea especial número {i} — contiene la palabra CLAVE\n")
            else:
                f.write(f"Esta es la línea número {i} del archivo de prueba\n")
    print(f"✓ Archivo creado: {ruta} ({num_lineas:,} líneas)")


if __name__ == "__main__":
    ARCHIVO = "archivo_grande.txt"

    # Crear el archivo de prueba
    crear_archivo_prueba(ARCHIVO, num_lineas=100_000)

    # Contar sin cargar todo en memoria
    total = contar_lineas(ARCHIVO)
    print(f"Total de líneas: {total:,}\n")

    # Buscar las líneas que contienen "CLAVE"
    print("Buscando líneas con 'CLAVE'...")
    encontradas = buscar_palabra(ARCHIVO, "CLAVE")
    print(f"Se encontraron {len(encontradas)} coincidencias:")
    for num, linea in encontradas[:3]:  # Mostramos solo las primeras 3
        print(f"  Línea {num:,}: {linea}")

    # Demostrar next() manualmente
    print("\nUsando next() manualmente en el generador:")
    gen = leer_lineas(ARCHIVO)
    print(f"  1er valor: {next(gen)}")
    print(f"  2do valor: {next(gen)}")
    print(f"  3er valor: {next(gen)}")

    # Limpiar
    Path(ARCHIVO).unlink()
    print(f"\n✓ Archivo '{ARCHIVO}' eliminado.")
