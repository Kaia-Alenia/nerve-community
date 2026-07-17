"""
Ejemplo: Mini juego "adivina el color" con random.choice, loop y conteo de intentos

Qué enseña este ejemplo:
  - Cómo usar random.choice() para seleccionar un elemento al azar de una lista
  - Cómo estructurar el loop de intentos con while + contador
  - Cómo dar pistas simples (mayor/menor en números, aquí: letra inicial)
  - Cómo manejar input no válido con validación condicional

Para tu reto (adivina el número):
  Aplica el mismo patrón de loop + contador + pistas,
  pero usa random.randint(1, 100) para generar un número
  y compara si el intento es mayor o menor al número secreto.

Glosario:
  random.choice(lista) — elige un elemento al azar de cualquier lista o string
  random.randint(a, b) — genera un entero al azar entre a y b (ambos incluidos)
  .lower()             — convierte un string a minúsculas (útil para comparar)
  .strip()             — elimina espacios al inicio y final del string
"""

import random

COLORES = ["rojo", "azul", "verde", "amarillo", "morado", "naranja"]
MAX_INTENTOS = 4


def jugar():
    # random.choice elige un color al azar de la lista
    color_secreto = random.choice(COLORES)
    intentos = 0

    print("=== Adivina el color ===")
    print(f"Tengo un color en mente. Tienes {MAX_INTENTOS} intentos.")
    print(f"Opciones posibles: {', '.join(COLORES)}\n")

    while intentos < MAX_INTENTOS:
        intento = input(f"Intento {intentos + 1}/{MAX_INTENTOS}: ").strip().lower()

        # Validar que el input sea uno de los colores válidos
        if intento not in COLORES:
            print(f"'{intento}' no es un color válido. Elige de la lista.\n")
            continue  # No contamos este como un intento fallido

        intentos += 1

        if intento == color_secreto:
            print(f"\n¡Correcto! Era '{color_secreto}'. Lo lograste en {intentos} intento(s).")
            return

        # Pista: comparar letra inicial (equivalente a mayor/menor en números)
        if intento[0] < color_secreto[0]:
            print(f"No es '{intento}'. El color secreto va después alfabéticamente.")
        else:
            print(f"No es '{intento}'. El color secreto va antes alfabéticamente.")
        print()

    print(f"\nSe acabaron los intentos. El color era '{color_secreto}'.")


if __name__ == "__main__":
    jugar()
