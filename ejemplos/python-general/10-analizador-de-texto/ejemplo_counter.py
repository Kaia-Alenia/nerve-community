from collections import Counter
import re

texto_ejemplo = "El perro corre. El gato salta. El perro duerme."

# 1. Limpiar el texto de puntuación y pasar todo a minúsculas
# re.sub reemplaza cualquier cosa que no sea letra o espacio por nada ('')
texto_limpio = re.sub(r'[^\w\s]', '', texto_ejemplo).lower()
print(f"Texto limpio: {texto_limpio}")

# 2. Dividir el texto en una lista de palabras
palabras = texto_limpio.split()

# 3. Usar Counter para contar cuántas veces aparece cada elemento en la lista
conteo = Counter(palabras)

# 4. Obtener los 2 elementos más comunes
top_2 = conteo.most_common(2)

print("\nResultados del conteo:")
for palabra, frecuencia in top_2:
    print(f"- La palabra '{palabra}' aparece {frecuencia} vez/veces.")
