import json
import os

ARCHIVO = "tareas.json"


def cargar_tareas():
    if os.path.exists(ARCHIVO):
        with open(ARCHIVO, "r", encoding="utf-8") as f:
            return json.load(f)
    return []


def guardar_tareas(tareas):
    with open(ARCHIVO, "w", encoding="utf-8") as f:
        json.dump(tareas, f, indent=4)


def mostrar_menu():
    print("\n--- Lista de Tareas ---")
    print("1. Ver tareas pendientes")
    print("2. Agregar tarea")
    print("3. Marcar como completada")
    print("4. Eliminar tarea")
    print("5. Salir")


def principal():
    tareas = cargar_tareas()

    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            if not tareas:
                print("\nNo hay tareas registradas.")
            else:
                print("\nTareas:")
                for i, tarea in enumerate(tareas):
                    estado = "[X]" if tarea["completada"] else "[ ]"
                    print(f"{i + 1}. {estado} {tarea['descripcion']}")

        elif opcion == "2":
            descripcion = input("\nEscribe la nueva tarea: ")
            tareas.append({"descripcion": descripcion, "completada": False})
            guardar_tareas(tareas)
            print("Tarea agregada exitosamente.")

        elif opcion == "3":
            try:
                indice = int(input("\nNúmero de la tarea a completar: ")) - 1
                if 0 <= indice < len(tareas):
                    tareas[indice]["completada"] = True
                    guardar_tareas(tareas)
                    print("Tarea marcada como completada.")
                else:
                    print("Error: El número de tarea no existe.")
            except ValueError:
                print("Error: Por favor ingresa un número válido.")

        elif opcion == "4":
            try:
                indice = int(input("\nNúmero de la tarea a eliminar: ")) - 1
                if 0 <= indice < len(tareas):
                    tarea_eliminada = tareas.pop(indice)
                    guardar_tareas(tareas)
                    print(f"Tarea '{tarea_eliminada['descripcion']}' eliminada.")
                else:
                    print("Error: El número de tarea no existe.")
            except ValueError:
                print("Error: Por favor ingresa un número válido.")

        elif opcion == "5":
            print("\nSaliendo del programa...")
            break

        else:
            print("\nOpción no válida. Intenta de nuevo.")


if __name__ == "__main__":
    principal()
