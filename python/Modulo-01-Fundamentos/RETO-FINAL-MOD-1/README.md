# Reto Final: Módulo 01 — Fundamentos 🏆

¡Llegaste al final del primer módulo! Ha llegado la hora de la verdad.

Este reto no te da instrucciones paso a paso. Tú decides **cómo** resolver el problema usando todo lo que aprendiste. Solo tienes el enunciado y el resultado esperado.

---

## El Problema: Sistema de Registro de un Club

Eres el programador de un club exclusivo. Debes crear un sistema que evalúe a un nuevo solicitante y emita un **reporte de acceso**.

Crea tu archivo en la carpeta `solucion/` dentro de `RETO-FINAL-MOD-1/` y nómbralo con el formato `tu-usuario-final.py` (por ejemplo, `kaia-final.py`).

### Datos del solicitante (define estos valores tú mismo al inicio del archivo):

- `nombre`: El nombre del solicitante. Guárdalo como texto (`str`).
- `edad`: La edad del solicitante. Guárdalo como número entero (`int`). Usa el valor `17`.
- `puntos_reputacion`: Los puntos de reputación del solicitante. Usa el valor `850`.
- `cuota_anual`: El costo anual del club. Usa el valor `1200`.
- `saldo_solicitante`: El dinero disponible del solicitante. Usa el valor `950`.

### Lógica que debes programar:

1. Calcula una variable `cuota_con_descuento`. Si el solicitante tiene `850` o más puntos de reputación, el club le da un descuento del 20%. El 20% de la cuota son 240 pesos, así que la cuota con descuento es `cuota_anual - 240`.

2. Calcula una variable `puede_pagar`. Pregunta (con un operador de comparación) si el `saldo_solicitante` es **mayor o igual** a la `cuota_con_descuento`.

3. Determina el **acceso al club** con `if / elif / else`:
   - Crea una variable `estado_acceso`.
   - **SI** la `edad` es **menor que** `18`: guarda en `estado_acceso` el texto `"Denegado: menor de edad"`.
   - **SI NO, SI** `puede_pagar` es `False`: guarda en `estado_acceso` el texto `"Denegado: saldo insuficiente"`.
   - **SI NO** (pasa ambas pruebas): guarda en `estado_acceso` el texto `"Acceso aprobado"`.

4. Imprime el reporte completo con separadores, tal como se ve en el resultado esperado.

---

## Resultado esperado en tu terminal

```text
--- REPORTE DE ACCESO AL CLUB ---
--- Solicitante ---
Alex
--- Edad ---
17
--- Puntos de reputación ---
850
--- Cuota normal ---
1200
--- Cuota con descuento (20%) ---
960
--- ¿Puede pagar la cuota? ---
False
--- VEREDICTO FINAL ---
Denegado: menor de edad
```

> **Nota:** El `nombre` puede ser el que tú quieras. Los números deben coincidir exactamente con los del resultado.

---

## Criterios de éxito ✓

- [ ] El código corre sin ningún error.
- [ ] Todos los valores numéricos coinciden con el resultado esperado.
- [ ] El `estado_acceso` muestra `"Denegado: menor de edad"` porque la `edad` es `17` (aunque no pueda pagar, la edad se evalúa primero).
- [ ] Usaste variables para **todo**: ningún número aparece "suelto" en un `print()`, solo variables.

¡Mucho éxito! Si logras esto, dominas los fundamentos de Python. El Módulo 02 te espera.
