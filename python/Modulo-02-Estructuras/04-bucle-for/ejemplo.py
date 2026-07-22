# El bucle for en acción: recorriendo colecciones sin esfuerzo.

print("--- 1. FOR CON UNA LISTA ---")

# Tenemos una lista de planetas del sistema solar.
planetas = ["Mercurio", "Venus", "Tierra", "Marte"]

# El bucle recorre la lista. En cada vuelta, 'planeta' guarda el elemento actual.
# No necesitamos saber los índices. El for se encarga de todo.
for planeta in planetas:
    print(planeta)

print("--- 2. FOR CON range(): CONTANDO NÚMEROS ---")

# range(5) genera los números del 0 al 4 (5 no incluido).
# Útil para repetir algo un número exacto de veces.
print("Contando del 0 al 4:")
for numero in range(5):
    print(numero)

print("--- 3. range(inicio, fin): CONTROLANDO EL PUNTO DE PARTIDA ---")

# range(1, 6) genera 1, 2, 3, 4, 5. El inicio está incluido, el fin NO.
print("Contando del 1 al 5:")
for numero in range(1, 6):
    print(numero)

print("--- 4. FOR + IF: FILTRANDO DENTRO DEL BUCLE ---")

# Recorremos los planetas y con un if filtramos cuál nos interesa.
# El if está DENTRO del for (doble indentación: 4 + 4 = 8 espacios total).
puntuaciones = [88, 45, 72, 95, 30, 61]

print("Puntuaciones aprobadas (70 o más):")
for puntuacion in puntuaciones:
    if puntuacion >= 70:
        # Este print está dentro del if, que está dentro del for.
        # Necesita 8 espacios de indentación.
        print(puntuacion)

print("--- 5. FOR CON UNA TUPLA ---")

# El for también funciona con tuplas. La sintaxis es idéntica.
dias_laborales = ("Lunes", "Martes", "Miércoles", "Jueves", "Viernes")

print("Los días de trabajo son:")
for dia in dias_laborales:
    print(dia)

print("--- FIN DEL EJEMPLO ---")
