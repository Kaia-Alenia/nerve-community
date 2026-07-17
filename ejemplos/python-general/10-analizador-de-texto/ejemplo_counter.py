from collections import Counter

# 1. Lista estática de elementos (ej. frutas)
frutas = ["manzana", "pera", "manzana", "naranja", "pera", "manzana", "platano"]

# 2. Usar Counter para contar cuántas veces aparece cada elemento en la lista
conteo = Counter(frutas)

# 3. Obtener los 2 elementos más comunes
top_2 = conteo.most_common(2)

print("Resultados del conteo de frutas:")
for fruta, frecuencia in top_2:
    print(f"- La fruta '{fruta}' aparece {frecuencia} vez/veces.")
