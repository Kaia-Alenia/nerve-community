"""
Ejemplo: Calculadora de IMC para mascotas con float(input), round() y f-strings

Qué enseña este ejemplo:
  - Cómo convertir el input del usuario (siempre string) a float con float()
  - Cómo manejar el error si el usuario escribe letras en vez de números
  - Cómo usar round() y f-strings con decimales específicos
  - Cómo definir rangos numéricos y devolver una categoría

Para tu reto (calculadora de IMC humano):
  Aplica el mismo patrón: float(input()) para peso y altura,
  cálculo matemático, y comparación de rangos para categorizar el resultado.

Glosario:
  float(valor)     — convierte un string a número decimal. Lanza ValueError si falla.
  round(num, n)    — redondea 'num' a 'n' decimales. round(7.5678, 2) → 7.57
  f"{valor:.2f}"   — formatea un número en un f-string con exactamente 2 decimales
  f"{valor:.1f}"   — 1 decimal; f"{valor:.4f}" → 4 decimales, etc.
  ValueError       — error que lanza Python cuando intentas convertir un texto
                     no numérico a int o float. Ej: float("hola") → ValueError

Nota: El IMC de mascotas no es un estándar médico.
Este ejemplo es solo didáctico — usa datos inventados para no prescribir nada real.
"""


def calcular_imc_mascota(peso_kg: float, largo_cm: float) -> float:
    """
    Calcula un "índice de masa" simplificado para mascotas.
    Fórmula inventada solo para el ejemplo: peso / (largo en metros)^2
    """
    if largo_cm <= 0 or peso_kg <= 0:
        raise ValueError("El peso y el largo deben ser valores positivos.")
    largo_m = largo_cm / 100
    return peso_kg / (largo_m ** 2)


def categorizar_mascota(imc: float) -> str:
    """
    Clasifica el resultado en rangos (inventados para el ejemplo).
    """
    if imc < 15:
        return "Muy liviano para su tamaño"
    elif imc < 25:
        return "Proporción saludable"
    elif imc < 35:
        return "Un poco pesado para su tamaño"
    else:
        return "Muy pesado para su tamaño"


def pedir_float(mensaje: str) -> float:
    """
    Pide un número al usuario en loop hasta que ingrese algo válido.
    Demuestra el patrón try/except para validar inputs numéricos.
    """
    while True:
        entrada = input(mensaje).strip()
        try:
            # float() intentará convertir el string a decimal
            valor = float(entrada)
            if valor <= 0:
                print("El valor debe ser mayor a cero.")
                continue
            return valor
        except ValueError:
            # Si el usuario escribe "gato" o "12a", float() lanza ValueError
            print(f"'{entrada}' no es un número válido. Intenta de nuevo.")


def main():
    print("=== Calculadora de proporción peso/tamaño para mascotas ===")
    print("(Solo para práctica — no es un indicador médico veterinario real)\n")

    nombre = input("Nombre de tu mascota: ").strip() or "tu mascota"

    # Usamos nuestra función de input seguro que valida el tipo
    peso = pedir_float("Peso en kg (ej: 4.5): ")
    largo = pedir_float("Largo de hocico a cola en cm (ej: 60): ")

    try:
        imc = calcular_imc_mascota(peso, largo)
        categoria = categorizar_mascota(imc)

        # f-string con .2f → siempre muestra exactamente 2 decimales
        print(f"\nResultado para {nombre}:")
        print(f"  Peso: {peso} kg | Largo: {largo} cm")
        print(f"  Índice calculado: {imc:.2f}")
        print(f"  Categoría: {categoria}")

    except ValueError as e:
        print(f"Error en el cálculo: {e}")


if __name__ == "__main__":
    main()
