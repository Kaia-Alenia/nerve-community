import pandas as pd
from pathlib import Path


def validar_ruta_csv(ruta):
    try:
        clean_path = ruta.strip("'\"")
        path = Path(clean_path)

        if path.is_file():
            return True
        else:
            raise FileNotFoundError(f"Archivo no encontrado en la ruta: {path}")
    except Exception as e:
        raise e


def validar_contenido_csv(ruta):
    try:
        df = pd.read_csv(ruta)
        required_columns = ["id", "titulo", "description", "estado"]

        if all(column in df.columns for column in required_columns):
            return True
        else:
            raise ValueError(
                f"El archivo CSV no contiene la estructura requerida: {required_columns}"
            )
    except Exception as e:
        raise e
