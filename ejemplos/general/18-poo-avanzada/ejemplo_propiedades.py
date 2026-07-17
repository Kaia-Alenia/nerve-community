"""
Ejemplo: POO avanzada — @property con setter y validación + __repr__

Qué enseña este ejemplo:
  - Cómo usar @property para acceso controlado a atributos
  - Cómo usar @nombre.setter para validar el valor al asignar
  - Cómo implementar __repr__ para que tu objeto sea legible en debugging
  - Diferencia entre atributo público, privado (_) y name-mangled (__)

Para tu reto (inventario de tienda):
  Aplica el mismo patrón para la clase Producto:
    @property precio → devuelve self._precio
    @precio.setter  → valida que sea positivo antes de guardar
  Y para Inventario:
    @property valor_total → calcula la suma al momento de pedirlo

Glosario:
  @property          — convierte un método en un "atributo de solo lectura"
                       se accede sin paréntesis: objeto.precio (no objeto.precio())
  
  @nombre.setter     — complemento de @property que permite asignar con validación
                       se activa cuando escribes: objeto.precio = 100
                       Si no defines setter, el atributo es de solo lectura.
  
  __repr__(self)     — devuelve una representación oficial del objeto.
                       Se muestra en el REPL de Python, en listas, en f-strings, etc.
                       Convención: debe devolver algo que se pueda evaluar de nuevo.
                       Ejemplo: "Producto(nombre='Leche', precio=25.0, stock=50)"
  
  __str__(self)      — representación amigable para el usuario (print())
                       Si no está definido, Python usa __repr__
  
  Atributos privados por convención:
    _nombre   — convención: no tocar desde afuera (pero Python no lo impide)
    __nombre  — name mangling: Python lo renombra a _Clase__nombre internamente
                (sí previene acceso accidental desde subclases)
"""


class CuentaBancaria:
    """
    Cuenta bancaria con @property para controlar el saldo.
    Equivale al rol de Inventario con su valor_total en tu reto.
    """

    def __init__(self, titular: str, saldo_inicial: float = 0.0):
        self.titular = titular
        # Usamos _saldo (con _) para indicar que es "privado por convención"
        self._saldo = 0.0
        # Usamos el setter para validar incluso en __init__
        self.saldo = saldo_inicial

    @property
    def saldo(self) -> float:
        """
        Propiedad de lectura: acceder con cuenta.saldo (sin paréntesis).
        Permite hacer cálculos o transformaciones antes de devolver.
        """
        return round(self._saldo, 2)

    @saldo.setter
    def saldo(self, nuevo_valor: float):
        """
        Setter: se activa con cuenta.saldo = 500.
        Valida el valor ANTES de guardarlo.
        """
        if not isinstance(nuevo_valor, (int, float)):
            raise TypeError(f"El saldo debe ser un número, no {type(nuevo_valor).__name__}")
        if nuevo_valor < 0:
            raise ValueError(f"El saldo no puede ser negativo: {nuevo_valor}")
        self._saldo = float(nuevo_valor)

    @property
    def tiene_fondos(self) -> bool:
        """Propiedad calculada de solo lectura (sin setter)."""
        return self._saldo > 0

    def depositar(self, cantidad: float):
        if cantidad <= 0:
            raise ValueError("La cantidad a depositar debe ser positiva.")
        self.saldo = self._saldo + cantidad
        print(f"  ✓ Depósito de ${cantidad:.2f}. Nuevo saldo: ${self.saldo:.2f}")

    def retirar(self, cantidad: float):
        if cantidad <= 0:
            raise ValueError("La cantidad a retirar debe ser positiva.")
        if cantidad > self._saldo:
            raise ValueError(f"Fondos insuficientes. Saldo: ${self.saldo:.2f}")
        self.saldo = self._saldo - cantidad
        print(f"  ✓ Retiro de ${cantidad:.2f}. Nuevo saldo: ${self.saldo:.2f}")

    def __repr__(self) -> str:
        """
        Representación oficial: aparece en el REPL, en listas, en f-strings.
        Intenta que sea evaluable: CuentaBancaria("Kaia", 1000.0)
        """
        return f"CuentaBancaria(titular='{self.titular}', saldo={self.saldo})"

    def __str__(self) -> str:
        """Representación amigable para print()."""
        estado = "con fondos" if self.tiene_fondos else "sin fondos"
        return f"Cuenta de {self.titular}: ${self.saldo:.2f} ({estado})"


if __name__ == "__main__":
    print("=== Demo de @property y @setter ===\n")

    # Crear cuenta con validación en __init__ (pasa por el setter)
    cuenta = CuentaBancaria("Kaia", saldo_inicial=1000.0)

    print(f"Cuenta creada: {cuenta}")  # usa __str__
    print(f"repr: {repr(cuenta)}\n")   # usa __repr__

    # Acceso a property (sin paréntesis)
    print(f"Saldo actual: ${cuenta.saldo}")
    print(f"Tiene fondos: {cuenta.tiene_fondos}\n")

    # Operaciones
    cuenta.depositar(500)
    cuenta.retirar(200)

    # El setter valida antes de guardar
    print("\n--- Pruebas de validación en el setter ---")

    try:
        cuenta.saldo = -100  # Debe rechazarlo
    except ValueError as e:
        print(f"  ✓ Error esperado: {e}")

    try:
        cuenta.saldo = "mucho"  # Debe rechazarlo
    except TypeError as e:
        print(f"  ✓ Error esperado: {e}")

    # Sin setter: @property de solo lectura
    try:
        cuenta.tiene_fondos = True  # No tiene setter → AttributeError
    except AttributeError as e:
        print(f"  ✓ Error esperado (sin setter): {e}")

    print(f"\nEstado final: {cuenta}")
