import time
from nerve import NexusClient

class ServidorCalculadora:
    def __init__(self):
        self.cliente = NexusClient()

    def atender_peticion(self, mensaje_crudo):
        remitente = mensaje_crudo.get("from")
        payload = mensaje_crudo.get("payload", {})
        
        accion = payload.get("accion")
        
        # Validamos que el mensaje es para nosotros y es una acción conocida
        if accion == "sumar":
            a = payload.get("a", 0)
            b = payload.get("b", 0)
            resultado = a + b
            
            print(f"🧮 Solicitud de suma recibida de '{remitente}': {a} + {b} = {resultado}")
            
            # Construimos la respuesta
            respuesta = {
                "accion": "respuesta_operacion",
                "resultado": resultado
            }
            
            # Mandamos la respuesta de vuelta a quien nos lo pidió
            print(f"Enviando resultado a '{remitente}'...")
            self.cliente.send(remitente, respuesta)

    def iniciar(self):
        self.cliente.connect("servidor_calculadora")
        print("✅ Servidor Calculadora en línea y esperando peticiones...")
        
        self.cliente.listen(self.atender_peticion)
        
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            print("\nApagando servidor...")
            self.cliente.disconnect()

if __name__ == "__main__":
    app = ServidorCalculadora()
    app.iniciar()
