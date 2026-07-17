def generador_fibonacci(limite_elementos):
    """
    Genera una secuencia de números de Fibonacci de forma infinita/perezosa.
    Se detiene cuando ha entregado 'limite_elementos'.
    """
    a, b = 0, 1
    entregados = 0
    
    while entregados < limite_elementos:
        # yield pausa la función y entrega el valor 'a'
        yield a
        a, b = b, a + b
        entregados += 1

if __name__ == "__main__":
    print("Generando los primeros 10 números de Fibonacci:")
    
    # Creamos la instancia del generador
    gen = generador_fibonacci(10)
    
    # Podemos iterarlo directamente en un for
    for numero in gen:
        print(numero, end=", ")
    
    print("...")
