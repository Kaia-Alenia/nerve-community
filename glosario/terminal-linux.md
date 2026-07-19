# ⌨️ Glosario: Terminal — Linux y macOS

Guía de la terminal para usuarios de **Linux y macOS** (y Termux en Android). Si estás en Windows, consulta el [Glosario de Windows](terminal-windows.md).

---

## Conceptos Universales de Terminal

Estos términos aplican en cualquier sistema operativo.

| Término | 🔍 ¿Qué es? | 🎯 ¿Para qué sirve? | 💻 Ejemplo |
| :--- | :--- | :--- | :--- |
| **Terminal** | Interfaz de texto para tu sistema | Un programa donde escribes comandos de texto para que la computadora los ejecute, en vez de hacer clic en iconos. Fundamental para desarrollo. | En Linux: `GNOME Terminal`, `Konsole`. En macOS: `Terminal.app`, `iTerm2` |
| **Shell** | El intérprete de comandos | El programa que lee lo que escribes y lo ejecuta. Es el "cerebro" de la terminal. | `bash`, `zsh`, `fish` |
| **bash** | El shell más común en Linux | El intérprete por defecto en la mayoría de distros Linux y en todos los servidores. macOS usa `zsh` por defecto desde 2019. | `#!/bin/bash` al inicio de un script |
| **Prompt** | La línea de espera | El símbolo (`$`) al inicio de la línea que indica que la terminal espera un comando. | `alejandro@laptop:~$` |
| **Comando** | Instrucción para la terminal | Una palabra (o serie de palabras) que le dices a la shell que ejecute. | `ls`, `cd`, `python3`, `git` |
| **Flag / Bandera** | Modificador de un comando | Una opción que cambia el comportamiento de un comando. Empieza con `-` o `--`. | `ls -la`, `git push --force` |
| **Ruta (Path)** | Dirección de un archivo o carpeta | La ubicación exacta de un archivo en el sistema de archivos. | `/home/usuario/nerve-community/` |
| **Ruta Absoluta** | Ruta completa desde la raíz | Empieza desde `/` (la raíz del sistema). Funciona desde cualquier carpeta. | `/home/alejandro/nerve-community/README.md` |
| **Ruta Relativa** | Ruta desde la carpeta actual | Depende de dónde estás ahora. Más corta, pero solo válida desde un lugar. | `../README.md` o `retos/general/` |
| **`~` (virgulilla)** | Carpeta de inicio del usuario | Atajo que representa `/home/tu_usuario/` en Linux o `/Users/tu_usuario/` en macOS. | `cd ~` = ir a tu carpeta de inicio |
| **`.` (punto)** | La carpeta actual | Representa "donde estás ahora mismo". | `git add .` = preparar todo lo que hay aquí |
| **`..` (dos puntos)** | La carpeta superior (padre) | Sube un nivel en el árbol de carpetas. | `cd ..` = ir a la carpeta de arriba |

---

## Comandos Esenciales de Linux / macOS

| Comando | 🔍 ¿Qué hace? | 💻 Ejemplo |
| :--- | :--- | :--- |
| **pwd** | Print Working Directory — muestra dónde estás | `pwd` → `/home/alejandro/nerve-community` |
| **ls** | List — lista archivos y carpetas | `ls` o `ls -la` (con detalles y archivos ocultos) |
| **cd** | Change Directory — cambia de carpeta | `cd retos/general` o `cd ..` |
| **mkdir** | Make Directory — crea una carpeta nueva | `mkdir mi-solucion` |
| **cp** | Copy — copia archivos o carpetas | `cp archivo.py copia.py` |
| **mv** | Move — mueve o renombra archivos | `mv viejo.py nuevo.py` |
| **rm** | Remove — borra archivos (⚠️ permanente, sin papelera) | `rm archivo.py` o `rm -rf carpeta/` |
| **cat** | Muestra el contenido de un archivo | `cat README.md` |
| **nano** | Editor de texto simple en terminal | `nano mi_script.py` → `Ctrl+O` guardar → `Ctrl+X` salir |
| **echo** | Imprime texto en la terminal | `echo "Hola mundo"` |
| **clear** | Limpia la pantalla | `clear` |
| **which** | Muestra dónde está instalado un programa | `which python3` → `/usr/bin/python3` |
| **grep** | Busca texto dentro de archivos | `grep "def " mi_script.py` |
| **chmod** | Cambia permisos de un archivo | `chmod +x script.sh` (hacerlo ejecutable) |
| **df -h** | Muestra espacio en disco disponible | `df -h` (`-h` = tamaño legible: MB/GB) |
| **sudo** | Superuser Do — ejecutar como administrador | `sudo apt install git` (instalar paquetes del sistema) |
| **apt** | Gestor de paquetes de Ubuntu/Debian | `sudo apt install python3` |
| **&&** | Encadenar comandos (el 2° solo corre si el 1° funcionó) | `git add . && git commit -m "mensaje"` |

