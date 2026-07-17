"""
Ejemplo: Construir un PIN bancario seguro con secrets + string

Qué enseña este ejemplo:
  - Cuándo usar secrets en lugar de random (y por qué importa)
  - Cómo usar string.digits, string.ascii_letters, string.punctuation
  - Cómo construir una cadena aleatoria con join() + secrets.choice()
  - Cómo garantizar que el resultado incluya al menos un carácter de cada tipo

Para tu reto (generador de contraseñas):
  Aplica el mismo patrón: construye el pool de caracteres según los
  parámetros del usuario (longitud, símbolos sí/no, mayúsculas sí/no),
  y usa secrets.choice() en un loop para construir la contraseña.

Glosario de términos "raros":
  secrets          — módulo para aleatoriedad segura (usa fuentes del sistema).
  random           — módulo de aleatoriedad predecible (NO usar para contraseñas).
  string.digits    — contiene "0123456789".
  string.ascii...  — contiene letras ("abcdefghijklmnopqrstuvwxyz", etc).
  string.punctuation — todos los símbolos: !"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~
  "".join(lista)   — une una lista de caracteres en un solo texto (ej: "a" + "b" = "ab").
  _ (guion bajo)   — se usa en `for _ in range()` cuando vas a repetir algo N veces 
                     pero no necesitas usar el número de la vuelta actual.
"""

import secrets
import string


def generar_pin(longitud: int = 6, solo_numeros: bool = True) -> str:
    """
    Genera un PIN seguro.
    Si solo_numeros=True, usa únicamente dígitos (PIN bancario clásico).
    Si solo_numeros=False, mezcla letras y dígitos (PIN alfanumérico).
    """
    if solo_numeros:
        pool = string.digits  # "0123456789"
    else:
        pool = string.ascii_uppercase + string.digits

    # join() + list comprehension: llama secrets.choice(pool) N veces
    # y une todos los caracteres resultantes en un string
    pin = "".join(secrets.choice(pool) for _ in range(longitud))
    return pin


def generar_pin_garantizado(longitud: int = 8) -> str:
    """
    Genera un PIN que GARANTIZA tener al menos:
      - 1 letra mayúscula
      - 1 dígito
      - 1 símbolo

    Técnica: generar una de cada tipo obligatorio, luego rellenar
    el resto con caracteres del pool completo y mezclar.
    """
    if longitud < 3:
        raise ValueError("La longitud mínima para un PIN garantizado es 3.")

    pool_completo = string.ascii_uppercase + string.digits + string.punctuation

    # 1. Garantizar al menos uno de cada tipo requerido
    obligatorios = [
        secrets.choice(string.ascii_uppercase),
        secrets.choice(string.digits),
        secrets.choice(string.punctuation),
    ]

    # 2. Rellenar el resto con caracteres aleatorios del pool completo
    relleno = [secrets.choice(pool_completo) for _ in range(longitud - 3)]

    # 3. Unir todo y mezclar (secrets.SystemRandom para barajar de forma segura)
    caracteres = obligatorios + relleno
    secrets.SystemRandom().shuffle(caracteres)

    return "".join(caracteres)


if __name__ == "__main__":
    print("=== Generador de PINs seguros ===\n")

    print("PINs numéricos (6 dígitos):")
    for _ in range(3):
        print(f"  {generar_pin(6, solo_numeros=True)}")

    print("\nPINs alfanuméricos (8 caracteres):")
    for _ in range(3):
        print(f"  {generar_pin(8, solo_numeros=False)}")

    print("\nPINs con garantía (letra + dígito + símbolo, 10 chars):")
    for _ in range(3):
        print(f"  {generar_pin_garantizado(10)}")
