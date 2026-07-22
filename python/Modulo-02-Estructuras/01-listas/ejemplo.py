# Las listas en acción: el tren de los datos.

print("--- 1. CREAR UNA LISTA ---")

# Creamos una lista con los nombres de 4 jugadores de un equipo.
# Observa los corchetes [ ] y las comas entre cada nombre.
equipo = ["Ana", "Bruno", "Carla", "Diego"]

# Imprimimos la lista completa. Python la muestra con sus corchetes.
print("El equipo completo es:")
print(equipo)

print("--- 2. ACCEDER A ELEMENTOS POR ÍNDICE ---")

# RECUERDA: Python empieza a contar desde CERO.
# El primer jugador está en la posición 0, no en la 1.
jugador_uno = equipo[0]
print("El primer jugador (índice 0) es:")
print(jugador_uno)

jugador_tres = equipo[2]
print("El tercer jugador (índice 2) es:")
print(jugador_tres)

print("--- 3. CONOCER EL TAMAÑO CON len() ---")

# len() nos dice cuántos elementos hay en la lista.
# Guardamos el resultado (un número entero) en una variable.
total_jugadores = len(equipo)
print("El número total de jugadores es:")
print(total_jugadores)

print("--- 4. AÑADIR UN ELEMENTO CON .append() ---")

# El equipo ficha a un nuevo jugador. Lo añadimos al final.
equipo.append("Elena")
print("Después de fichar a Elena, el equipo es:")
print(equipo)

# El tamaño ahora cambió.
nuevo_total = len(equipo)
print("El nuevo total de jugadores es:")
print(nuevo_total)

print("--- 5. ELIMINAR UN ELEMENTO CON .pop() ---")

# Bruno (índice 1) se retira del equipo. Lo eliminamos.
equipo.pop(1)
print("Después de que Bruno se retiró, el equipo es:")
print(equipo)

print("--- 6. COMBINANDO CON IF (del Nivel 05) ---")

# ¿El equipo tiene suficientes jugadores para jugar (mínimo 4)?
jugadores_actuales = len(equipo)
if jugadores_actuales >= 4:
    print("El equipo está completo y puede competir.")
else:
    print("El equipo necesita más jugadores.")

print("--- FIN DEL EJEMPLO ---")
