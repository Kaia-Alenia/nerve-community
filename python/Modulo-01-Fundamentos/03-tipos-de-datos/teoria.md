# Teoría: La naturaleza de la información

En el mundo real, no guardas agua en una caja de cartón ni libros en el refrigerador. Dependiendo de lo que vas a guardar, usas el recipiente adecuado. 

En Python, la información también tiene una naturaleza específica. A esto le llamamos **Tipos de Datos**. Hoy conoceremos los tres fundamentales: Texto, Números y Booleanos.

## 1. Texto (String o `str`)

Ya lo conoces. Es cualquier cosa escrita para que la lea un humano. 
- **La regla visual:** SIEMPRE va entre comillas (dobles `" "` o simples `' '`).
- **Ejemplo:** `"Hola"`, `"123"`, `"¡Peligro!"`.
- *Ojo:* Si un número está entre comillas `"10"`, Python lo ve como un dibujo del número 10, no como una cantidad matemática.

## 2. Números Enteros (Integer o `int`)

Son números exactos, sin punto decimal, perfectos para contar cosas (1, 2, 3, -5, 100).
- **La regla visual:** NUNCA llevan comillas.
- **Ejemplo:** `10`, `42`, `-5`.
- **Anatomía del símbolo `+`**: Con los números enteros, el símbolo `+` no es un adorno, sirve para realizar sumas matemáticas exactas para la computadora. Si tienes `5 + 5`, el resultado real será `10`.

## 3. Booleanos (`bool`)

Imagina un interruptor de luz: solo tiene dos estados posibles, Encendido (Verdadero) o Apagado (Falso). En Python, esto es un booleano.
- **La regla visual:** Se escriben exactamente como `True` (Verdadero) o `False` (Falso). ¡La primera letra SIEMPRE debe ser mayúscula y NO llevan comillas!
- **Ejemplo:** `True`, `False`.

## ¿Qué pasa si me equivoco?

El error más común de los principiantes es confundir el texto con números. 
Si intentas guardar un booleano en minúsculas (ej. `true`), Python te lanzará un `NameError` pensando que es una variable que olvidaste crear. 
Si pones el número `"10"` entre comillas e intentas sumarle `5`, Python entrará en pánico porque no sabe cómo sumar letras con matemáticas (lanzará un `TypeError`).
