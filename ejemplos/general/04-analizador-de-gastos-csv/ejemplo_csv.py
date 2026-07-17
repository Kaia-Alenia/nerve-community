import csv
import io

# Simulamos el contenido de un archivo CSV en texto plano para el ejemplo
contenido_csv = """nombre,edad,ciudad
Ana,28,Madrid
Luis,35,Bogotá
Carmen,22,Lima"""

# io.StringIO permite leer este texto como si fuera un archivo real
archivo_simulado = io.StringIO(contenido_csv)

# 1. Leer el CSV usando DictReader (convierte cada fila en un diccionario)
lector = csv.DictReader(archivo_simulado)

print("Datos extraídos del CSV:")
# 2. Iterar sobre cada fila
for fila in lector:
    # Podemos acceder a los datos usando los nombres de las columnas
    nombre = fila["nombre"]
    edad = int(fila["edad"])  # Convertimos a entero
    print(f"- {nombre} tiene {edad} años y vive en {fila['ciudad']}")