---

## Python desde la Terminal (Linux/macOS)

| Comando | 🔍 ¿Qué hace? | 💻 Ejemplo |
| :--- | :--- | :--- |
| **python3** | Ejecutar un script Python | `python3 mi_script.py` |
| **python3 --version** | Ver versión instalada | `python3 --version` → `Python 3.11.2` |
| **pip3 install** | Instalar una librería externa | `pip3 install requests` |
| **pip3 install -r requirements.txt** | Instalar todas las dependencias del proyecto | `pip3 install -r requirements.txt` |
| **pip3 list** | Ver librerías instaladas | `pip3 list` |
| **pip3 freeze** | Generar requirements.txt | `pip3 freeze > requirements.txt` |

> ⚠️ En Linux/macOS usa `python3` y `pip3` (con el `3`). Sin el `3`, podría ejecutar Python 2, que ya está obsoleto.

---

## Termux (Android)

Termux es una terminal Linux que corre en tu celular Android, sin necesidad de root ni PC.

| Término | 🔍 ¿Qué es? | 🎯 ¿Para qué sirve? | 💻 Ejemplo |
| :--- | :--- | :--- | :--- |
| **Termux** | Terminal Linux para Android | Emula una terminal Linux completa en tu celular. **Solo desde F-Droid**, la versión de Play Store está descontinuada. | `https://f-droid.org/packages/com.termux/` |
| **F-Droid** | Tienda de apps Open Source | La tienda de donde se descarga la versión correcta de Termux. | `https://f-droid.org` |
| **pkg** | Gestor de paquetes de Termux | El equivalente de `apt` dentro de Termux. Instala herramientas del sistema. | `pkg install python git gh -y` |
| **pkg update && pkg upgrade** | Actualizar paquetes de Termux | Primer comando a correr al abrir Termux por primera vez. | `pkg update && pkg upgrade` |
| **termux-setup-storage** | Dar acceso al almacenamiento | Permite que Termux acceda a las carpetas del celular (Descargas, etc.). | `termux-setup-storage` |
| **Acode** | Editor de código para Android | App con resaltado de sintaxis para editar archivos de Termux cómodamente. | Disponible en F-Droid y Play Store |
| **root** | Superusuario del sistema | El usuario con todos los permisos. Termux **NO** requiere root. | Termux es seguro por no necesitar root |
| **Sparse-Checkout** | Clonar solo una carpeta del repo | Descarga solo el reto que necesitas, sin bajar todo el proyecto. Crucial para ahorrar datos. | `git sparse-checkout set retos/general/01-lista-de-tareas-cli` |

---

## Variables de Entorno (Linux/macOS)

| Término | 🔍 ¿Qué es? | 🎯 ¿Para qué sirve? | 💻 Ejemplo |
| :--- | :--- | :--- | :--- |
| **Variable de entorno** | Variable global del sistema | Disponible para todos los programas. Se usa para configuración y credenciales (API keys). | `API_KEY=abc123` |
| **PATH** | Lista de carpetas donde buscar ejecutables | Cuando escribes `python3`, el sistema busca en las carpetas del PATH. | `echo $PATH` |
| **export** | Exportar variable al entorno | Hace que la variable esté disponible para los procesos hijos de esa sesión. | `export API_KEY="mi_clave"` |
| **.env** | Archivo de variables de entorno locales | Guarda keys y configuración. **NUNCA** se sube a GitHub (va en `.gitignore`). | `API_KEY=mi_clave` dentro del archivo `.env` |
| **.gitignore** | Archivo que le dice a Git qué ignorar | Protege archivos privados y temporales para que no se suban al repo. | `.env`, `__pycache__/`, `*.pyc` |

---

> 💡 **Tip:** En Termux puedes usar exactamente los mismos comandos de Linux que ves aquí. ¡Es la misma shell!

---

← [Volver al Índice del Glosario](README.md) | → [Glosario Windows](terminal-windows.md)
