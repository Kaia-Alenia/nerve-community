"""
Ejemplo: Excepciones personalizadas con herencia — validación de edad

Qué enseña este ejemplo:
  - Cómo crear excepciones propias heredando de Exception
  - Por qué crear excepciones específicas en vez de usar ValueError genérico
  - Cómo usar raise para lanzar una excepción manualmente
  - Cómo capturar excepciones específicas con except en orden de más a menos específico

Para tu reto (validador de edad):
  Este ejemplo es directamente aplicable. Crea tus excepciones
  EdadNegativaError y EdadNoNumericaError heredando de Exception,
  y lánzalas con raise en la función que valida la edad.

Glosario:
  class MiError(Exception)  — crea una excepción personalizada.
    Exception es la clase base de todos los errores en Python.
    Al heredar de ella, tu clase "es" un error que Python puede capturar.

  raise MiError("mensaje")  — lanza la excepción manualmente.
    Detiene la ejecución y busca el except más cercano que la maneje.

  try / except / else / finally:
    try:     — bloque que puede fallar
    except ErrorEspecifico: — captura ese tipo de error específico
    except Exception:       — captura CUALQUIER error (úsalo como último recurso)
    else:    — se ejecuta SOLO si no hubo excepciones
    finally: — se ejecuta SIEMPRE (con o sin error) — útil para limpiar recursos

  Orden de except: de más específico a más general.
    Si pones except Exception primero, nunca llegará a los except específicos.
"""


# --- Definición de excepciones personalizadas ---
class EdadInvalidaError(Exception):
    """
    Clase base para todos los errores de edad.
    Heredar de ella permite capturar TODOS los errores de edad con un solo except.
    """

    pass


class EdadNegativaError(EdadInvalidaError):
    """Se lanza cuando la edad es un número negativo."""

    pass


class EdadExcesivaError(EdadInvalidaError):
    """Se lanza cuando la edad supera un máximo razonable."""

    MAXIMO = 150

    def __init__(self, edad_recibida: int):
        # Podemos personalizar el mensaje de error en __init__
        super().__init__(
            f"Edad {edad_recibida} supera el máximo posible de {self.MAXIMO} años."
        )
        self.edad_recibida = edad_recibida


class EdadNoNumericaError(EdadInvalidaError):
    """Se lanza cuando el input no es un número."""

    pass


# --- Función que valida y lanza las excepciones ---
def validar_edad(entrada: str) -> int:
    """
    Recibe un string (como vendrá de input()), valida la edad y la devuelve.
    Lanza una excepción específica según el tipo de error.
    """
    # Intentar convertir a entero
    try:
        edad = int(entrada)
    except ValueError:
        raise EdadNoNumericaError(f"'{entrada}' no es un número entero válido.")

    if edad < 0:
        raise EdadNegativaError(f"La edad no puede ser negativa. Recibido: {edad}")

    if edad > EdadExcesivaError.MAXIMO:
        raise EdadExcesivaError(edad)

    return edad


# --- Uso con try/except ---
def procesar_registro(nombre: str, edad_str: str):
    """
    Procesa el registro de una persona, manejando cada tipo de error.
    """
    print(f"\nProcesando: nombre='{nombre}', edad='{edad_str}'")
    try:
        edad = validar_edad(edad_str)
        print(f"  ✓ Registro válido: {nombre}, {edad} años")

    except EdadNoNumericaError as e:
        # Más específico primero
        print(f"  ✗ Error de formato: {e}")

    except EdadNegativaError as e:
        print(f"  ✗ Edad negativa: {e}")

    except EdadExcesivaError as e:
        print(f"  ✗ Edad excesiva: {e}")
        print(f"     Valor recibido fue: {e.edad_recibida}")

    except EdadInvalidaError as e:
        # Captura CUALQUIER EdadInvalidaError no capturado arriba
        print(f"  ✗ Error de edad genérico: {e}")


if __name__ == "__main__":
    print("=== Demo de excepciones personalizadas ===")

    casos = [
        ("María", "28"),  # Válido
        ("Carlos", "-5"),  # EdadNegativaError
        ("Luis", "abc"),  # EdadNoNumericaError
        ("Ana", "200"),  # EdadExcesivaError
        ("Sofía", "0"),  # Válido (recién nacida)
        ("Pedro", "150"),  # EdadExcesivaError (exactamente el límite)
        ("Juan", "3.5"),  # EdadNoNumericaError (float no es int)
    ]

    for nombre, edad_str in casos:
        procesar_registro(nombre, edad_str)
