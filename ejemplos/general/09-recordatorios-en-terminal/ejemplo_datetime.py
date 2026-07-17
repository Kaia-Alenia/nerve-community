"""
Ejemplo: Calcular días hasta un evento dado por el usuario con datetime

Qué enseña este ejemplo:
  - Cómo parsear una fecha dada por el usuario con strptime()
  - Cómo calcular la diferencia entre dos fechas con timedelta
  - Cómo comparar fechas para saber si ya pasaron
  - Cómo revisar periódicamente (loop con time.sleep)

Para tu reto (recordatorios en terminal):
  Aplica el mismo patrón: guarda la fecha del recordatorio,
  y en un loop compara datetime.now() con esa fecha.
  Cuando now() >= fecha_recordatorio, muestra la alerta.

Glosario de términos "raros":
  datetime.datetime.now()     — fecha y hora actual del sistema
  datetime.datetime.strptime(texto, formato) — convierte un string a datetime
    El formato usa códigos:
      %Y = año con 4 dígitos (2025)
      %m = mes con 2 dígitos (01-12)
      %d = día con 2 dígitos (01-31)
      %H = hora en formato 24h (00-23)
      %M = minutos (00-59)
  timedelta                   — representa una duración (días, horas, segundos)
    timedelta(days=7)         — 7 días
    timedelta(hours=2, minutes=30) — 2 horas y 30 minutos
  diferencia.days             — días enteros en una diferencia de fechas
  tiempo2 - tiempo1           — resta dos datetimes → devuelve un timedelta
  time.sleep(segundos)        — pausa el programa N segundos
"""

import datetime
import time


def pedir_fecha_evento() -> datetime.datetime:
    """
    Pide al usuario una fecha en formato YYYY-MM-DD HH:MM
    y la convierte a un objeto datetime.
    Repite hasta que el formato sea correcto.
    """
    formato = "%Y-%m-%d %H:%M"
    while True:
        entrada = input("Fecha del evento (YYYY-MM-DD HH:MM): ").strip()
        try:
            # strptime: string parse time
            # Convierte "2025-12-25 09:00" → datetime(2025, 12, 25, 9, 0)
            fecha = datetime.datetime.strptime(entrada, formato)
            return fecha
        except ValueError:
            print(f"Formato incorrecto. Usa: YYYY-MM-DD HH:MM (ej: 2025-12-25 09:00)")


def calcular_tiempo_restante(fecha_evento: datetime.datetime) -> str:
    """
    Calcula cuánto tiempo falta (o pasó) desde ahora hasta el evento.
    Devuelve un string descriptivo.
    """
    ahora = datetime.datetime.now()
    diferencia = fecha_evento - ahora

    if diferencia.total_seconds() < 0:
        # El evento ya pasó — diferencia es negativa
        diferencia_pasada = ahora - fecha_evento
        dias = diferencia_pasada.days
        horas = diferencia_pasada.seconds // 3600
        return f"Hace {dias} día(s) y {horas} hora(s)"
    else:
        dias = diferencia.days
        horas = diferencia.seconds // 3600
        minutos = (diferencia.seconds % 3600) // 60
        return f"Faltan {dias} día(s), {horas} hora(s) y {minutos} minuto(s)"


def vigilar_evento(nombre: str, fecha_evento: datetime.datetime, intervalo_seg: int = 5):
    """
    Revisa periódicamente si el evento ya llegó.
    Simula el loop de un sistema de recordatorios.
    """
    print(f"\nVigilando el evento '{nombre}'...")
    print("(Presiona Ctrl+C para detener)\n")

    try:
        while True:
            ahora = datetime.datetime.now()
            tiempo_str = calcular_tiempo_restante(fecha_evento)
            print(f"  [{ahora.strftime('%H:%M:%S')}] {nombre}: {tiempo_str}")

            if ahora >= fecha_evento:
                print(f"\n  *** ¡RECORDATORIO! '{nombre}' es AHORA ***")
                break

            time.sleep(intervalo_seg)
    except KeyboardInterrupt:
        print("\nVigilancia detenida.")


if __name__ == "__main__":
    nombre = input("Nombre del evento: ").strip() or "Mi evento"
    fecha = pedir_fecha_evento()
    print(f"\nEvento '{nombre}' programado para: {fecha.strftime('%d/%m/%Y a las %H:%M')}")
    print(calcular_tiempo_restante(fecha))

    respuesta = input("\n¿Quieres que el programa vigile y avise cuando llegue? (s/n): ").lower()
    if respuesta == "s":
        vigilar_evento(nombre, fecha)
