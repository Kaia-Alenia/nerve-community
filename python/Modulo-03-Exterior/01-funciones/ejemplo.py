# Las funciones en acción: recetas de código reutilizables.

print("--- 1. FUNCIÓN SIN PARÁMETROS ---")

# Definimos la función. Esto NO la ejecuta todavía.
# Es como escribir la receta, sin cocinar aún.
def mostrar_bienvenida():
    print("============================")
    print("  Bienvenido al sistema     ")
    print("============================")

# Aquí SÍ la ejecutamos. Los () le dicen a Python: "¡corre ahora!".
mostrar_bienvenida()

# La llamamos una segunda vez. El código se reutiliza sin repetirlo.
mostrar_bienvenida()

print("--- 2. FUNCIÓN CON UN PARÁMETRO ---")

# Esta función recibe un dato (el nombre) para personalizarse.
# 'jugador' es el parámetro: una variable temporal que solo existe aquí dentro.
def anunciar_jugador(jugador):
    print("El jugador en turno es:")
    print(jugador)

# Llamamos la función con diferentes datos cada vez.
anunciar_jugador("Ana")
anunciar_jugador("Bruno")
anunciar_jugador("Carla")

print("--- 3. FUNCIÓN CON VARIOS PARÁMETROS ---")

# Una función puede recibir más de un parámetro, separados por coma.
def mostrar_puntuacion(jugador, puntos):
    print(jugador)
    print(puntos)

mostrar_puntuacion("Diego", 1500)
mostrar_puntuacion("Elena", 980)

print("--- 4. FUNCIÓN QUE DEVUELVE UN RESULTADO (return) ---")

# Esta función no imprime: CALCULA y devuelve el resultado.
# Quien la llame recibirá ese resultado como si fuera un valor normal.
def calcular_nivel(experiencia):
    nivel = experiencia // 100   # División entera: 350 xp → nivel 3
    return nivel

# Guardamos lo que la función devuelve en una variable.
nivel_jugador = calcular_nivel(350)
print("El nivel del jugador con 350 XP es:")
print(nivel_jugador)

# Podemos usar el return directamente dentro de un print.
print("El nivel del jugador con 820 XP es:")
print(calcular_nivel(820))

print("--- 5. FUNCIÓN + FOR: PROCESANDO UNA LISTA ---")

# Una función puede trabajar con estructuras que ya conocemos.
def mostrar_inventario(lista_items):
    for item in lista_items:
        print(item)

inventario = ["Espada", "Escudo", "Poción"]
mostrar_inventario(inventario)

print("--- FIN DEL EJEMPLO ---")
