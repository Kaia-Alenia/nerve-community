# ⌨️ Glosario: Terminal y Linux

Todo lo que necesitas saber sobre la terminal (línea de comandos) para trabajar con los retos de Nerve Community, tanto en Linux/macOS como desde tu celular con Termux.

---

## La Terminal

| Término | 🔍 ¿Qué es? | 🎯 ¿Para qué sirve? | 💻 Ejemplo |
| :--- | :--- | :--- | :--- |
| **Terminal** | Interfaz de texto para tu sistema | Un programa donde escribes comandos de texto para que la computadora los ejecute, en vez de hacer clic en iconos. Fundamental para desarrollo. | `bash`, `zsh`, `cmd` (Windows) |
| **Shell** | El intérprete de comandos | El programa que lee lo que escribes en la terminal y lo ejecuta. `bash` es el más común en Linux. | `bash`, `zsh`, `fish` |
| **bash** | El shell más común en Linux | El intérprete de comandos por defecto en la mayoría de distros Linux y en los servidores. | `#!/bin/bash` al inicio de un script |
| **Prompt** | La línea de espera de la terminal | El símbolo (normalmente `$`) que aparece al inicio de la línea, indicando que la terminal espera un comando. | `alejandro@laptop:~$` |
| **Comando** | Instrucción para la terminal | Una palabra (o serie de palabras) que le dices a la terminal que ejecute. | `ls`, `cd`, `python3`, `git` |
| **Flag / Bandera** | Modificador de un comando | Una opción que cambia el comportamiento de un comando. Generalmente empieza con `-` o `--`. | `ls -la` (muestra archivos ocultos), `git push --force` |
| **Ruta (Path)** | Dirección de un archivo o carpeta | La ubicación exacta de un archivo o carpeta en el sistema de archivos. | `/home/usuario/Documentos/mi_proyecto/` |
| **Ruta Absoluta** | Ruta completa desde la raíz | Empieza desde el directorio raíz `/`. Funciona desde cualquier lugar. | `/home/alejandro/nerve-community/README.md` |
| **Ruta Relativa** | Ruta desde la carpeta actual | Depende de donde estés ahora mismo. Más corta pero solo válida desde un lugar. | `../README.md` o `retos/general/` |
| **`~` (virgulilla)** | Carpeta de inicio del usuario | Un atajo que representa la carpeta principal de tu usuario. Evita escribir la ruta completa. | `cd ~` = ir a tu carpeta de inicio |
| **`.` (punto)** | La carpeta actual | Un punto solo representa "donde estás ahora". | `git add .` = agregar todo lo que hay aquí |
| **`..` (dos puntos)** | La carpeta superior (padre) | Sube un nivel en el árbol de carpetas. | `cd ..` = ir a la carpeta de arriba |

---

## Comandos Esenciales de Linux/macOS

| Comando | 🔍 ¿Qué hace? | 💻 Ejemplo |
| :--- | :--- | :--- |
| **pwd** | Print Working Directory — muestra la ruta de la carpeta donde estás | `pwd` → `/home/alejandro/nerve-community` |
| **ls** | List — muestra los archivos y carpetas en la carpeta actual | `ls` o `ls -la` (con detalles y ocultos) |
| **cd** | Change Directory — cambia de carpeta | `cd retos/general` o `cd ..` |
| **mkdir** | Make Directory — crea una carpeta nueva | `mkdir mi-solucion` |
| **cp** | Copy — copia archivos o carpetas | `cp archivo.py copia_archivo.py` |
| **mv** | Move — mueve o renombra archivos | `mv viejo_nombre.py nuevo_nombre.py` |
| **rm** | Remove — borra archivos (⚠️ sin papelera, permanente) | `rm archivo.py` o `rm -rf carpeta/` |
| **cat** | Concatenate — muestra el contenido de un archivo | `cat README.md` |
| **nano** | Editor de texto simple en terminal | `nano mi_script.py` (editar) → `Ctrl+O` guardar → `Ctrl+X` salir |
| **echo** | Imprime texto en la terminal | `echo "Hola mundo"` |
| **clear** | Limpia la pantalla de la terminal | `clear` |
| **which** | Muestra dónde está instalado un programa | `which python3` → `/usr/bin/python3` |
| **grep** | Busca texto dentro de archivos | `grep "def " mi_script.py` → busca funciones |
| **chmod** | Change Mode — cambia los permisos de un archivo | `chmod +x mi_script.sh` (hacerlo ejecutable) |
| **df -h** | Muestra el espacio en disco disponible | `df -h` (el `-h` = "human readable", en MB/GB) |
| **&&** | Encadena comandos (el 2° solo corre si el 1° funciona) | `git add . && git commit -m "mensaje"` |

