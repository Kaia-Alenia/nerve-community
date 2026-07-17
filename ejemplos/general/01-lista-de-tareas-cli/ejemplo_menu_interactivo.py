"""
Ejemplo: Mini gestor de contactos con menú interactivo y persistencia JSON

Qué enseña este ejemplo:
  - Cómo crear un loop de menú principal con while True + break
  - Cómo usar input() para leer texto del usuario
  - Cómo guardar y cargar datos con json.dump / json.load
  - Cómo manejar el caso en que el archivo aún no existe

Para tu reto (lista de tareas):
  Aplica el mismo patrón de loop + input() + guardado JSON,
  pero en vez de contactos trabajarás con tareas (texto + estado completado).
"""

import json
import os

ARCHIVO = "contactos.json"


def cargar_contactos():
    """
    Carga la lista de contactos desde el archivo JSON.
    Si el archivo no existe (primera vez que corres el programa),
    devuelve una lista vacía en vez de fallar.
    """
    if not os.path.exists(ARCHIVO):
        return []  # Primera ejecución: no hay archivo todavía

    with open(ARCHIVO, "r", encoding="utf-8") as f:
        # json.load convierte el texto JSON guardado de vuelta a objetos Python
        return json.load(f)


def guardar_contactos(contactos):
    """
    Guarda la lista de contactos en el archivo JSON.

    json.dump(objeto, archivo, indent=4):
      - objeto:  lo que quieres guardar (lista, dict, etc.)
      - archivo: el archivo abierto donde escribir
      - indent=4: hace el JSON legible con sangría de 4 espacios
    encoding="utf-8": necesario para caracteres especiales (acentos, ñ, etc.)
    """
    with open(ARCHIVO, "w", encoding="utf-8") as f:
        json.dump(contactos, f, indent=4, ensure_ascii=False)


def mostrar_contactos(contactos):
    if not contactos:
        print("No hay contactos guardados todavía.")
        return
    print("\n--- Tus contactos ---")
    for i, contacto in enumerate(contactos, start=1):
        print(f"  {i}. {contacto['nombre']} — {contacto['telefono']}")


def agregar_contacto(contactos):
    nombre = input("Nombre: ").strip()
    telefono = input("Teléfono: ").strip()
    if nombre:
        contactos.append({"nombre": nombre, "telefono": telefono})
        guardar_contactos(contactos)
        print(f"✓ Contacto '{nombre}' guardado.")
    else:
        print("El nombre no puede estar vacío.")


def main():
    # Cargamos los datos al inicio (o empezamos con lista vacía)
    contactos = cargar_contactos()

    # El loop principal del menú: sigue corriendo hasta que el usuario elija Salir
    while True:
        print("\n=== Gestor de Contactos ===")
        print("1. Ver contactos")
        print("2. Agregar contacto")
        print("3. Salir")

        # input() detiene el programa y espera que el usuario escriba algo
        opcion = input("\nElige una opción (1-3): ").strip()

        if opcion == "1":
            mostrar_contactos(contactos)
        elif opcion == "2":
            agregar_contacto(contactos)
        elif opcion == "3":
            print("¡Hasta luego!")
            break  # break sale del while True
        else:
            print("Opción no reconocida, intenta de nuevo.")


if __name__ == "__main__":
    main()
