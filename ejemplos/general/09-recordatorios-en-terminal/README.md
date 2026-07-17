## Fechas y Tiempo (Datetime)

**¿Qué muestra este ejemplo?**
Cómo obtener la fecha actual, hacer sumas/restas de tiempo con `timedelta`, y formatear fechas a texto (o texto a fechas) usando el módulo `datetime`.

**¿Por qué es útil?**
Es necesario para cualquier sistema que maneje expiraciones, agendas, cronómetros, logs de eventos o tareas programadas.

**Cómo correrlo**
- No necesita instalar nada extra, todo es librería estándar de Python.
- Comando para ejecutarlo: `python ejemplo_datetime.py`

**¿Qué retos usan esta base?**
- [#21 Python General 09 — Recordatorios en terminal](https://github.com/Kaia-Alenia/nerve-community/issues/21)

**Nota para principiantes**
Trabajar con zonas horarias (Timezones) en Python es complicado. Si puedes elegir, intenta guardar siempre tus fechas en formato UTC y conviértelas a la hora local solo al momento de mostrárselas al usuario.