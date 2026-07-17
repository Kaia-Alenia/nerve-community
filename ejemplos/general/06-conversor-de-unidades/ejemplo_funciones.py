"""
Ejemplo: Conversor de unidades con funciones puras, type hints y menú separado

Qué enseña este ejemplo:
  - Qué es una "función pura" y por qué es buena práctica separar lógica de UI
  - Cómo usar type hints (los ": float" y "-> float" después del nombre)
  - Cómo estructurar un menú con varias categorías sin repetir código
  - Cómo validar inputs numéricos con try/except ValueError

Para tu reto (conversor de unidades):
  Aplica el mismo patrón: una función por conversión, un menú
  que llame a la función correspondiente, y validación de input.

Glosario de type hints:
  def funcion(param: tipo) -> tipo_retorno:
    param: tipo   — indica qué tipo de dato espera el parámetro
    -> tipo       — indica qué tipo de dato devuelve la función

  Son opcionales en Python, pero sirven como documentación en vivo y
  ayudan a los editores a detectar errores antes de correr el código.

  Ejemplos:
    def sumar(a: float, b: float) -> float:   # recibe 2 floats, devuelve float
    def saludo(nombre: str) -> str:           # recibe string, devuelve string
    def imprimir(msg: str) -> None:           # devuelve None (no retorna nada)
"""

# --- Funciones puras: solo reciben datos y devuelven datos ---
# No imprimen nada, no llaman a input(), no dependen de variables globales.
# Son fáciles de probar: si le das el mismo input, SIEMPRE dan el mismo output.


def km_a_millas(km: float) -> float:
    """Convierte kilómetros a millas."""
    return km * 0.621371


def millas_a_km(millas: float) -> float:
    """Convierte millas a kilómetros."""
    return millas / 0.621371


def celsius_a_fahrenheit(c: float) -> float:
    """Convierte grados Celsius a Fahrenheit."""
    return (c * 9 / 5) + 32


def fahrenheit_a_celsius(f: float) -> float:
    """Convierte grados Fahrenheit a Celsius."""
    return (f - 32) * 5 / 9


def kg_a_libras(kg: float) -> float:
    """Convierte kilogramos a libras."""
    return kg * 2.20462


def libras_a_kg(libras: float) -> float:
    """Convierte libras a kilogramos."""
    return libras / 2.20462


# --- Mapa de opciones: conecta el menú con las funciones puras ---
OPCIONES = {
    "1": ("km → millas", km_a_millas, "km", "millas"),
    "2": ("millas → km", millas_a_km, "millas", "km"),
    "3": ("°C → °F", celsius_a_fahrenheit, "°C", "°F"),
    "4": ("°F → °C", fahrenheit_a_celsius, "°F", "°C"),
    "5": ("kg → libras", kg_a_libras, "kg", "libras"),
    "6": ("libras → kg", libras_a_kg, "libras", "kg"),
}


def mostrar_menu():
    print("\n=== Conversor de Unidades ===")
    for clave, (descripcion, _, _, _) in OPCIONES.items():
        print(f"  {clave}. {descripcion}")
    print("  7. Salir")


def pedir_valor(unidad: str) -> float | None:
    """Pide un número al usuario. Devuelve None si el input no es válido."""
    entrada = input(f"Ingresa el valor en {unidad}: ").strip()
    try:
        return float(entrada)
    except ValueError:
        print(f"Error: '{entrada}' no es un número válido.")
        return None


def main():
    while True:
        mostrar_menu()
        opcion = input("\nElige una opción: ").strip()

        if opcion == "7":
            print("¡Hasta luego!")
            break
        elif opcion in OPCIONES:
            descripcion, funcion, unidad_entrada, unidad_salida = OPCIONES[opcion]
            valor = pedir_valor(unidad_entrada)
            if valor is not None:
                resultado = funcion(valor)  # Llamamos a la función pura
                print(f"\n{valor} {unidad_entrada} = {resultado:.4f} {unidad_salida}")
        else:
            print("Opción no válida.")


if __name__ == "__main__":
    main()
