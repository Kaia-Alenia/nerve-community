"""
Ejemplo: Mini gestor de contactos con menú interactivo y persistencia JSON

Qué enseña este ejemplo:
  - Cómo crear un loop de menú principal con while True + break
  - Cómo usar input() para leer texto y números del usuario
  - Cómo guardar y cargar datos con json.dump / json.load
  - Cómo actualizar un elemento específico de una lista (modificar un diccionario)
  - Cómo eliminar un elemento usando list.pop() o del
  - Cómo manejar el caso en que el archivo aún no existe

Para tu reto (lista de tareas):
  Aplica el mismo patrón de loop + input() + guardado JSON, pero en vez de 
  contactos (nombre/teléfono) trabajarás con tareas (texto/completado).
  - Tu "agregar" será para nuevas tareas.
  - Tu "actualizar" será tu "marcar como completada".
  - Tu "eliminar" funcionará igual que eliminar un contacto.

Glosario de términos "raros":
  with open(...) as f — Abre un archivo de forma segura. "f" es solo una variable 
                        corta para "file" (archivo). Si hay error, cierra el archivo solo.
  "r" o "w"           — Modos al abrir un archivo: "r" (read = leer), "w" (write = escribir).
  encoding="utf-8"    — Asegura que los acentos y caracteres especiales (ñ, á) se guarden bien.
  json.load()         — Convierte texto JSON de un archivo a una lista/diccionario en Python.
  json.dump()         — Convierte una lista/diccionario en Python a texto JSON en un archivo.
"""

import json
import os

ARCHIVO = "contactos.json"


def cargar_contactos():
    """
    Carga la lista de contactos desde el archivo JSON.
    Si el archivo no existe (primera vez), devuelve una lista vacía.
    """
    if not os.path.exists(ARCHIVO):
        return []

    with open(ARCHIVO, "r", encoding="utf-8") as f:
        return json.load(f)


def guardar_contactos(contactos):
    """Guarda la lista de contactos en el archivo JSON."""
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


def actualizar_contacto(contactos):
    """Demuestra cómo modificar un elemento existente en la lista."""
    mostrar_contactos(contactos)
    if not contactos:
        return

    try:
        idx = int(input("\nNúmero del contacto a actualizar: ")) - 1
        if 0 <= idx < len(contactos):
            nuevo_tel = input("Nuevo teléfono: ").strip()
            # Modificamos el valor dentro del diccionario
            contactos[idx]["telefono"] = nuevo_tel
            guardar_contactos(contactos)
            print("✓ Contacto actualizado.")
        else:
            print("Número inválido.")
    except ValueError:
        print("Por favor, ingresa un número válido.")


def eliminar_contacto(contactos):
    """Demuestra cómo eliminar un elemento de la lista usando pop()."""
    mostrar_contactos(contactos)
    if not contactos:
        return

    try:
        idx = int(input("\nNúmero del contacto a eliminar: ")) - 1
        if 0 <= idx < len(contactos):
            # pop() remueve y devuelve el elemento en ese índice
            eliminado = contactos.pop(idx)
            guardar_contactos(contactos)
            print(f"✓ Contacto '{eliminado['nombre']}' eliminado.")
        else:
            print("Número inválido.")
    except ValueError:
        print("Por favor, ingresa un número válido.")


def main():
    contactos = cargar_contactos()

    while True:
        print("\n=== Gestor de Contactos ===")
        print("1. Ver contactos")
        print("2. Agregar contacto")
        print("3. Actualizar teléfono")
        print("4. Eliminar contacto")
        print("5. Salir")

        opcion = input("\nElige una opción (1-5): ").strip()

        if opcion == "1":
            mostrar_contactos(contactos)
        elif opcion == "2":
            agregar_contacto(contactos)
        elif opcion == "3":
            actualizar_contacto(contactos)
        elif opcion == "4":
            eliminar_contacto(contactos)
        elif opcion == "5":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no reconocida, intenta de nuevo.")


if __name__ == "__main__":
    main()
