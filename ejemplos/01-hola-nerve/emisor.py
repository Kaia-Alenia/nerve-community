import time
from nerve import NexusClient

def main():
    print("Iniciando emisor...")
    # 1. Crear el cliente de Nerve
    cliente = NexusClient()
    
    # 2. Conectarse al Hub con un identificador único
    cliente.connect("emisor_01")
    print("✅ Emisor conectado al Nerve Hub.")
    
    # Esperamos un momento para asegurar que el receptor esté listo
    time.sleep(1)
    
    # 3. Preparar el mensaje (payload) y enviarlo al receptor
    mensaje = {
        "texto": "¡Hola, Nerve!",
        "timestamp": time.time()
    }
    
    print("Enviando mensaje a 'receptor_01'...")
    cliente.send("receptor_01", mensaje)
    
    print("Mensaje enviado. Terminando emisor...")
    # Desconectamos el cliente para liberar recursos
    cliente.disconnect()

if __name__ == "__main__":
    main()
