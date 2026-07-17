import requests
from bs4 import BeautifulSoup

# URL de ejemplo pública y permitida para pruebas
URL = "https://example.com"

try:
    # 1. Hacer una petición GET a la URL
    respuesta = requests.get(URL, timeout=5)

    # 2. Verificar que la petición fue exitosa (código 200)
    respuesta.raise_for_status()

    # 3. Parsear el contenido HTML con BeautifulSoup
    soup = BeautifulSoup(respuesta.text, "html.parser")

    # 4. Extraer información (por ejemplo, el título de la página)
    titulo = soup.title.string if soup.title else "Sin título"
    print(f"Título de la página: {titulo}")

except requests.exceptions.RequestException as e:
    # Manejo de errores de red (ej. sin internet, URL no existe)
    print(f"Error de conexión: {e}")
