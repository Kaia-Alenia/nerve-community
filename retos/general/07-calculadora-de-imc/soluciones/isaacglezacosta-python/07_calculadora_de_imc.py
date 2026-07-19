"""
Calculadora de índice de masa corporal (IMC)
Este programa solicita al usuario su peso (kg) y altura (m), calcula su IMC
y lo categoriza según las siguientes categorías:
    - Bajo peso: IMC < 18.5
    - Peso normal: 18.5 <= IMC < 25
    - Sobrepeso: 25 <= IMC < 30
    - Obesidad: IMC >= 30
"""


def calcular_imc(peso: float, altura: float) -> float:
    """
    Calcula el índice de masa corporal.
    Fórmula: IMC = peso (kg) / altura^2 (m)
    """ 
    return peso / altura ** 2


def categorizar_imc(imc: float) -> str:
    """
    Categoriza el IMC del usuario.
    """

    if imc > 30.0:
        return "Obesidad"
    elif imc > 25.0:
        return "Sobrepeso"
    elif imc > 18.5:
        return "Peso normal"
    else:
        return "Bajo peso"


def pedir_float(mensaje: str) -> float:
    """
    Solicita al usuario un número flotante y maneja errores de entrada.
    """
    while True:
        entrada = input(mensaje).strip()
        try:
            valor = float(entrada)
            if valor <= 0:
                print("Por favor, ingrese un número mayor que cero.")
                continue
            else:
                return valor
        except ValueError:
            print("Por favor, ingrese un número válido.")


def main():
    print("=== Calculadora de índice de masa corporal ===")
    print("¡Bienvenido a la calculadora de IMC!\n")

    nombre = input("Ingrese su nombre: ").strip()
    peso = pedir_float("Ingrese su peso en kg (ej. 70): ")
    altura = pedir_float("Ingrese su altura en m (ej. 1.75): ")

    try:
        imc = calcular_imc(peso, altura)
        categoria = categorizar_imc(imc)

        print(f"\nResultado para {nombre}:")
        print(f"Peso: {peso} kg | Altura: {altura:.2f} m")
        print(f"IMC calculado: {imc:.2f}")
        print(f"Categoría: {categoria}")

    except ValueError as e:
        print("Error en el cálculo.")
        print(e)


if __name__ == "__main__":
    main()