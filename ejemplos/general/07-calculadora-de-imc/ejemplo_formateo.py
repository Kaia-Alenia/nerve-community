def calcular_promedio(nota1: float, nota2: float, nota3: float) -> float:
    """
    Recibe múltiples parámetros y retorna el cálculo matemático.
    """
    suma_total = nota1 + nota2 + nota3
    return suma_total / 3


def categorizar_promedio(promedio: float) -> str:
    """
    Devuelve un string descriptivo basado en el valor.
    """
    if promedio >= 9.0:
        return "Excelente"
    elif promedio >= 7.0:
        return "Aprobado"
    else:
        return "Reprobado"


def main():
    print("--- Ejemplo: Calculadora de Promedio ---")

    # En un caso real, podrías usar inputs y validarlos.
    # Aquí usamos valores de ejemplo.
    n1 = 7.5
    n2 = 8.8
    n3 = 6.2

    promedio = calcular_promedio(n1, n2, n3)
    categoria = categorizar_promedio(promedio)

    # Usamos f-strings para formatear:
    # {promedio:.1f} redondeará a 1 decimal
    print(f"\nNotas: {n1}, {n2}, {n3}")
    print(f"El promedio es: {promedio:.1f} -> Categoría: {categoria}")


if __name__ == "__main__":
    main()
