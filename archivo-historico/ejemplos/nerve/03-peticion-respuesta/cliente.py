import time
from nerve import NexusClient


class ClientePeticion:
    def __init__(self):
        self.cliente = NexusClient()
        self.respuesta_recibida = None

    def manejar_respuesta(self, mensaje_crudo):
        # Filtramos para procesar solo los mensajes dirigidos a nosotros con un tipo esperado
        payload = mensaje_crudo.get("payload", {})
        accion = payload.get("accion")

        if accion == "respuesta_operacion":
            self.respuesta_recibida = payload.get("resultado")
            print(
                f"✅ ¡El servidor respondió! El resultado es: {self.respuesta_recibida}"
            )

    def iniciar(self):
        self.cliente.connect("cliente_calculadora")
        self.cliente.listen(self.manejar_respuesta)

        print("Enviando petición de suma al servidor (5 + 7)...")
        # Mandamos un payload estructurado pidiendo algo específico
        peticion = {"accion": "sumar", "a": 5, "b": 7}
        self.cliente.send("servidor_calculadora", peticion)

        # Esperamos hasta que el servidor nos conteste
        tiempo_espera = 0
        while self.respuesta_recibida is None and tiempo_espera < 5:
            print("⏳ Esperando respuesta...")
            time.sleep(1)
            tiempo_espera += 1

        if self.respuesta_recibida is None:
            print("❌ Tiempo de espera agotado. El servidor no contestó.")

        self.cliente.disconnect()


if __name__ == "__main__":
    app = ClientePeticion()
    app.iniciar()
