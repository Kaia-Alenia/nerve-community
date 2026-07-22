# Las tuplas en acción: el acta sellada.

print("--- 1. CREAR UNA TUPLA ---")

# Los puntos cardinales nunca cambian. Son un dato fijo: usamos tupla.
# Observa los paréntesis ( ) en lugar de los corchetes [ ] de las listas.
puntos_cardinales = ("Norte", "Sur", "Este", "Oeste")

print("Los puntos cardinales son:")
print(puntos_cardinales)

print("--- 2. ACCEDER POR ÍNDICE (igual que las listas) ---")

# El índice funciona exactamente igual que en las listas.
# Python sigue contando desde cero.
primer_punto = puntos_cardinales[0]
print("El primer punto cardinal (índice 0) es:")
print(primer_punto)

tercer_punto = puntos_cardinales[2]
print("El tercer punto cardinal (índice 2) es:")
print(tercer_punto)

print("--- 3. len() TAMBIÉN FUNCIONA EN TUPLAS ---")

total = len(puntos_cardinales)
print("El total de puntos cardinales es:")
print(total)

print("--- 4. COMPARANDO: LISTA vs TUPLA ---")

# Una lista de tareas pendientes: SÍ puede cambiar → Lista
tareas_pendientes = ["comprar leche", "llamar al médico"]
tareas_pendientes.append("pagar renta")
print("Lista de tareas (puede cambiar):")
print(tareas_pendientes)

# Las estaciones del año: NO cambian → Tupla
estaciones = ("Primavera", "Verano", "Otoño", "Invierno")
print("Estaciones del año (no cambian):")
print(estaciones)

print("--- 5. IF CON TUPLAS: ¿Existe el dato que busco? ---")

# Guardamos el punto buscado en una variable.
punto_buscado = "Sur"

# El operador 'in' pregunta si un elemento está dentro de la colección.
# Devuelve True o False. Lo veremos a fondo más adelante; por ahora, obsérvalo.
esta_en_la_tupla = punto_buscado == puntos_cardinales[1]
if esta_en_la_tupla:
    print("El punto Sur está en la posición 1 de la tupla.")
else:
    print("No se encontró en esa posición.")

print("--- FIN DEL EJEMPLO ---")
