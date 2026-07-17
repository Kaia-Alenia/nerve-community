# Logger Distribuido (Manejo de Logs)

**¿Qué muestra este ejemplo?**
Muestra cómo capturar la fecha y hora actual (timestamps) y cómo escribir información en un archivo en modo *append* (agregar al final sin borrar lo anterior), que es la base fundamental de cualquier sistema de logs.

**¿Por qué es útil?**
Todos los sistemas en producción necesitan un registro de qué ha pasado (cuándo inició, cuándo ocurrió un error, etc.). 

**Conceptos clave:**
- **Append**: Al abrir un archivo en modo append, todo lo nuevo se escribe al final.
- **Timestamps**: Formatear la fecha/hora en un formato legible, típicamente `[YYYY-MM-DD HH:MM:SS]`.

**¿Qué retos usan esta base?**
- [Reto 05 — Logger distribuido](https://github.com/Kaia-Alenia/nerve-community/issues/5)
