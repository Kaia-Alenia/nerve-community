import random
import secrets

participantes = ["Ana", "Beto", "Carlos", "Diana"]

# 1. Uso de random (NO seguro para criptografía o contraseñas)
# random usa una semilla predecible. Útil para juegos o simulaciones.
ganador_azar = random.choice(participantes)
print(f"Ganador al azar (random): {ganador_azar}")

# 2. Uso de secrets (Seguro, diseñado para contraseñas y tokens)
# secrets usa fuentes de aleatoriedad del sistema operativo.
ganador_seguro = secrets.choice(participantes)
print(f"Ganador al azar (secrets): {ganador_seguro}")
