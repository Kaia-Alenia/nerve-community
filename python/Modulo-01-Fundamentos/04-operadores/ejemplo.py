# Los operadores aritméticos y de comparación en acción.

print("--- 1. OPERADORES ARITMÉTICOS ---")

# Tenemos dos números guardados en cajas.
puntos_jugador_a = 150
puntos_jugador_b = 47

# El símbolo '+' suma los números de ambas cajas.
total_puntos = puntos_jugador_a + puntos_jugador_b
print("Suma de puntos:")
print(total_puntos)

# El símbolo '-' resta. Cuántos puntos le lleva A a B.
diferencia = puntos_jugador_a - puntos_jugador_b
print("Diferencia de puntos:")
print(diferencia)

# El símbolo '*' multiplica (es el asterisco, no la 'x').
# Si cada punto vale 3 monedas, ¿cuántas monedas tiene el jugador A?
monedas_a = puntos_jugador_a * 3
print("Monedas del jugador A:")
print(monedas_a)

print("--- 2. DIVISIÓN NORMAL vs DIVISIÓN ENTERA ---")

# El símbolo '/' divide y SIEMPRE da decimales.
# Repartimos 10 monedas entre 4 amigos.
monedas_totales = 10
amigos = 4

# Con '/', Python devuelve el resultado exacto con decimales.
reparto_exacto = monedas_totales / amigos
print("Reparto exacto (con '/') :")
print(reparto_exacto)

# Con '//', Python descarta los decimales. ¿Cuántas recibe cada uno SIN dividir monedas?
reparto_entero = monedas_totales // amigos
print("Reparto entero (con '//') :")
print(reparto_entero)

# Con '%', Python devuelve las que SOBRAN.
monedas_sobrantes = monedas_totales % amigos
print("Monedas sobrantes (con '%') :")
print(monedas_sobrantes)

print("--- 3. OPERADORES DE COMPARACIÓN ---")
# Los operadores de comparación hacen PREGUNTAS. La respuesta es True o False.

vida_jugador = 80
vida_maxima = 100

# ¿Tiene el jugador la vida máxima? Preguntamos con '=='
tiene_vida_llena = vida_jugador == vida_maxima
print("¿El jugador tiene vida llena?")
print(tiene_vida_llena)

# ¿Tiene el jugador MENOS de 50 de vida? Preguntamos con '<'
esta_en_peligro = vida_jugador < 50
print("¿El jugador está en peligro (vida < 50)?")
print(esta_en_peligro)

# ¿El jugador A tiene más puntos que el jugador B?
a_gana = puntos_jugador_a > puntos_jugador_b
print("¿El jugador A va ganando?")
print(a_gana)

print("--- FIN DEL EJEMPLO ---")
