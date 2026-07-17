import time
from nerve import NexusClient

def procesar_mensaje(mensaje_crudo):
    # El servidor nos entrega el mensaje completo. Lo extraemos.
    print(f" ¡Mensaje recibido!: {mensaje_crudo}")
    
    # Podemos extraer el payload original si queremos
    payload = mensaje_crudo.get("payload", {})
    if "texto" in payload:
        print(f"Texto extraído: {payload['texto']}")

def main():
    print("Iniciando receptor...")
    cliente = NexusClient()
    
    # Nos conectamos como "receptor_01"
    cliente.connect("receptor_01")
    print("✅ Receptor conectado. Esperando mensajes...")
    
    # Registramos la función que se llamará al recibir mensajes
    cliente.listen(procesar_mensaje)
    
    try:
        # Mantenemos el programa vivo para escuchar
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nSaliendo...")
        cliente.disconnect()

if __name__ == "__main__":
    main()
