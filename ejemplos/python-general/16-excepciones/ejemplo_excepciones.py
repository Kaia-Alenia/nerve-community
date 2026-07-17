class FondosInsuficientesError(Exception):
    """
    Excepción personalizada lanzada cuando un usuario intenta
    retirar más dinero del que tiene en su cuenta.
    """
    pass

def procesar_retiro(balance_actual, cantidad_a_retirar):
    """
    Intenta restar la cantidad del balance. Si no hay suficiente,
    levanta una excepción personalizada.
    """
    if cantidad_a_retirar > balance_actual:
        # Lanzamos nuestro error, no un ValueError genérico
        raise FondosInsuficientesError(
            f"Transacción rechazada: Intentas retirar ${cantidad_a_retirar}, "
            f"pero solo tienes ${balance_actual} disponibles."
        )
    
    return balance_actual - cantidad_a_retirar

if __name__ == "__main__":
    mi_balance = 500
    intentos = [200, 1000]

    for intento in intentos:
        print(f"\nIntentando retirar: ${intento}")
        try:
            mi_balance = procesar_retiro(mi_balance, intento)
            print(f"✅ Éxito. Nuevo balance: ${mi_balance}")
        except FondosInsuficientesError as e:
            # Capturamos específicamente nuestro error bancario
            print(f"❌ {e}")
        except Exception as e:
            # Por si ocurre algún otro error imprevisto
            print(f"⚠️ Error general: {e}")
