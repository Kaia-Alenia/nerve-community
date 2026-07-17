import json
import os

ARCHIVO = "pepe.json"

datos = {
"nombre": "Alejandro Mtz",
"ciudad": "Queretaro",
"sistema": "Linux"

}

with open(ARCHIVO, "w", encoding="utf-8") as f:
    json.dump(datos, f, indent=4)
    print(f"Los datos se guardaron en {ARCHIVO}")

if os.path.exists(ARCHIVO):
    with open(ARCHIVO, "r", encoding="utf-8") as f:
        datos_cargados = json.load(f)
        print("Datos leidos:",  datos_cargados)
        print("Datos:", datos_cargados["nombre"], datos_cargados["ciudad"], datos_cargados["sistema"])
