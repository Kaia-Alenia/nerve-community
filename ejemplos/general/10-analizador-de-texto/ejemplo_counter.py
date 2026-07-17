"""
Ejemplo: Analizar un párrafo real — palabras únicas, frecuencia, estadísticas

Qué enseña este ejemplo:
  - Cómo limpiar y tokenizar texto con split() y lower()
  - Cómo eliminar puntuación con str.translate() + string.punctuation
  - Cómo usar Counter para contar frecuencias
  - Cómo filtrar stopwords (palabras vacías) de una lista
  - Cómo combinar todo para un análisis de texto realista

Para tu reto (analizador de texto):
  Aplica el mismo patrón para leer un archivo .txt,
  y reportar: líneas, palabras, promedio por línea,
  y las 10 palabras más frecuentes (sin stopwords).

Glosario:
  split()          — divide un string por espacios y devuelve una lista de palabras
                     "hola mundo".split() → ["hola", "mundo"]
  lower()          — convierte todo a minúsculas (para comparar sin importar case)
  str.translate()  — reemplaza o elimina caracteres según una tabla de mapeo
  str.maketrans()  — construye la tabla para translate()
                     str.maketrans("", "", ".,!?") → elimina esos caracteres
  Counter(lista)   — crea un diccionario donde la clave es el elemento
                     y el valor es cuántas veces aparece
  .most_common(n)  — devuelve los N elementos más frecuentes como lista de tuplas
  set()            — colección sin duplicados; útil para palabras únicas
"""

import string
from collections import Counter

# Palabras vacías en español (no aportan significado, no queremos contarlas)
STOPWORDS = {
    "el", "la", "los", "las", "un", "una", "unos", "unas",
    "de", "en", "a", "y", "o", "que", "con", "por", "para",
    "del", "al", "se", "es", "son", "su", "sus", "lo", "le",
    "más", "pero", "como", "si", "no", "ya", "fue", "era",
    "hay", "ser", "me", "te", "nos", "les",
}


def limpiar_palabra(palabra: str) -> str:
    """
    Convierte a minúsculas y elimina puntuación de una palabra.
    str.maketrans("", "", chars) crea una tabla que borra todos los chars.
    """
    tabla = str.maketrans("", "", string.punctuation + "¡¿«»")
    return palabra.lower().translate(tabla)


def analizar_texto(texto: str) -> dict:
    """
    Analiza el texto y devuelve estadísticas en un diccionario.
    """
    # 1. Separar en palabras y limpiar cada una
    palabras_crudas = texto.split()
    palabras_limpias = [limpiar_palabra(p) for p in palabras_crudas]

    # 2. Filtrar palabras vacías y palabras de 1 carácter
    palabras_validas = [
        p for p in palabras_limpias
        if p and len(p) > 1 and p not in STOPWORDS
    ]

    # 3. Contar frecuencias con Counter
    conteo = Counter(palabras_validas)

    # 4. Palabras únicas (sin repetir)
    unicas = set(palabras_validas)

    return {
        "total_palabras": len(palabras_crudas),
        "palabras_unicas": len(unicas),
        "palabras_validas": len(palabras_validas),
        "top_5": conteo.most_common(5),
        "mas_frecuente": conteo.most_common(1)[0] if conteo else None,
    }


def imprimir_reporte(stats: dict):
    print("\n--- Reporte de Análisis de Texto ---")
    print(f"  Total de palabras:     {stats['total_palabras']}")
    print(f"  Palabras únicas:       {stats['palabras_unicas']}")
    print(f"  (Excluyendo stopwords y puntuación)")

    if stats["mas_frecuente"]:
        palabra, veces = stats["mas_frecuente"]
        print(f"  Palabra más frecuente: '{palabra}' ({veces} veces)")

    print("\n  Top 5 palabras más usadas:")
    for palabra, veces in stats["top_5"]:
        barra = "█" * veces
        print(f"    {palabra:<15} {barra} ({veces})")


if __name__ == "__main__":
    TEXTO_EJEMPLO = """
    Python es un lenguaje de programación poderoso y fácil de aprender.
    Python tiene estructuras de datos eficientes y un enfoque simple pero efectivo
    hacia la programación orientada a objetos. La elegante sintaxis de Python y su
    tipado dinámico, junto con su naturaleza interpretada, hacen de Python un
    lenguaje ideal para scripting y desarrollo rápido de aplicaciones en muchas
    áreas y en muchas plataformas distintas.
    """

    print("Texto a analizar:")
    print(TEXTO_EJEMPLO)

    stats = analizar_texto(TEXTO_EJEMPLO)
    imprimir_reporte(stats)
