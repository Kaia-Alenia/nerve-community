import time
from nerve import NexusClient


def main():
    print("Iniciando publicador (estación de radio)...")
    cliente = NexusClient()
    cliente.connect("publicador_noticias")
    print("✅ Publicador conectado al Hub.")

    contador = 1
    try:
        while True:
            noticia = {
                "canal": "noticias_tech",
                "titular": f"Noticia #{contador}: Nerve Hub funciona genial",
                "timestamp": time.time(),
            }

            # Usamos broadcast para enviarlo a todos los nodos conectados
            print(f" Transmitiendo (broadcast): {noticia['titular']}")
            cliente.broadcast(noticia)

            contador += 1
            time.sleep(3)  # Transmite cada 3 segundos

    except KeyboardInterrupt:
        print("\nApagando publicador...")
        cliente.disconnect()


if __name__ == "__main__":
    main()
