import datetime

# 1. Obtener la fecha y hora actual
ahora = datetime.datetime.now()
print(f"Momento actual: {ahora.strftime('%Y-%m-%d %H:%M:%S')}")

# 2. Calcular una fecha futura (ej. sumar 3 días)
# timedelta nos permite sumar o restar tiempo (días, horas, minutos, segundos)
futuro = ahora + datetime.timedelta(days=3)
print(f"Momento futuro (en 3 días): {futuro.strftime('%Y-%m-%d %H:%M:%S')}")

# 3. Comparar fechas
fecha_limite = datetime.datetime(2030, 1, 1, 0, 0, 0)
if ahora < fecha_limite:
    print("Todavía no llegamos al año 2030.")
else:
    print("Ya pasamos el inicio del año 2030.")
