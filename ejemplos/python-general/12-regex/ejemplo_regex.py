import re

def es_telefono_valido(telefono: str) -> bool:
    """
    Valida si una cadena tiene el formato de un número telefónico mexicano:
    +52 seguido de un espacio y exactamente 10 dígitos.
    """
    # Explicación del patrón:
    # ^     : Inicio de la cadena
    # \+52  : El texto literal "+52" (el + se escapa con \)
    # \s    : Un espacio en blanco
    # \d{10}: Exactamente 10 dígitos numéricos
    # $     : Fin de la cadena
    patron = r'^\+52\s\d{10}$'
    
    # re.match devuelve un objeto Match si encuentra coincidencia al inicio, o None si no.
    if re.match(patron, telefono):
        return True
    return False

if __name__ == "__main__":
    casos = [
        "+52 1234567890",   # Válido
        "+52 5551234567",   # Válido
        "1234567890",       # Inválido (Falta +52)
        "+52 123",          # Inválido (Muy corto)
        "+52  1234567890",  # Inválido (Doble espacio)
        "+1 1234567890",    # Inválido (Código de otro país)
    ]

    for caso in casos:
        validez = " Válido" if es_telefono_valido(caso) else " Inválido"
        print(f"[{validez}] {caso}")
