# Los diccionarios en acción: la ficha del jugador.

print("--- 1. CREAR UN DICCIONARIO ---")

# Modelamos la ficha de un jugador de videojuego.
# Cada clave (entre comillas) describe el dato. El valor puede ser str, int o bool.
jugador = {
    "alias": "DragonX",
    "nivel": 42,
    "vida": 100,
    "esta_conectado": True
}

# Imprimimos el diccionario completo. Python lo muestra con sus llaves { }.
print("Ficha completa del jugador:")
print(jugador)

print("--- 2. ACCEDER A VALORES POR CLAVE ---")

# En lugar de un número, usamos el nombre de la clave entre corchetes.
alias = jugador["alias"]
print("El alias del jugador es:")
print(alias)

vida_actual = jugador["vida"]
print("La vida actual del jugador es:")
print(vida_actual)

print("--- 3. MODIFICAR UN VALOR EXISTENTE ---")

# El jugador sube de nivel. Modificamos el valor de la clave "nivel".
# La sintaxis es igual que asignar una variable, pero con la clave como destino.
jugador["nivel"] = 43
print("El jugador subió de nivel. Su nivel ahora es:")
print(jugador["nivel"])

print("--- 4. AÑADIR UNA CLAVE NUEVA ---")

# El jugador consigue una habilidad especial. Creamos una nueva clave.
jugador["habilidad"] = "Teletransportación"
print("Se añadió la habilidad. La ficha actualizada es:")
print(jugador)

print("--- 5. ELIMINAR UNA CLAVE CON .pop() ---")

# El jugador se desconecta. Eliminamos el estado de conexión.
jugador.pop("esta_conectado")
print("El jugador se desconectó. La ficha sin ese campo es:")
print(jugador)

print("--- 6. IF CON DICCIONARIO ---")

# Usamos el valor de una clave en una condición.
if jugador["vida"] > 50:
    print("El jugador tiene buena salud para continuar.")
else:
    print("El jugador necesita curarse.")

print("--- FIN DEL EJEMPLO ---")
