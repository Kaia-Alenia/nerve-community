## Aleatoriedad Segura (Secrets vs Random)

**¿Qué muestra este ejemplo?**
La diferencia entre generar números o valores pseudoaleatorios usando el módulo `random` frente a generar datos criptográficamente seguros usando el módulo `secrets`.

**¿Por qué es útil?**
Es crítico para crear tokens de sesión, contraseñas, o enlaces reseteo, garantizando que atacantes no puedan predecir los valores generados.

**Cómo correrlo**
- No necesita instalar nada extra, todo es librería estándar de Python.
- Comando para ejecutarlo: `python ejemplo_secrets.py`

**¿Qué retos usan esta base?**
- [#15 Python General 03 — Juego de adivina el número](https://github.com/Kaia-Alenia/nerve-community/issues/15)
- [#17 Python General 05 — Generador de contraseñas seguras](https://github.com/Kaia-Alenia/nerve-community/issues/17)

**Nota para principiantes**
Usa `random` para juegos o simulaciones, pero nunca para contraseñas o tokens de seguridad — para eso siempre usa `secrets`.