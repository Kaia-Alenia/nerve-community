from Model import Tareas
import pandas as pd
from Functions import validar_ruta_csv, validar_contenido_csv, obtener_ruta_absoluta

df = pd.DataFrame(columns=["id", "titulo", "description", "estado"])

id_task = 1

ruta_csv = ""


def option1():  # Insertar Tarea
    try:
        global id_task
        global df
        titulo_tarea = input("Ingrese el titulo de la tarea: ")
        description_tarea = input("Descripción de la tarea: ")
        estado_tarea = False
        tarea = Tareas(
            id=id_task,
            titulo=titulo_tarea,
            description=description_tarea,
            estado=estado_tarea,
        )
        id_task += 1
        nueva_fila = pd.DataFrame([{
            "id": tarea.id,
            "titulo": tarea.titulo,
            "description": tarea.description,
            "estado": tarea.estado,
        }])
        df = pd.concat([df, nueva_fila], ignore_index=True)
        print(f"Tarea creada: {tarea}\n")
    except Exception as e:
        print(f"Error al crear tarea: {e}")


def option2():  # Modificar Tarea
    global df
    try:
        id_buscar = int(input("Ingrese el id de la tarea a modificar: "))
        if id_buscar not in df["id"].values:
            print(f"No existe una tarea con dicha id.")
        else:
            while True:
                print("¿Qué desea modificar?")
                print("----------------------------------")
                print("1. Titulo")
                print("2. Descripción")
                print("3. Ambos")

                res = int(input("Introduce la opción elegida: "))

                if res == 1:
                    titulo_new = input("Introduce el nuevo titulo: ")
                    df.loc[df["id"] == id_buscar, "titulo"] = titulo_new
                    print("Titulo cambiado")
                    print(df.loc[df["id"] == id_buscar])
                    break
                elif res == 2:
                    des_new = input("Introduce la nueva descripción: ")
                    df.loc[df["id"] == id_buscar, "description"] = des_new
                    print("Descripción cambiado")
                    print(df.loc[df["id"] == id_buscar])
                    break
                elif res == 3:
                    titulo_new = input("Introduce el nuevo titulo: ")
                    des_new = input("Introduce la nueva descripción: ")
                    df.loc[df["id"] == id_buscar, "titulo"] = titulo_new
                    df.loc[df["id"] == id_buscar, "description"] = des_new
                    print("Tarea modificada")
                    print(df.loc[df["id"] == id_buscar])
                    break
                else:
                    print("Ingrese una opción valida")
    except Exception as e:
        print(f"Error al modificar el registro: {e}")


def option3():  # Actualizar Estado tarea
    global df
    try:
        id_buscar = int(input("Ingrese el id de la tarea a actualizar estado: "))
        if id_buscar not in df["id"].values:
            print(f"No existe una tarea con dicha id: {id_buscar}")
        else:
            df.loc[df["id"] == id_buscar, "estado"] = True
            print(f"Estado de la tarea con id: {id_buscar} actualizado.")
            print(df.loc[df["id"] == id_buscar])

    except Exception as e:
        print(f"Error al actualizar estado de la tarea: {e}")


def option4():  # Eliminar tarea
    global df
    try:
        id_buscar = int(input("Ingresa el id de la tarea a eliminar: "))
        if id_buscar not in df["id"].values:
            print(f"No existe una tarea con dicha id: {id_buscar}")
        else:
            df = df[df["id"] != id_buscar]
            print(f"Tarea eliminada")
            print(df)
    except Exception as e:
        print(f"Error al eliminar tarea: {e}")


def option5():  # Ver tarea especifica
    global df
    try:
        id_buscar = int(input("Ingrese la tarea a ver(id): "))
        tarea = df.loc[df["id"] == id_buscar]
        print(tarea)
    except Exception as e:
        print(f"Error al buscar tarea: {e}")


def option6():  # ver lista de tareas
    if df.empty:
        print("No hay tareas registradas.")
    else:
        print(df.to_string(index=False))



