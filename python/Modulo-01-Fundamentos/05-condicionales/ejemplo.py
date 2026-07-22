# El guardia de seguridad: tomando decisiones con if / elif / else.

print("--- 1. IF SIMPLE: ¿Tiene suficiente vida? ---")

# Guardamos la vida actual del personaje en una caja.
vida_actual = 80

# Preguntamos: ¿La vida es mayor a 50?
# Si la respuesta es True, Python ejecuta el print de adentro.
if vida_actual > 50:
    # Esta línea tiene 4 espacios al inicio. Está "dentro" del if.
    print("El personaje está sano y puede pelear.")

print("--- 2. IF / ELSE: Un camino o el otro ---")

# Cambiamos la vida a un valor bajo para ver el otro camino.
vida_actual = 20

# Si la vida es mayor a 50 → camino A.
# Si NO (else) → camino B.
if vida_actual > 50:
    print("El personaje está sano.")
else:
    # Esta línea también tiene 4 espacios. Está "dentro" del else.
    print("¡PELIGRO! El personaje necesita una poción.")

print("--- 3. IF / ELIF / ELSE: Múltiples caminos ---")

# Guardamos la puntuación del jugador.
puntuacion = 750

# Python revisa cada condición de arriba hacia abajo.
# Ejecuta SOLO el primer bloque cuya condición sea True y luego salta al final.

if puntuacion >= 1000:
    # ¿Tiene 1000 o más? → Rango "S"
    print("Rango: S — ¡Maestro!")
elif puntuacion >= 700:
    # Si no llegó a 1000, ¿tiene 700 o más? → Rango "A"
    # 750 SÍ es >= 700, así que este bloque se ejecuta.
    print("Rango: A — ¡Excelente!")
elif puntuacion >= 400:
    # Si no llegó a 700, ¿tiene 400 o más? → Rango "B"
    print("Rango: B — ¡Bien!")
else:
    # Si ninguna condición anterior fue True → Rango "C"
    print("Rango: C — Sigue practicando.")

print("--- 4. COMPARANDO CON == ---")

# El guardia pide una contraseña.
contrasena_correcta = 9999
intento = 1234

# Usamos '==' para PREGUNTAR si el intento es igual a la contraseña correcta.
# RECUERDA: '==' es preguntar, '=' es guardar.
if intento == contrasena_correcta:
    print("Acceso concedido.")
else:
    print("Acceso denegado. Contraseña incorrecta.")

print("--- FIN DEL EJEMPLO ---")
