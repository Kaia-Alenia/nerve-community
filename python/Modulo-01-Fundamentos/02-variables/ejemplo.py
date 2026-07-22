print("--- 1. CREANDO NUESTRA PRIMERA CAJA ---")
# Agarramos el texto "Nerve" y lo GUARDAMOS (asignamos) en la caja llamada 'usuario'.
# Recuerda: el símbolo '=' significa "guarda lo de la derecha en la izquierda".
usuario = "Nerve"
print("¡Caja 'usuario' creada con éxito!")

print("--- 2. LEYENDO LO QUE HAY EN LA CAJA ---")
# Le pedimos a Python que mire dentro de la caja y lo muestre en pantalla.
# Observa que 'usuario' no tiene comillas.
print(usuario)

print("--- 3. MÚLTIPLES CAJAS A LA VEZ ---")
# Podemos tener tantas cajas como queramos.
mensaje_bienvenida = "¡Bienvenido a tu segundo nivel!"
print(mensaje_bienvenida)

print("--- 4. REUTILIZANDO CAJAS (SOBRESCRIBIR) ---")
# ¿Qué pasa si guardamos algo nuevo en una caja que ya existía?
# Python sacará lo viejo y meterá lo nuevo.
usuario = "Estudiante"
print("El contenido de la caja 'usuario' ha cambiado a:")
print(usuario)
