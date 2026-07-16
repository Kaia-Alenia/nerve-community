def convertir_celsius_a_fahrenheit(celsius: float) -> float:
    """
    Función pura: recibe un valor, devuelve un valor modificado.
    No imprime nada, no pide inputs.
    """
    return (celsius * 9/5) + 32

def mostrar_menu():
    print("\n--- MENÚ DE EJEMPLO ---")
    print("1. Convertir Celsius a Fahrenheit")
    print("2. Salir")
    return input("Elige una opción: ")

def main():
    while True:
        opcion = mostrar_menu()
        
        if opcion == "1":
            try:
                c = float(input("Ingresa grados Celsius: "))
                # Llamamos a la función pura
                resultado = convertir_celsius_a_fahrenheit(c)
                print(f"{c} °C equivalen a {resultado:.2f} °F.")
            except ValueError:
                print("Error: Ingresa un número válido.")
        elif opcion == "2":
            print("Saliendo...")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()