---

## Python desde la Terminal

| Comando | 🔍 ¿Qué hace? | 💻 Ejemplo |
| :--- | :--- | :--- |
| **python3** | Ejecutar un script de Python | `python3 mi_script.py` |
| **python3 --version** | Ver la versión instalada de Python | `python3 --version` → `Python 3.11.2` |
| **pip install** | Instalar una librería externa de Python | `pip install requests beautifulsoup4` |
| **pip install -r requirements.txt** | Instalar todas las dependencias de un proyecto | `pip install -r requirements.txt` |
| **requirements.txt** | Archivo que lista las dependencias de un proyecto | `pip freeze > requirements.txt` (generarlo) |
| **pip list** | Ver todas las librerías instaladas | `pip list` |
| **pip show** | Ver información de una librería específica | `pip show requests` |

---

## Termux (Android)

| Término | 🔍 ¿Qué es? | 🎯 ¿Para qué sirve? | 💻 Ejemplo |
| :--- | :--- | :--- | :--- |
| **Termux** | Terminal Linux para Android | Una app que emula una terminal Linux completa en tu celular Android. Permite programar sin PC. **Solo desde F-Droid, NO desde Play Store.** | Instalar desde `f-droid.org` |
| **F-Droid** | Tienda de apps Open Source para Android | La tienda donde descargas Termux y otras apps de código abierto. La versión de Termux en Play Store está desactualizada. | `https://f-droid.org` |
| **pkg** | Gestor de paquetes de Termux | El equivalente de `apt` en Termux. Instala herramientas del sistema. | `pkg install python git gh` |
| **pkg update && pkg upgrade** | Actualizar todos los paquetes de Termux | El primer comando que debes correr al abrir Termux por primera vez (o después de un tiempo sin usarlo). | `pkg update && pkg upgrade` |
| **termux-setup-storage** | Dar acceso al almacenamiento del celular | Permite que Termux acceda a las carpetas de tu celular (Descargas, Documentos, etc.). | `termux-setup-storage` |
| **Acode** | Editor de código para Android | App de edición de código con resaltado de sintaxis, fácil de usar en celular. Abre archivos de Termux. | Disponible en F-Droid y Play Store |
| **Sparse-Checkout** | Descargar solo una parte del repo | Técnica de Git para clonar solo la carpeta del reto que necesitas, sin descargar todo el repositorio. Crucial para no gastar datos. | `git sparse-checkout set retos/general/01-lista-de-tareas-cli` |
| **root** | Superusuario del sistema | El usuario con todos los permisos en Linux. Termux NO requiere root, a diferencia de otras apps de terminal. | Termux es seguro porque no necesita root |

---

## Variables de Entorno

| Término | 🔍 ¿Qué es? | 🎯 ¿Para qué sirve? | 💻 Ejemplo |
| :--- | :--- | :--- | :--- |
| **Variable de entorno** | Variable global del sistema | Una variable que el sistema operativo pone a disposición de todos los programas. Usada para configurar comportamiento o guardar credenciales. | `API_KEY=abc123` |
| **PATH** | Lista de carpetas donde buscar programas | Cuando escribes `python3`, el sistema busca ese programa en las carpetas del PATH. | `echo $PATH` |
| **export** | Exportar una variable al entorno | Hace que una variable esté disponible para los programas que se ejecuten desde esa terminal. | `export API_KEY="mi_clave_secreta"` |
| **.env** | Archivo de variables de entorno | Un archivo que guarda variables de entorno localmente. **NUNCA** se sube a Git (debe estar en `.gitignore`). | `API_KEY=mi_clave` en un archivo llamado `.env` |
| **.gitignore** | Archivo que le dice a Git qué ignorar | Lista de archivos y carpetas que Git no debe rastrear ni subir a GitHub. Protege claves, contraseñas y archivos temporales. | `.env`, `__pycache__/`, `*.pyc` |

---

> 💡 **Tip de Termux:** Si estás empezando desde el celular, los retos recomendados son los de Python General (carpeta `general/`). Evita los retos de `nerve/` por ahora ya que requieren compilar Go o Rust, lo cual es pesado en Android.

---

← [Volver al Índice del Glosario](README.md)
