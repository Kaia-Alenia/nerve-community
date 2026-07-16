## Peticiones HTTP (Requests)

**¿Qué muestra este ejemplo?**
Cómo hacer peticiones HTTP (GET, POST) a APIs o páginas web externas usando la librería externa `requests`, manejando posibles errores de red o códigos de estado fallidos.

**¿Por qué es útil?**
Es la base para consumir cualquier API REST (como consultar el clima, leer mensajes, o enviar notificaciones) y para hacer scraping de sitios web.

**Cómo correrlo**
- Dependencias necesarias: `pip install requests`
- Comando para ejecutarlo: `python ejemplo_requests.py`

**¿Qué retos usan esta base?**
- [#14 Python General 02 — Web scraper simple](https://github.com/Kaia-Alenia/nerve-community/issues/14)

**Nota para principiantes**
Siempre revisa el `response.status_code` o usa `response.raise_for_status()` antes de intentar leer los datos; asumir que una petición web siempre será exitosa causará que tu programa se cierre inesperadamente si no hay internet o el servidor falla.