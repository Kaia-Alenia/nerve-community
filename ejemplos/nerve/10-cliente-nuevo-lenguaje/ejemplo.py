/**
 * Ejemplo: Cliente de Socket TCP en Python
 * 
 * Qué enseña este ejemplo:
 *   - Conectarse a un servidor a través de una dirección IP y un puerto usando sockets.
 *   - Codificar un JSON a bytes y enviarlo.
 *   - Esperar y decodificar la respuesta del servidor.
 * 
 * Para tu reto (Nuevo Cliente Nerve):
 *   En un cliente Nerve real, querrás mantener este socket abierto (persistencia) 
 *   y ejecutar un bucle (loop) en un hilo (thread) separado para estar siempre
 *   escuchando los nuevos mensajes que el Hub envía, disparando callbacks o
 *   eventos a tu aplicación.
 */

import socket
import json

def main():
    host = "127.0.0.1"
    puerto = 5000

    print(f"🔄 Conectando a {host}:{puerto}...")

    # 1. Crear el socket TCP (AF_INET para IPv4, SOCK_STREAM para TCP)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            # 2. Conectarse al servidor
            s.connect((host, puerto))
            print("✅ Conectado exitosamente")

            # 3. Preparar el payload simulando un mensaje Nerve
            payload = {
                "tipo": "publicar",
                "canal": "test",
                "contenido": "Hola desde el nuevo cliente Python!"
            }

            # 4. Enviar los datos. Deben convertirse de Diccionario -> JSON String -> Bytes
            datos_str = json.dumps(payload) + "\n"
            s.sendall(datos_str.encode("utf-8"))
            print(f"⬆️ Enviado: {datos_str.strip()}")

            # 5. Esperar la respuesta (leyendo hasta 1024 bytes)
            datos_recibidos = s.recv(1024)
            if datos_recibidos:
                # Decodificar de Bytes -> String
                respuesta = datos_recibidos.decode("utf-8").strip()
                print(f"⬇️ Recibido: {respuesta}")
            else:
                print("⚠️ El servidor cerró la conexión sin responder.")

        except ConnectionRefusedError:
            print("❌ No se pudo conectar. ¿Está el servidor encendido?")
        except Exception as e:
            print(f"❌ Error inesperado: {e}")

if __name__ == "__main__":
    main()
