import shutil
import os
from pathlib import Path

def crear_archivo_zip(carpeta_a_comprimir, nombre_archivo_salida):
    """
    Comprime todo el contenido de una carpeta en un archivo .zip.
    """
    ruta = Path(carpeta_a_comprimir)
    
    if not ruta.exists() or not ruta.is_dir():
        print(f"Error: La carpeta '{carpeta_a_comprimir}' no existe o no es un directorio.")
        return

    print(f"Comprimiendo la carpeta '{carpeta_a_comprimir}'...")
    
    # shutil.make_archive(nombre_salida, formato, carpeta_origen)
    # Crea un archivo .zip con el contenido de la carpeta de origen.
    shutil.make_archive(nombre_archivo_salida, 'zip', ruta)
    
    print(f"¡Listo! Se creó el archivo: {nombre_archivo_salida}.zip")

if __name__ == "__main__":
    # Vamos a crear una carpeta de prueba temporal para comprimirla
    carpeta_prueba = "datos_temporales"
    os.makedirs(carpeta_prueba, exist_ok=True)
    
    # Creamos un archivo vacío dentro para que tenga contenido
    with open(os.path.join(carpeta_prueba, "nota.txt"), "w") as f:
        f.write("Este es un archivo de prueba.")
        
    crear_archivo_zip(carpeta_prueba, "mi_backup")
    
    print("Puedes revisar que se ha creado 'mi_backup.zip' en este directorio.")
