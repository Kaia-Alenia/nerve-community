"""
Ejemplo: Decorador @medir_tiempo con functools.wraps

Qué enseña este ejemplo:
  - La anatomía completa de un decorador: función externa + wrapper
  - Para qué sirve @functools.wraps y qué pasa si lo omites
  - Cómo medir tiempo de ejecución con time.perf_counter()
  - Cómo hacer un decorador que funcione con CUALQUIER función (*args, **kwargs)

Para tu reto (profiler de funciones):
  Este ejemplo ya es muy similar al reto. Tu variación debe:
  - Usar time.perf_counter() (más preciso que time.time() para medición)
  - Manejar funciones con argumentos arbitrarios (*args, **kwargs)
  - Devolver el valor de retorno de la función original

Glosario:
  functools.wraps(funcion)  — un decorador para decoradores.
    Sin él, la función decorada pierde su nombre (__name__) y su docstring.
    Con él, el wrapper "pretende" ser la función original.
    Ejemplo sin wraps: saludar.__name__ → "wrapper"  (MALO)
    Ejemplo con wraps: saludar.__name__ → "saludar"  (CORRECTO)
  
  *args    — captura todos los argumentos posicionales como una tupla
  **kwargs — captura todos los argumentos nombrados como un diccionario
  Usarlos en el wrapper garantiza que el decorador funcione con CUALQUIER función.

  time.perf_counter() — reloj de alta resolución para medir duración
                        NO usar time.time() para benchmarks (menos preciso)
"""

import functools
import time


def medir_tiempo(funcion):
    """
    Decorador que mide cuántos segundos tarda en ejecutarse la función.
    Se usa escribiendo @medir_tiempo justo antes de def.
    """

    @functools.wraps(funcion)
    def wrapper(*args, **kwargs):
        inicio = time.perf_counter()

        # Llamar a la función original con todos sus argumentos
        resultado = funcion(*args, **kwargs)

        fin = time.perf_counter()
        duracion = fin - inicio

        # Imprimimos el tiempo, pero devolvemos el resultado original
        print(f"  ⏱ '{funcion.__name__}' tardó {duracion:.6f} segundos")
        return resultado

    return wrapper


# --- Aplicando el decorador ---
@medir_tiempo
def sumar_lista(numeros: list) -> float:
    """Suma todos los números de una lista."""
    return sum(numeros)


@medir_tiempo
def buscar_en_lista(lista: list, objetivo) -> bool:
    """Busca un elemento en una lista con iteración lineal (O(n))."""
    for item in lista:
        if item == objetivo:
            return True
    return False


@medir_tiempo
def simular_trabajo_pesado(iteraciones: int) -> int:
    """Simula trabajo computacional con un loop."""
    total = 0
    for i in range(iteraciones):
        total += i * i
    return total


if __name__ == "__main__":
    print("=== Demo del decorador @medir_tiempo ===\n")

    # Demostración: las funciones se ven iguales, pero el tiempo se imprime solo
    numeros = list(range(1_000_000))

    print("1. Sumar 1 millón de números:")
    resultado = sumar_lista(numeros)
    print(f"   Resultado: {resultado:,}\n")

    print("2. Buscar el último elemento (peor caso):")
    encontrado = buscar_en_lista(numeros, 999_999)
    print(f"   Encontrado: {encontrado}\n")

    print("3. Trabajo pesado con 500,000 iteraciones:")
    resultado = simular_trabajo_pesado(500_000)
    print(f"   Resultado: {resultado:,}\n")

    # Verificar que @functools.wraps preservó el nombre y docstring
    print("--- Verificación de @functools.wraps ---")
    print(f"sumar_lista.__name__ = '{sumar_lista.__name__}'")
    print(f"sumar_lista.__doc__  = '{sumar_lista.__doc__}'")
