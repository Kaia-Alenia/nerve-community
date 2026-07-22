# Los archivos en acción: el cuaderno que no olvida.
# Al ejecutar este script, se creará un archivo 'registro.txt'
# en la misma carpeta donde lo ejecutes.

print("--- 1. ESCRIBIR EN UN ARCHIVO (modo 'w') ---")

# Abrimos el archivo en modo 'w' (write/escribir).
# Si 'registro.txt' no existe, Python lo crea.
# Si ya existe, BORRA su contenido y empieza desde cero.
with open("registro.txt", "w") as archivo:
    # .write() escribe una cadena de texto en el archivo.
    # '\n' es el salto de línea. Sin él, todo iría en una sola línea.
    archivo.write("=== Registro del sistema ===\n")
    archivo.write("Línea 1: Programa iniciado.\n")
    archivo.write("Línea 2: Usuario autenticado.\n")

# El bloque 'with' terminó, el archivo se cerró automáticamente.
print("Archivo 'registro.txt' creado con éxito.")

print("--- 2. LEER TODO EL CONTENIDO (modo 'r') ---")

# Abrimos el mismo archivo en modo 'r' (read/leer).
with open("registro.txt", "r") as archivo:
    # .read() devuelve todo el contenido del archivo como un texto (str).
    contenido_completo = archivo.read()

print("Contenido del archivo:")
print(contenido_completo)

print("--- 3. LEER LÍNEA POR LÍNEA CON for ---")

# El bucle 'for' recorre el archivo una línea a la vez.
# Cada 'linea' incluye el '\n' al final, por eso el print agrega una línea extra.
with open("registro.txt", "r") as archivo:
    for linea in archivo:
        print(linea)

print("--- 4. AÑADIR AL FINAL (modo 'a') ---")

# Modo 'a' (append/añadir): no borra el contenido existente.
# Añade el nuevo texto al final del archivo.
with open("registro.txt", "a") as archivo:
    archivo.write("Línea 3: Sesión cerrada correctamente.\n")

print("Línea añadida al final. Leyendo el archivo completo...")

with open("registro.txt", "r") as archivo:
    print(archivo.read())

print("--- 5. MANEJO DE ERRORES CON ARCHIVOS ---")

# ¿Qué pasa si intentamos leer un archivo que no existe?
# Usamos try/except para evitar que el programa explote.
try:
    with open("archivo_inexistente.txt", "r") as archivo:
        contenido = archivo.read()
except FileNotFoundError:
    print("Error capturado: el archivo no existe. Continuando...")

print("--- FIN DEL EJEMPLO ---")
