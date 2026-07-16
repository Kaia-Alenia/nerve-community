import time
import sys
from nerve import NexusClient

# Tomamos el nombre del suscriptor por argumento de consola, 
# para poder ejecutar varios distintos. 
# Si no hay argumento, le ponemos uno por defecto.
nombre_nodo = sys.argv[1] if len(sys.argv) > 1 else "suscriptor_default"

def al_recibir_noticia(mensaje_crudo):
    # En un patrón Pub-Sub usando 'broadcast', todos reciben el mensaje.
    # El trabajo del suscriptor es FILTRAR lo que le interesa.
    payload = mensaje_crudo.get("payload", {})
    
    if payload.get("canal") == "noticias_tech":
        titular = payload.get("titular", "Sin titular")
        print(f"[{nombre_nodo}] 📰 Nueva noticia interceptada: {titular}")

def main():
    print(f"Iniciando {nombre_nodo}...")
    cliente = NexusClient()
    cliente.connect(nombre_nodo)
    print(f"✅ {nombre_nodo} conectado. Escuchando el canal 'noticias_tech'...")
    
    cliente.listen(al_recibir_noticia)
    
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print(f"\nApagando {nombre_nodo}...")
        cliente.disconnect()

if __name__ == "__main__":
    main()
