# El bucle while en acción: contadores y condiciones dinámicas.

print("--- 1. CUENTA REGRESIVA CLÁSICA ---")

# Partimos de 5 y contamos hasta 0.
# La condición 'contador > 0' se revisa al inicio de CADA vuelta.
contador = 5

while contador > 0:
    print(contador)
    # CRÍTICO: restamos 1 en cada vuelta para que el bucle avance.
    # Si olvidamos esta línea, el programa se congela.
    contador = contador - 1

print("¡Despegue!")

print("--- 2. ACUMULADOR: SUMANDO MIENTRAS SE PUEDE ---")

# Un personaje recolecta monedas. Sigue recolectando mientras tenga energía.
energia = 100
monedas = 0

# Cada vuelta gasta 25 de energía y gana 10 monedas.
while energia > 0:
    energia = energia - 25
    monedas = monedas + 10

print("El personaje se quedó sin energía.")
print("Monedas recolectadas:")
print(monedas)
print("Energía final:")
print(energia)

print("--- 3. while CON UNA LISTA: VACIANDO LA COLA ---")

# Una lista de tareas pendientes. Seguimos trabajando mientras haya tareas.
tareas = ["Diseñar logo", "Escribir código", "Probar la app"]

print("Procesando tareas...")
while len(tareas) > 0:
    # .pop() sin argumento elimina y devuelve el ÚLTIMO elemento.
    # Guardamos lo que eliminamos para poder imprimirlo.
    tarea_actual = tareas.pop()
    print("Completando:")
    print(tarea_actual)

print("Todas las tareas completadas.")
print("Lista de tareas restantes:")
print(tareas)

print("--- 4. while + if: CONDICIÓN COMPUESTA ---")

# Vaciamos una barra de vida con condiciones adicionales.
vida = 80

while vida > 0:
    vida = vida - 30
    # Revisamos si la vida llegó a 0 o menos (evitamos números negativos en el mensaje).
    if vida <= 0:
        print("El personaje ha caído. Vida final: 0")
    else:
        print("Vida restante:")
        print(vida)

print("--- FIN DEL EJEMPLO ---")
