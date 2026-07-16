# Función genérica para pedir un número entero al usuario de forma segura
def pedir_numero():
    # Bucle infinito hasta que el usuario ingrese algo válido
    while True:
        entrada = input("Por favor, ingresa un número entero: ")
        
        try:
            # Intentamos convertir la entrada a un entero
            numero = int(entrada)
            print(f"¡Excelente! Ingresaste el número {numero}.")
            return numero
            
        except ValueError:
            # Si int() falla, capturamos el error ValueError
            # Esto evita que el programa se caiga con un "Traceback"
            print("Error: Eso no es un número válido. Intenta de nuevo.")

# Llamamos a la función
numero_valido = pedir_numero()
