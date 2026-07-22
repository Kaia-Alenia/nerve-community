# El input en acción: el programa que escucha y responde.
# AVISO: Este archivo es INTERACTIVO. Al ejecutarlo, la terminal te pedirá datos.
# Escribe los valores que se piden y presiona Enter cada vez.

print("--- 1. CAPTURA DE TEXTO ---")

# input() pausa el programa y espera que el usuario escriba algo.
# Lo que escriba se guarda como texto (str) en la variable.
nombre_usuario = input("¿Cuál es tu nombre? ")

print("¡Hola!")
print(nombre_usuario)

print("--- 2. LA TRAMPA: input() SIEMPRE DA TEXTO ---")

# Aunque el usuario escriba un número, Python lo guarda como texto.
# Usamos int() para convertirlo a número real antes de guardarlo.
edad_texto = input("¿Cuántos años tienes? ")

# En este momento, 'edad_texto' es texto. No podemos hacer matemáticas.
print("Lo que recibimos (como texto):")
print(edad_texto)

# Convertimos el texto a número entero.
edad_numero = int(edad_texto)

# Ahora sí podemos operar con él.
anios_para_treinta = 30 - edad_numero
print("Años que faltan para los 30:")
print(anios_para_treinta)

print("--- 3. CONVERSIÓN DIRECTA (en una sola línea) ---")

# Lo más común es convertir y capturar en la misma línea.
# int() envuelve a input(). Python primero ejecuta lo de adentro (input),
# luego lo convierte con int().
puntos = int(input("¿Cuántos puntos tienes? "))

if puntos >= 1000:
    print("¡Rango de leyenda!")
elif puntos >= 500:
    print("Rango avanzado.")
else:
    print("Sigue practicando.")

print("--- 4. INPUT DENTRO DE UNA FUNCIÓN ---")

# Las funciones también pueden usar input() para recopilar datos.
def crear_perfil():
    alias = input("Elige tu alias: ")
    nivel = int(input("¿En qué nivel empiezas? "))

    # Usamos las variables dentro de la función para construir el perfil.
    perfil = {
        "alias": alias,
        "nivel": nivel
    }
    return perfil

datos_jugador = crear_perfil()
print("Perfil creado:")
print(datos_jugador)

print("--- FIN DEL EJEMPLO ---")