def option7():
    global id_task
    global df
    global ruta_csv

    if df.empty:
        ruta = input("Ingrese la ruta del archivo CSV: ")
        try:
            ruta_limpia = validar_ruta_csv(ruta)
            if validar_contenido_csv(ruta_limpia):
                ruta_csv = ruta_limpia
                df_csv = pd.read_csv(ruta_limpia)
                df = pd.concat([df, df_csv], ignore_index=True)
                df["id"] = df["id"].astype(int)
                df["estado"] = df["estado"].astype(bool)
                id_task = df["id"].max() + 1
                print(df.to_string(index=False))
        except Exception as e:
            print(f"Error durante el proceso de CSV:\n{e}")
    else:
        while True:
            print("Hay datos existentes en el dataframe.")
            print("¿Qué desea hacer con ellos?")
            print("----------------------------------------")
            print(
                "1. Fusionar los registros con los del CSV (Se dará prioridad a los registros existentes del DF)."
            )
            print(
                "2. Reemplazar los registros existentes con los del CSV (Se eliminarán los registros existentes)."
            )

            option = input("Ingrese su opción (1 o 2):")

            if option == "1":
                print("Fusionando registros existentes con los del CSV...")
                ruta = input("Ingrese la ruta del archivo CSV: ")
                try:
                    ruta_limpia = validar_ruta_csv(ruta)
                    if validar_contenido_csv(ruta_limpia):
                        ruta_csv = ruta_limpia
                        df_csv = pd.read_csv(ruta_limpia)
                        ultimo_id_df = df["id"].max()
                        primer_id_csv = df_csv["id"].min()
                        df_csv["id"] = (
                            df_csv["id"] - primer_id_csv + (ultimo_id_df + 1)
                        )
                        df = pd.concat([df, df_csv], ignore_index=True)
                        df["id"] = df["id"].astype(int)
                        df["estado"] = df["estado"].astype(bool)
                        id_task = df["id"].max() + 1
                        print(df.to_string(index=False))
                        break
                except Exception as e:
                    print(f"Error durante el proceso de CSV:\n{e}")
                break
            elif option == "2":
                print(
                    "Eliminando registros existentes y reemplazando con los del CSV..."
                )
                df = df.iloc[0:0]
                id_task = 1
                ruta = input("Ingrese la ruta del archivo CSV: ")
                try:
                    ruta_limpia = validar_ruta_csv(ruta)
                    if validar_contenido_csv(ruta_limpia):
                        ruta_csv = ruta_limpia
                        df_csv = pd.read_csv(ruta_limpia)
                        df = pd.concat([df, df_csv], ignore_index=True)
                        df["id"] = df["id"].astype(int)
                        df["estado"] = df["estado"].astype(bool)
                        id_task = df["id"].max() + 1
                        print(df.to_string(index=False))
                        break
                except Exception as e:
                    print(f"Error durante el proceso de CSV:\n{e}")
            else:
                print("Ingresa una opción válida (1 o 2).")


def option8():
    global df
    global ruta_csv

    if df.empty:
        print("No hay datos para exportar. ¡Hasta luego!")
        return

    destino = ruta_csv

    if ruta_csv:
        print(f"Ruta actual configurada: {ruta_csv}")
        print("1. Sobrescribir en el archivo importado")
        print("2. Exportar a un nuevo archivo CSV")
        opc = input("Seleccione una opción (1 o 2, por defecto 1): ").strip()
        if opc == "2":
            destino = input("Ingrese la nueva ruta o nombre del archivo CSV: ").strip("'\"")
    else:
        destino = input("Ingrese el nombre o ruta del archivo CSV para exportar (ej: tareas.csv): ").strip("'\"")

    if not destino:
        destino = "tareas.csv"

    path_destino = obtener_ruta_absoluta(destino)

    print(f"Exportando información a archivo CSV: {path_destino}...")
    try:
        df.to_csv(path_destino, index=False, encoding="utf-8")
        print(f"Información exportada correctamente en: {path_destino}")
        print("Bye Bye!")
    except Exception as e:
        print(f"Error al exportar a CSV: {e}")


def menu():
    print("Administrador de tareas")
    while True:
        print("--------------------------")
        print("1. Insertar Tarea")
        print("2. Modificar Tarea")
        print("3. Actualizar Estado de Tarea")
        print("4. Eliminar Tarea")
        print("5. Ver Tarea Específica")
        print("6. Ver Lista de Tareas")
        print("7. Importar lista desde un archivo CSV")
        print("8. Salir")

        option = input("¿Qué desea hacer?")

        if option == "1":
            option1()
        elif option == "2":
            option2()
        elif option == "3":
            option3()
        elif option == "4":
            option4()
        elif option == "5":
            option5()
        elif option == "6":
            option6()
        elif option == "7":
            option7()
        elif option == "8":
            option8()
            break
        else:
            print("Ingrese una opción valida")


if __name__ == "__main__":
    menu()
