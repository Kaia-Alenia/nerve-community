"""
Ejemplo: Leer un CSV real desde disco con csv.DictReader, filtrar y calcular sumas

Qué enseña este ejemplo:
  - Cómo abrir y leer un archivo CSV real con open() + csv.DictReader
  - Por qué DictReader (con D mayúscula) es mejor que reader simple
  - Cómo convertir strings a números para operar con ellos
  - Cómo filtrar filas y calcular sumas / promedios

Para tu reto (analizador de gastos):
  Aplica el mismo patrón para leer tu CSV de gastos
  (fecha, categoría, monto) y calcular totales por categoría.

Glosario de términos "raros":
  with open(...) as f — Abre un archivo y lo cierra automáticamente al terminar. 
                        'f' es una variable corta para 'file'.
  "r" o "w"           — Modos: "r" (read = leer), "w" (write = escribir).
  encoding="utf-8"    — Asegura que los acentos y caracteres especiales (ñ, á) se guarden bien.
  newline=""          — Evita que se escriban líneas en blanco extra entre filas en Windows.
  csv.DictReader      — Lee el CSV convirtiendo cada fila en un diccionario (usa D mayúscula).
  csv.reader          — Más básico: devuelve cada fila como lista de strings.
  float(valor)        — Convierte un texto como "1234.50" a un número decimal.

Archivo de ejemplo (empleados.csv):
  nombre,departamento,salario
  Ana García,Ingeniería,35000
  Luis Martínez,Marketing,28000
  Carmen López,Ingeniería,42000
  Pedro Sánchez,Marketing,31000
  Sofía Ramírez,Ingeniería,39000
"""

import csv
from pathlib import Path


def leer_empleados(ruta_csv: str) -> list:
    """
    Lee el CSV y devuelve una lista de diccionarios.
    Cada dict representa un empleado: {"nombre": ..., "departamento": ..., "salario": ...}
    """
    empleados = []
    ruta = Path(ruta_csv)

    if not ruta.exists():
        print(f"Archivo no encontrado: {ruta_csv}")
        return []

    # open() abre el archivo; newline="" es recomendado por la documentación de csv
    with open(ruta, "r", encoding="utf-8", newline="") as f:
        # DictReader usa la primera fila como nombres de columna automáticamente
        lector = csv.DictReader(f)
        for fila in lector:
            # Las filas de CSV son siempre strings — convertimos salario a float
            empleados.append({
                "nombre": fila["nombre"],
                "departamento": fila["departamento"],
                "salario": float(fila["salario"]),
            })

    return empleados


def reporte_por_departamento(empleados: list):
    """
    Calcula el total y promedio de salario por departamento.
    """
    totales = {}

    for emp in empleados:
        dept = emp["departamento"]
        if dept not in totales:
            totales[dept] = {"suma": 0.0, "cantidad": 0}
        totales[dept]["suma"] += emp["salario"]
        totales[dept]["cantidad"] += 1

    print("\n--- Reporte por departamento ---")
    for dept, datos in totales.items():
        promedio = datos["suma"] / datos["cantidad"]
        print(f"  {dept}: total=${datos['suma']:,.0f} | promedio=${promedio:,.0f} | empleados={datos['cantidad']}")


if __name__ == "__main__":
    # Crear archivo de ejemplo si no existe
    archivo = "empleados.csv"
    if not Path(archivo).exists():
        with open(archivo, "w", encoding="utf-8", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["nombre", "departamento", "salario"])
            writer.writerows([
                ["Ana García", "Ingeniería", 35000],
                ["Luis Martínez", "Marketing", 28000],
                ["Carmen López", "Ingeniería", 42000],
                ["Pedro Sánchez", "Marketing", 31000],
                ["Sofía Ramírez", "Ingeniería", 39000],
            ])
        print(f"Archivo '{archivo}' creado de ejemplo.")

    empleados = leer_empleados(archivo)
    print(f"\nSe leyeron {len(empleados)} empleados.")
    reporte_por_departamento(empleados)
