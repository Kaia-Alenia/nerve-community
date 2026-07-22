# Reto 04: La Calculadora de la Tienda 🛒

Eres el cajero de una tienda y debes calcular el total de una compra, el cambio y responder algunas preguntas usando operadores.

## Instrucciones

Dentro de la carpeta `solucion/` que está en `04-operadores/`, crea tu archivo con el formato `tu-usuario-04.py` (por ejemplo, `kaia-04.py`). Luego sigue los pasos:

1. Crea una variable `precio_camisa` con el valor `250` (un número entero).
2. Crea una variable `precio_pantalon` con el valor `480` (un número entero).
3. Crea una variable `total_compra` que guarde la **suma** de ambos precios usando `+`.
4. El cliente paga con `800`. Crea una variable `pago_cliente` con ese valor.
5. Crea una variable `cambio` que guarde la **resta** de `pago_cliente - total_compra`.
6. Crea una variable `puede_comprar` que guarde el resultado de preguntar si `pago_cliente >= total_compra` (usa `>=`).
7. Crea una variable `es_compra_cara` que guarde el resultado de preguntar si `total_compra > 600` (usa `>`).
8. Usa `print()` con separadores para mostrar todo como se ve en el resultado esperado.

**Resultado esperado en tu terminal:**
```text
--- Ticket de Compra ---
730
--- Pago del cliente ---
800
--- Cambio ---
70
--- ¿El cliente puede pagar? ---
True
--- ¿Es una compra cara (más de 600)? ---
True
```

Ejecuta desde la raíz del proyecto:
- **macOS / Linux:** `python3 python/Modulo-01-Fundamentos/04-operadores/solucion/tu-usuario-04.py`
- **Windows:** `python python/Modulo-01-Fundamentos/04-operadores/solucion/tu-usuario-04.py`

Si todos los valores coinciden y Python no arrojó ningún error, ¡pasaste al siguiente nivel!
