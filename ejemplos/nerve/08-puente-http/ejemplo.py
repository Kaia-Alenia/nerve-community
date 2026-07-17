"""
Ejemplo: Servidor HTTP con FastAPI

Qué enseña este ejemplo:
  - Crear una aplicación básica de FastAPI.
  - Definir un modelo de datos (Pydantic) para recibir JSON.
  - Crear un endpoint (ruta) POST que lea esos datos.

Para tu reto (Puente HTTP para Nerve):
  Cuando el endpoint reciba los datos, deberás usar el cliente Nerve (app.state.nerve)
  para retransmitir la información hacia el hub de Nerve.
"""

from fastapi import FastAPI
from pydantic import BaseModel

# 1. Definir el modelo de los datos que esperamos recibir
# Esto asegura que quien envíe el POST, nos mande un JSON con un campo "mensaje"
class MensajePayload(BaseModel):
    mensaje: str

# 2. Inicializar la aplicación FastAPI
app = FastAPI()

# 3. Ruta GET básica para comprobar que funciona
@app.get("/")
def leer_raiz():
    return {"status": "Servidor funcionando"}

# 4. Ruta POST que será nuestro "puente"
# FastAPI automáticamente convierte el cuerpo del POST desde JSON hacia nuestro modelo
@app.post("/enviar")
def recibir_y_reenviar(payload: MensajePayload):
    # En la terminal veremos lo que llegó
    print(f"📩 Recibido por HTTP: {payload.mensaje}")
    
    # ¡Aquí es donde integrarías Nerve! 
    # Ejemplo: cliente_nerve.publicar("canal_http", payload.mensaje)
    
    return {"status": "ok", "recibido": payload.mensaje}

# NOTA: Para ejecutar esto se usa uvicorn desde la terminal:
# uvicorn ejemplo:app --reload
