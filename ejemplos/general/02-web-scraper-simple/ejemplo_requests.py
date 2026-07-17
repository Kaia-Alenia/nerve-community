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

Glosario de términos:
  requests     — librería para hacer peticiones HTTP (GET, POST, etc.)
  BeautifulSoup— librería para navegar y buscar dentro de HTML/XML
  html.parser  — el motor de Python que interpreta el texto HTML
                 (alternativa: lxml, más rápido pero requiere instalación)
  find_all()   — busca TODOS los elementos que coincidan con el selector
  find()       — busca solo el PRIMERO que coincida
  .text        — extrae el texto dentro de una etiqueta HTML (sin las etiquetas)
  .get("attr") — extrae el valor de un atributo HTML (ej: href, src, class)
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

        for elemento in elementos:
            # .find() dentro de un elemento busca solo en ese bloque
            texto = elemento.find("span", class_="text").text
            autor = elemento.find("small", class_="author").text
            print(f'"{texto}"')
            print(f"  — {autor}\n")

    except requests.exceptions.ConnectionError:
        print("Error: No se pudo conectar. Revisa tu conexión a internet.")
    except requests.exceptions.Timeout:
        print("Error: La petición tardó demasiado (timeout).")
    except requests.exceptions.HTTPError as e:
        print(f"Error HTTP: {e}")


if __name__ == "__main__":
    obtener_frases()
