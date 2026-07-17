"""
Ejemplo: Extraer múltiples elementos de una página con requests + BeautifulSoup

Qué enseña este ejemplo:
  - Cómo hacer una petición HTTP GET con requests.get()
  - Qué significa raise_for_status() y para qué sirve
  - Cómo crear un objeto BeautifulSoup (el "parser" del HTML)
  - Cómo buscar TODOS los elementos de un tipo con find_all()
  - Cómo manejar errores de red con try/except

Para tu reto (web scraper):
  Aplica el mismo patrón para extraer datos de books.toscrape.com
  (título + precio de varios libros), que es una página pública
  diseñada específicamente para practicar scraping.

Glosario de términos "raros":
  requests     — Librería para pedir datos a internet (como lo hace tu navegador).
  BeautifulSoup— Librería que toma código HTML feo y te deja buscar dentro de él fácilmente.
  html.parser  — El motor que lee el HTML. Sin él, BeautifulSoup no sabe cómo leer el texto.
  raise_for_status() — Función que hace que el programa explote si la página no existe (Error 404).
  find_all()   — Busca TODOS los elementos que coincidan y devuelve una lista.
  find()       — Busca solo el PRIMER elemento que coincida.
  .text        — Extrae solo el texto limpio que ven los humanos (sin código HTML).
  .get("attr") — Extrae un atributo invisible, como el enlace (href) de un botón.
"""

import requests
from bs4 import BeautifulSoup

# Esta URL es una página de ejemplo hecha para practicar scraping
URL = "https://quotes.toscrape.com/"


def obtener_frases():
    try:
        # 1. Hacer la petición GET
        respuesta = requests.get(URL, timeout=5)

        # 2. raise_for_status() lanza una excepción si el servidor devolvió
        #    un error (ej: 404 Not Found, 500 Server Error)
        #    Sin esto, requests no falla aunque la página no exista
        respuesta.raise_for_status()

        # 3. Crear el objeto BeautifulSoup para navegar el HTML
        #    respuesta.text es el HTML de la página como texto plano
        soup = BeautifulSoup(respuesta.text, "html.parser")

        # 4. Buscar TODOS los elementos con class="quote"
        #    find_all devuelve una lista, aunque no encuentre nada (lista vacía)
        elementos = soup.find_all("div", class_="quote")

        print(f"Se encontraron {len(elementos)} frases en la página.\n")

        datos_extraidos = []
        for elemento in elementos:
            # .find() dentro de un elemento busca solo en ese bloque
            texto = elemento.find("span", class_="text").text
            autor = elemento.find("small", class_="author").text
            datos_extraidos.append({"texto": texto, "autor": autor})
            print(f'"{texto}"')
            print(f"  — {autor}\n")

        # 5. Guardar los datos en un archivo CSV (pieza final del rompecabezas)
        import csv
        with open("frases.csv", "w", encoding="utf-8", newline="") as f:
            # fieldnames define el nombre de las columnas (llaves del diccionario)
            escritor = csv.DictWriter(f, fieldnames=["texto", "autor"])
            escritor.writeheader()
            escritor.writerows(datos_extraidos)
            
        print("✓ Datos guardados exitosamente en 'frases.csv'")

    except requests.exceptions.ConnectionError:
        print("Error: No se pudo conectar. Revisa tu conexión a internet.")
    except requests.exceptions.Timeout:
        print("Error: La petición tardó demasiado (timeout).")
    except requests.exceptions.HTTPError as e:
        print(f"Error HTTP: {e}")


if __name__ == "__main__":
    obtener_frases()
