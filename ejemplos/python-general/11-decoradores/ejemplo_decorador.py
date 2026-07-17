import functools

def log_ejecucion(funcion):
    """
    Un decorador simple que imprime un mensaje antes y después
    de ejecutar la función decorada.
    """
    @functools.wraps(funcion)
    def wrapper(*args, **kwargs):
        print(f" Iniciando ejecución de '{funcion.__name__}'...")
        resultado = funcion(*args, **kwargs)
        print(f"⏹ Finalizó '{funcion.__name__}'.")
        return resultado
    return wrapper

@log_ejecucion
def saludar(nombre):
    print(f"  ¡Hola {nombre}, bienvenido!")

if __name__ == "__main__":
    saludar("Kaia")
    print("-" * 20)
    saludar("Alejandro")
