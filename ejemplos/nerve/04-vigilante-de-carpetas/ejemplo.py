"""
Ejemplo: Monitoreo de carpeta con watchdog

Qué enseña este ejemplo:
  - Cómo usar una librería externa (watchdog) para vigilar el sistema de archivos.
  - Cómo usar manejadores de eventos (event handlers) para reaccionar a cambios.
  - Cómo mantener el programa vivo con un loop (while True) + sleep.

Para tu reto (Vigilante de carpetas con Nerve):
  Aplica esta misma estructura. En vez de solo hacer `print`, cuando se cree un 
  archivo, usarás `cliente.broadcast()` o `cliente.send()` de Nerve para 
  notificar a otros nodos.

Glosario de funciones/librerías:
  FileSystemEventHandler — Una clase base que tiene métodos como on_created, on_modified, etc.
  Observer             — El objeto que se encarga de vigilar la carpeta en un hilo separado.
  time.sleep(1)        — Hace que el programa espere 1 segundo, evitando usar el 100% de la CPU.
"""

import time
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Definimos cómo queremos reaccionar a los eventos
class MiManejador(FileSystemEventHandler):
    
    # Se llama automáticamente cuando se crea un archivo o carpeta
    def on_created(self, event):
        # event.src_path contiene la ruta del archivo afectado
        print(f"📁 [NUEVO] Se ha creado: {event.src_path}")
        
    # Se llama cuando se modifica un archivo
    def on_modified(self, event):
        print(f"✏️  [MODIFICADO] Se ha modificado: {event.src_path}")
        
    # Se llama cuando se elimina un archivo
    def on_deleted(self, event):
        print(f"🗑️  [ELIMINADO] Se ha eliminado: {event.src_path}")


def main():
    carpeta_a_vigilar = "./carpeta_prueba"
    
    # Creamos la carpeta si no existe
    if not os.path.exists(carpeta_a_vigilar):
        os.makedirs(carpeta_a_vigilar)
        print(f"Carpeta creada: {carpeta_a_vigilar}")

    # 1. Instanciamos nuestro manejador y el observador
    manejador = MiManejador()
    observador = Observer()
    
    # 2. Le decimos al observador qué carpeta vigilar, y qué manejador usar
    # recursive=False significa que no vigilará subcarpetas.
    observador.schedule(manejador, path=carpeta_a_vigilar, recursive=False)
    
    # 3. Iniciamos el observador (esto ocurre en segundo plano)
    observador.start()
    print(f"👀 Vigilando la carpeta '{carpeta_a_vigilar}'...")
    print("Crea, modifica o elimina archivos ahí para ver los eventos. Presiona Ctrl+C para salir.")

    try:
        # Mantenemos el hilo principal vivo
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nDeteniendo observador...")
        observador.stop()
        
    # Esperamos a que termine de cerrarse limpiamente
    observador.join()

if __name__ == "__main__":
    main()
