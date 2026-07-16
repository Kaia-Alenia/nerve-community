import datetime
import time

# 1. Obtener la fecha y hora actual
ahora = datetime.datetime.now()
print(f"Momento actual: {ahora.strftime('%Y-%m-%d %H:%M:%S')}")

# 2. Calcular una fecha futura (ej. dentro de 3 segundos)
# timedelta nos permite sumar o restar tiempo
futuro = ahora + datetime.timedelta(seconds=3)
print(f"Momento futuro: {futuro.strftime('%Y-%m-%d %H:%M:%S')}")

print("\nEsperando 3 segundos...")
# 3. Pausar la ejecución del programa sin saturar el procesador
time.sleep(3)

nuevo_ahora = datetime.datetime.now()
# 4. Comparar fechas
if nuevo_ahora >= futuro:
    print(f"¡El tiempo ha pasado! Momento actual: {nuevo_ahora.strftime('%Y-%m-%d %H:%M:%S')}")
