import pandas as pd
from pathlib import Path


BASE_DIR = Path(__file__).parent.resolve()


def obtener_ruta_absoluta(ruta: str) -> Path:
    clean_path = ruta.strip("'\"")
    path = Path(clean_path)
    if not path.is_absolute():
        path = BASE_DIR / path
    return path


def validar_ruta_csv(ruta: str) -> str:
    path = obtener_ruta_absoluta(ruta)

    if path.is_file():
        return str(path)
    raise FileNotFoundError(f"Archivo no encontrado en la ruta: {path}")


def validar_contenido_csv(ruta: str) -> bool:
    # 2.- Leer la ruta ya limpia para validar su estructura
    df = pd.read_csv(ruta, encoding="utf-8")
    required_columns = ["id", "titulo", "description", "estado"]

    if all(column in df.columns for column in required_columns):
        return True

    raise ValueError(
        f"El archivo CSV no contiene la estructura requerida: {required_columns}"
    )
    
