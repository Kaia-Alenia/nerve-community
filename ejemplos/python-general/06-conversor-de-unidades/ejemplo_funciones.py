def convertir_dolares_a_euros(dolares: float) -> float:
    """
    Función pura: recibe un valor, devuelve un valor modificado.
    No imprime nada, no pide inputs.
    """
    return dolares * 0.85  # tasa de ejemplo, no representa el valor real de mercado


def mostrar_menu():
    print("\n--- MENÚ DE EJEMPLO ---")
    print("1. Convertir Dólares a Euros")
    print("2. Salir")
    return input("Elige una opción: ")


def main():
    while True:
        opcion = mostrar_menu()

        if opcion == "1":
            try:
                usd = float(input("Ingresa cantidad en Dólares (USD): "))
                # Llamamos a la función pura
                resultado = convertir_dolares_a_euros(usd)
                print(f"${usd} USD equivalen a €{resultado:.2f} EUR.")
            except ValueError:
                print("Error: Ingresa un número válido.")
        elif opcion == "2":
            print("Saliendo...")
            break
        else:
            print("Opción no válida.")


if __name__ == "__main__":
    main()
