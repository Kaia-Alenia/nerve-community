# POO Avanzada: Propiedades Calculadas

## ¿Qué muestra este ejemplo?
Muestra cómo usar el decorador `@property` en la Programación Orientada a Objetos (POO) para crear atributos computados o propiedades de "solo lectura".

## ¿Por qué es útil?
A veces necesitas que un objeto exponga un dato que se arma a partir de otros (como juntar nombre y apellido, o resumir un libro). Usando `@property`, logras que el usuario de la clase pueda consultar el dato simplemente leyendo `objeto.resumen` (sin usar paréntesis), ocultando el cálculo interno. Además, al no definir un *setter*, garantizas que nadie desde fuera pueda corromper ese dato sobreescribiéndolo directamente.

## ¿Cómo correrlo?
Abre tu terminal, navega a esta carpeta y ejecuta:
```bash
python ejemplo_propiedades.py
```

## ¿Qué retos usan esta base?
- 👉 **[Ver Issue #32 en GitHub: Python General 18 - Inventario de Tienda (POO Avanzada)](https://github.com/Kaia-Alenia/nerve-community/issues/32)**

## Nota para principiantes
El decorador `@property` transforma un método en un atributo virtual. Esta es la forma "Pythónica" de manejar getters y setters. Si luego necesitas permitir que el valor cambie, agregarás un decorador secundario llamado `@nombre_de_propiedad.setter`.
