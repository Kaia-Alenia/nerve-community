import json
import os

# Archivo donde guardaremos nuestros datos
ARCHIVO = "datos_ejemplo.json"

# Datos de prueba (un diccionario)
datos = {
    "nombre": "Kaia",
    "version": 1.0,
    "activo": True
}

# 1. Guardar (escribir) datos en un archivo JSON
with open(ARCHIVO, "w", encoding="utf-8") as f:
    # json.dump toma los datos y el archivo donde escribirlos
    json.dump(datos, f, indent=4)
    print(f"Datos guardados en {ARCHIVO}")

# 2. Leer datos desde un archivo JSON
if os.path.exists(ARCHIVO):
    with open(ARCHIVO, "r", encoding="utf-8") as f:
        # json.load lee el archivo y lo convierte de nuevo a un diccionario
        datos_cargados = json.load(f)
        print("Datos leídos:", datos_cargados)
        print("Nombre:", datos_cargados["nombre"])
