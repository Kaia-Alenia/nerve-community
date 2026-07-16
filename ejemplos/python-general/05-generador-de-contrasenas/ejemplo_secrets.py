import random
import secrets
import string

opciones = ["Rojo", "Verde", "Azul", "Amarillo"]
alfabeto = string.ascii_letters + string.digits

# 1. Uso de random (NO seguro para criptografía o contraseñas)
# random usa una semilla predecible. Útil para juegos o simulaciones.
color_azar = random.choice(opciones)
print(f"Color al azar (random): {color_azar}")

# 2. Uso de secrets (Seguro, diseñado para contraseñas y tokens)
# secrets usa fuentes de aleatoriedad del sistema operativo.
color_seguro = secrets.choice(opciones)
print(f"Color al azar (secrets): {color_seguro}")

# 3. Ejemplo común: generar un token aleatorio seguro de 8 caracteres
token = "".join(secrets.choice(alfabeto) for _ in range(8))
print(f"Token seguro generado: {token}")
