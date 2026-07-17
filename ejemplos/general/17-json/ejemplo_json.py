"""
Ejemplo: Leer configuraciones JSON/YAML con manejo de claves faltantes

Qué enseña este ejemplo:
  - Cómo leer un archivo JSON con json.load() + pathlib
  - Cómo manejar claves faltantes con .get() y KeyError
  - Cómo detectar automáticamente el formato del archivo (.json o .yaml)
  - Cómo devolver valores por defecto cuando el archivo no existe

Para tu reto (lector de configuraciones):
  Aplica el mismo patrón: detecta la extensión, usa json.load o yaml.safe_load,
  y maneja los casos de archivo inexistente o claves faltantes con valores por defecto.

Glosario:
  json.load(archivo)     — lee un archivo y devuelve dict/list de Python
  json.dump(datos, archivo, indent=4) — escribe dict/list como JSON en un archivo
  yaml.safe_load(archivo)— lee un archivo YAML y devuelve dict de Python
                           (usar safe_load, NO yaml.load — es más seguro)
  dict.get(clave, default) — devuelve el valor de la clave, o 'default' si no existe
                             Nunca lanza KeyError (a diferencia de dict[clave])
  dict.get("a", {}).get("b", valor) — acceso seguro a claves anidadas
  pathlib.Path.suffix    — extensión del archivo: ".json", ".yaml", ".yml"
  KeyError               — error que lanza Python al acceder a una clave inexistente
                           con dict[clave] (en vez de dict.get(clave))
"""

import json
from pathlib import Path

# pyyaml es un paquete externo: pip install pyyaml
# Solo se importa si el archivo es .yaml — no es obligatorio instalarlo
try:
    import yaml
    YAML_DISPONIBLE = True
except ImportError:
    YAML_DISPONIBLE = False


# Configuración por defecto (usada si el archivo no existe o faltan claves)
CONFIG_POR_DEFECTO = {
    "base_url": "http://localhost:8000",
    "timeout_seg": 30,
    "debug": False,
    "base_de_datos": {
        "host": "localhost",
        "puerto": 5432,
        "nombre": "mi_app",
    },
}


def cargar_config(ruta: str) -> dict:
    """
    Carga una configuración desde un archivo .json o .yaml.
    Si el archivo no existe, devuelve la configuración por defecto.
    Si faltan claves, las rellena con los valores por defecto.
    """
    archivo = Path(ruta)

    if not archivo.exists():
        print(f"Archivo '{ruta}' no encontrado. Usando configuración por defecto.")
        return CONFIG_POR_DEFECTO.copy()

    extension = archivo.suffix.lower()

    try:
        with open(archivo, "r", encoding="utf-8") as f:
            if extension == ".json":
                datos = json.load(f)
            elif extension in (".yaml", ".yml"):
                if not YAML_DISPONIBLE:
                    print("pyyaml no instalado. Instala con: pip install pyyaml")
                    return CONFIG_POR_DEFECTO.copy()
                datos = yaml.safe_load(f)
            else:
                print(f"Formato '{extension}' no soportado.")
                return CONFIG_POR_DEFECTO.copy()

        # Combinar con los defaults: claves faltantes usan el valor por defecto
        config_completa = CONFIG_POR_DEFECTO.copy()
        config_completa.update(datos)
        return config_completa

    except json.JSONDecodeError as e:
        print(f"Error al parsear JSON: {e}")
        return CONFIG_POR_DEFECTO.copy()


def acceder_configuracion(config: dict):
    """
    Demuestra cómo acceder a claves de forma segura.
    """
    print("\n--- Configuración cargada ---")

    # dict.get(clave, default) → NUNCA lanza KeyError
    url = config.get("base_url", "sin-url")
    timeout = config.get("timeout_seg", 30)
    debug = config.get("debug", False)

    print(f"  URL: {url}")
    print(f"  Timeout: {timeout}s")
    print(f"  Debug: {debug}")

    # Acceso anidado seguro con .get() encadenado
    db = config.get("base_de_datos", {})
    host_db = db.get("host", "desconocido")
    puerto_db = db.get("puerto", 5432)

    print(f"  Base de datos: {host_db}:{puerto_db}")

    # Contraste: acceso con [] → lanza KeyError si no existe
    try:
        _ = config["clave_que_no_existe"]
    except KeyError as e:
        print(f"\n  (Ejemplo de KeyError al usar config[{e}])")
        print("  Solución: usar config.get('clave_que_no_existe', valor_defecto)")


if __name__ == "__main__":
    # Demo 1: archivo inexistente → defaults
    print("=== Demo 1: Archivo inexistente ===")
    config1 = cargar_config("no_existe.json")
    acceder_configuracion(config1)

    # Demo 2: crear un JSON parcial y cargarlo
    print("\n=== Demo 2: JSON con solo algunas claves ===")
    config_parcial = {
        "base_url": "https://api.miempresa.com",
        "debug": True,
        # timeout_seg y base_de_datos faltan → usarán los defaults
    }
    with open("config_ejemplo.json", "w", encoding="utf-8") as f:
        json.dump(config_parcial, f, indent=4)
    print("Archivo 'config_ejemplo.json' creado con configuración parcial.")

    config2 = cargar_config("config_ejemplo.json")
    acceder_configuracion(config2)

    # Limpiar
    Path("config_ejemplo.json").unlink()
    print("\n✓ Archivo de prueba eliminado.")
