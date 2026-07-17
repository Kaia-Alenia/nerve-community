# Empieza a contribuir usando solo tu celular (Termux)

No tener computadora no es excusa para hacer tu primer Pull Request. Con tu celular Android y esta guía, puedes resolver retos reales de programación.

## ¿Qué es Termux y por qué es seguro?
Termux es una aplicación para Android que emula una terminal Linux real. Es de código abierto y no requiere acceso root. 
**ATENCIÓN:** Debes instalar Termux **únicamente** desde [F-Droid](https://f-droid.org/packages/com.termux/). NO lo instales desde la Google Play Store, ya que esa versión está desactualizada y descontinuada.

## Instalación paso a paso

1. Instala F-Droid en tu celular (si no lo tienes) y descarga Termux desde ahí.
2. Abre Termux por primera vez y ejecuta los siguientes comandos para actualizar el sistema e instalar las herramientas necesarias:
   ```bash
   pkg update && pkg upgrade
   pkg install python git gh -y
   ```
3. Verifica que todo se haya instalado correctamente:
   ```bash
   python --version
   git --version
   gh --version
   ```
4. Dale permiso a Termux para acceder al almacenamiento de tu celular (útil si deseas editar los archivos fuera de Termux):
   ```bash
   termux-setup-storage
   ```

## Editor de código recomendado

Escribir código directamente en la terminal del celular puede ser incómodo. Te recomendamos instalar la aplicación **Acode** (disponible en F-Droid o Play Store). Acode es un editor de texto con resaltado de sintaxis muy fácil de usar, y puede abrir los archivos directamente desde la carpeta de Termux.

**Alternativa simple:** Si no quieres instalar otra aplicación, puedes usar el editor `nano` que viene integrado en Termux. Comandos básicos de nano:
- Guardar: `Ctrl + O` y luego `Enter`
- Salir: `Ctrl + X`

## Autenticarte con GitHub desde Termux

Para poder contribuir, necesitas enlazar Termux con tu cuenta de GitHub. Ejecuta:
```bash
gh auth login
```
Te hará una serie de preguntas, responde así:
- *What account do you want to log into?* → **GitHub.com**
- *What is your preferred protocol for Git operations?* → **HTTPS**
- *Authenticate Git with your GitHub credentials?* → **Yes**
- *How would you like to authenticate GitHub CLI?* → **Login with a web browser**

Te dará un código de 8 caracteres. Cópialo, presiona `Enter` para abrir el navegador, inicia sesión en GitHub y pega el código.

## Clonar tu fork usando Sparse-Checkout (IMPORTANTE)

**No clones todo el repositorio.** El proyecto contiene muchos retos y lenguajes pesados que consumirán tus datos móviles y espacio de almacenamiento. En su lugar, descargaremos **únicamente** la carpeta del reto en el que vas a trabajar.

1. Ve a la página de [nerve-community](https://github.com/Kaia-Alenia/nerve-community) en tu navegador y presiona **Fork**.
2. En Termux, ejecuta lo siguiente (reemplaza `TU-USUARIO` por tu usuario de GitHub y usa el comando de la tabla de abajo):

```bash
# Clonar solo la estructura sin archivos
git clone --filter=blob:none --no-checkout https://github.com/TU-USUARIO/nerve-community.git
cd nerve-community
git sparse-checkout init --cone

# Configurar la carpeta específica del reto (EJEMPLO)
git sparse-checkout set retos/general/NOMBRE-DEL-RETO

# Extraer los archivos de esa carpeta
git checkout main
cd retos/general/NOMBRE-DEL-RETO
```

### Comandos de Sparse-Checkout para cada reto (Copia y pega)

Solo necesitas el reto de la carpeta `general/`. Aquí tienes el comando listo para cada reto:

| Reto | Comando |
|------|---------|
| 01 - Lista de tareas CLI | `git sparse-checkout set retos/general/01-lista-de-tareas-cli` |
| 02 - Web scraper simple | `git sparse-checkout set retos/general/02-web-scraper-simple` |
| 03 - Juego de adivinanza | `git sparse-checkout set retos/general/03-juego-de-adivinanza` |
| 04 - Analizador de gastos CSV | `git sparse-checkout set retos/general/04-analizador-de-gastos-csv` |
| 05 - Generador de contraseñas | `git sparse-checkout set retos/general/05-generador-de-contrasenas` |
| 06 - Conversor de unidades | `git sparse-checkout set retos/general/06-conversor-de-unidades` |
| 07 - Calculadora de IMC | `git sparse-checkout set retos/general/07-calculadora-de-imc` |
| 08 - Organizador de archivos | `git sparse-checkout set retos/general/08-organizador-de-archivos` |
| 09 - Recordatorios en terminal | `git sparse-checkout set retos/general/09-recordatorios-en-terminal` |
| 10 - Analizador de texto | `git sparse-checkout set retos/general/10-analizador-de-texto` |
| 11 - Profiler de funciones | `git sparse-checkout set retos/general/11-profiler-de-funciones` |
| 12 - Validador de emails | `git sparse-checkout set retos/general/12-validador-de-emails` |
| 13 - Lector de archivos gigantes | `git sparse-checkout set retos/general/13-lector-archivos-gigantes` |
| 14 - CLI del clima | `git sparse-checkout set retos/general/14-cli-del-clima` |
| 15 - Herramienta de backup | `git sparse-checkout set retos/general/15-herramienta-de-backup` |
| 16 - Validador de edad | `git sparse-checkout set retos/general/16-validador-de-edad` |
| 17 - Lector de configuraciones | `git sparse-checkout set retos/general/17-lector-de-configuraciones` |
| 18 - Inventario de tienda | `git sparse-checkout set retos/general/18-inventario-de-tienda` |

*Si quieres trabajar en otro reto más adelante, no necesitas borrar nada. Solo ejecuta el nuevo comando `git sparse-checkout set ...` en la carpeta `nerve-community` y Git se encargará del resto.*

## Instalar dependencias de Python

Dependiendo del reto, puedes necesitar dependencias externas (ej. `pip install requests beautifulsoup4` para el scraper).

> ⚠️ **Atención:** Algunas librerías complejas que requieren compilación en C (como `Pillow` o `numpy`) pueden dar problemas en Termux. Si apenas inicias, escoge retos que utilicen solo Python puro (mira la sección de recomendados abajo).

## Flujo de trabajo normal

Una vez configurado todo, el trabajo es idéntico al que harías en una PC:
1. Crea una rama nueva: `git checkout -b mi-solucion`
2. Edita los archivos con Acode o `nano` y prueba tu código corriendo `python archivo.py`
3. Haz el commit: `git add .` y luego `git commit -m "feat: mi solución"`
4. Sube los cambios a tu fork: `git push -u origin mi-solucion`
5. Crea el Pull Request desde GitHub (o usando `gh pr create`).

*(Si es tu primera vez, consulta la guía paso a paso: [COMO-HACER-TU-PRIMER-PR.md](COMO-HACER-TU-PRIMER-PR.md))*

## Problemas comunes y soluciones

- **Error al instalar con pip:** Si `pip install` falla indicando falta de compilador, ejecuta `pkg install clang python-dev` e intenta de nuevo.
- **Espacio insuficiente:** Revisa tu espacio libre ejecutando `df -h`. Puedes liberar espacio borrando el caché de paquetes con `pkg clean`.
- **El celular se calienta rápido:** La compilación e instalación prolongada exigen mucho al procesador. Evita correr tareas muy largas con la pantalla encendida permanentemente; pausa y carga tu celular si es necesario.

## ¿Qué retos SÍ recomendamos desde el celular?

Hemos curado una lista con los retos ideales para Android, que no requieren librerías pesadas ni compilación. 
👉 **Puedes consultarla aquí:** [Issue #46 - Retos ideales para Termux](https://github.com/Kaia-Alenia/nerve-community/issues/46) 

*(Nota: Los retos de la carpeta `retos/nerve/` enfocados en Go y Rust implican compilación nativa pesada, por lo que no se recomiendan para trabajar desde el celular por ahora).*

---

### ¡El código no discrimina dispositivos!
Muchas personas maravillosas han aprendido a programar utilizando únicamente su celular Android. Tu primer Pull Request, ya sea enviado desde un teclado mecánico RGB o desde el teclado táctil en el transporte público, cuenta exactamente igual y tiene el mismo valor para la comunidad open source. ¡A programar!
