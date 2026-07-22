# El manejo de errores en acción: el programa a prueba de balas.
# AVISO: Este archivo es INTERACTIVO. La terminal te pedirá datos.
# Prueba escribir cosas incorrectas a propósito para ver el try/except en acción.

print("--- 1. SIN PROTECCIÓN (el programa moriría) ---")

# Este bloque está protegido. Si el usuario escribe texto, capturamos el error.
print("Intentando convertir un texto a número...")
try:
    # Simulamos que alguien nos dio texto en lugar de un número.
    numero_invalido = int("esto_no_es_un_numero")
    print("Conversión exitosa.")
except ValueError:
    # Python llegó aquí porque int("esto_no_es_un_numero") falló.
    print("¡Error capturado! El valor no es un número entero válido.")

print("El programa continúa sin haberse caído.")

print("--- 2. PROTEGIENDO EL INPUT DEL USUARIO ---")

# Ahora protegemos una entrada real del usuario.
# Si escribe texto cuando pedimos un número, el programa sobrevive.
try:
    edad = int(input("Escribe tu edad (número entero): "))
    print("Edad registrada:")
    print(edad)
except ValueError:
    print("Eso no es un número entero. Se usará 0 como valor por defecto.")
    edad = 0

print("Valor final de edad:")
print(edad)

print("--- 3. CAPTURANDO MÚLTIPLES TIPOS DE ERROR ---")

# Un mismo try puede tener varios except para distintos errores.
lista_ejemplo = [10, 20, 30]

try:
    indice = int(input("Dame un índice para buscar en la lista (0, 1 o 2): "))
    resultado = lista_ejemplo[indice]
    print("El elemento en esa posición es:")
    print(resultado)
except ValueError:
    # El usuario escribió texto en lugar de un número.
    print("Error: el índice debe ser un número entero.")
except IndexError:
    # El usuario escribió un número pero fuera del rango [0, 2].
    print("Error: ese índice no existe en la lista.")

print("--- 4. TRY / EXCEPT / ELSE / FINALLY ---")

print("Intentando dividir dos números...")
try:
    dividendo = int(input("Escribe el dividendo: "))
    divisor   = int(input("Escribe el divisor (no pongas 0): "))
    cociente  = dividendo / divisor
except ValueError:
    print("Error: uno de los valores no es un número.")
except ZeroDivisionError:
    print("Error: no se puede dividir entre cero.")
else:
    # Solo se ejecuta si el try tuvo ÉXITO.
    print("Resultado de la división:")
    print(cociente)
finally:
    # Se ejecuta SIEMPRE, haya error o no.
    print("Operación de división finalizada.")

print("--- FIN DEL EJEMPLO ---")
