"""
Ejemplo: Escritura de Logs en Python

Qué enseña este ejemplo:
  - Cómo obtener la fecha y hora actual con `datetime`.
  - Cómo abrir un archivo en modo "append" ("a") para no sobreescribir datos anteriores.
  - Cómo formatear strings para que luzcan como logs profesionales.

Para tu reto (Logger Distribuido con Nerve):
  En vez de llamar a `escribir_log` con datos estáticos, tu receptor de Nerve
  escuchará mensajes de otros nodos y llamará a tu función de log para
  registrarlos en un archivo central.

Glosario:
  datetime.now()           — Obtiene la fecha y hora exactas del sistema.
  strftime("%Y-%m-%d...")  — Da formato a la fecha (String Format Time). %Y es año, %m es mes, etc.
  open(..., "a")           — Abre el archivo en modo "append" (agregar al final). Si usas "w", borra todo.
"""

from datetime import datetime

# El archivo donde guardaremos los logs
ARCHIVO_LOG = "sistema.log"


def escribir_log(nivel: str, mensaje: str):
    """
    Escribe un mensaje de log en el archivo con un timestamp y un nivel (INFO, ERROR, etc.).
    """
    # 1. Obtenemos el timestamp actual
    ahora = datetime.now()

    # 2. Le damos un formato legible, ej: 2026-07-17 15:30:05
    timestamp_formateado = ahora.strftime("%Y-%m-%d %H:%M:%S")

    # 3. Construimos la línea de log final
    # Ejemplo: [2026-07-17 15:30:05] [INFO] El servidor ha iniciado correctamente
    linea_log = f"[{timestamp_formateado}] [{nivel}] {mensaje}\n"

    # 4. Imprimimos en consola (opcional, para verlo en vivo)
    print(linea_log, end="")

    # 5. Escribimos en el archivo en modo "a" (append)
    with open(ARCHIVO_LOG, "a", encoding="utf-8") as f:
        f.write(linea_log)


def main():
    print(f"Escribiendo logs en '{ARCHIVO_LOG}'...\n")

    escribir_log("INFO", "Sistema iniciado.")
    escribir_log("DEBUG", "Conexión a la base de datos establecida en 14ms.")
    escribir_log("WARNING", "Poco espacio en disco (15% restante).")
    escribir_log(
        "ERROR", "Fallo al procesar el archivo 'datos.csv': Archivo no encontrado."
    )
    escribir_log("INFO", "Apagando sistema de forma segura.")

    print(f"\nRevisa el archivo '{ARCHIVO_LOG}' para ver los resultados guardados.")


if __name__ == "__main__":
    main()
