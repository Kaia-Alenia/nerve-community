"""
Ejemplo: Concurrencia con asyncio en Python

Qué enseña este ejemplo:
  - Usar `asyncio.gather` para lanzar múltiples tareas al mismo tiempo.
  - Medir cuánto tarda un bloque de código en ejecutarse usando `time.time()`.

Para tu reto (Probador de Carga Nerve):
  Reemplazarás `simular_peticion()` con `cliente.publicar(...)` o
  una llamada remota de Nerve para bombardear la red y medir el
  rendimiento total (mensajes por segundo).
"""

import asyncio
import time


# 1. Definir una tarea asíncrona que simula trabajo
async def simular_peticion(id_peticion: int):
    # Simulamos que enviar un mensaje tarda 100 milisegundos (0.1s)
    # Importante usar asyncio.sleep para no bloquear el hilo principal
    await asyncio.sleep(0.1)
    # Podrías retornar el resultado o simplemente confirmar
    return True


async def main():
    total_mensajes = 1000
    print(f"🚀 Iniciando prueba de carga: {total_mensajes} peticiones...")

    # Guardar el tiempo de inicio
    inicio = time.time()

    # 2. Crear una lista con todas las "promesas" o "tareas" a ejecutar
    tareas = []
    for i in range(total_mensajes):
        tareas.append(simular_peticion(i))

    # 3. asyncio.gather ejecuta todas las tareas en paralelo (concurrentemente)
    # Espera hasta que todas terminen y devuelve una lista con sus resultados
    resultados = await asyncio.gather(*tareas)

    # Calcular el tiempo total transcurrido
    fin = time.time()
    tiempo_total = fin - inicio

    exitosos = sum(1 for r in resultados if r is True)

    # 4. Mostrar estadísticas
    print(f"✅ Prueba finalizada en {tiempo_total:.2f} segundos.")
    print(f"📊 Mensajes exitosos: {exitosos}/{total_mensajes}")
    print(f"⚡ Rendimiento: {(total_mensajes / tiempo_total):.2f} peticiones/segundo")


if __name__ == "__main__":
    # Iniciar el bucle de eventos asíncrono
    asyncio.run(main())
