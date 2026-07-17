# Excepciones Personalizadas

## ¿Qué muestra este ejemplo?
Muestra cómo crear una excepción propia heredando de la clase base `Exception` en Python, y cómo levantarla (`raise`) y atraparla (`except`) en un bloque `try/except`.

## ¿Por qué es útil?
A veces los errores genéricos de Python (`ValueError`, `TypeError`) no describen bien el problema en la lógica de tu negocio. Crear tus propias excepciones (ej. `UsuarioNoEncontradoError`, `ConexionPerdidaError`) hace que tu código sea mucho más legible, y permite que otros programadores atrapen exactamente el error que diseñaste sin confundirlo con errores generales.

## ¿Cómo correrlo?
Abre tu terminal, navega a esta carpeta y ejecuta:
```bash
python ejemplo_excepciones.py
```

## ¿Qué retos usan esta base?
- 👉 **[Ver Issue #30 en GitHub: Python General 16 - Validador de Edad (Excepciones Personalizadas)](https://github.com/Kaia-Alenia/nerve-community/issues/30)**

## Nota para principiantes
Crear una excepción personalizada es extremadamente sencillo: solo creas una clase nueva, la haces heredar de `Exception`, y pones `pass` adentro. Python se encarga de que todo lo demás funcione (como pasarle un mensaje de error).
