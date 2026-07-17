import json
from pathlib import Path

def guardar_puntaje(puntaje, ruta_archivo="score.json"):
    """
    Guarda el puntaje más alto en un archivo JSON.
    """
    datos = {
        "juego": "Adivina el Número",
        "record_actual": puntaje
    }
    # Abrimos el archivo en modo escritura (w)
    with open(ruta_archivo, "w", encoding="utf-8") as f:
        # json.dump serializa el diccionario a formato JSON y lo guarda.
        # indent=4 lo hace fácil de leer para los humanos.
        json.dump(datos, f, indent=4)
    print(f"Puntaje de {puntaje} guardado correctamente.")

def cargar_puntaje(ruta_archivo="score.json"):
    """
    Carga el puntaje más alto desde un archivo JSON.
    """
    archivo = Path(ruta_archivo)
    
    if not archivo.exists():
        print("No hay récord anterior.")
        return 0
        
    # Abrimos el archivo en modo lectura (r)
    with open(ruta_archivo, "r", encoding="utf-8") as f:
        # json.load parsea el archivo de texto y lo convierte a dict
        datos = json.load(f)
        return datos["record_actual"]

if __name__ == "__main__":
    print("--- Intentando cargar puntaje anterior ---")
    record = cargar_puntaje()
    print(f"Récord actual: {record}")
    
    nuevo_record = record + 150
    print("\n--- Guardando nuevo puntaje ---")
    guardar_puntaje(nuevo_record)
