# ⌨️ Glosario: Terminal — Linux y macOS

Guía de la terminal para usuarios de **Linux y macOS** (y Termux en Android). Si estás en Windows, consulta el [Glosario de Windows](terminal-windows.md).

---

## Conceptos Universales de Terminal

Estos términos aplican en cualquier sistema operativo.

| Término | 🔍 ¿Qué es? | 🎯 ¿Para qué sirve? | 💻 Ejemplo | ⚠️ Error común | 🔗 Relacionado |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Shell** | El intérprete de comandos | El programa que lee lo que escribes y lo ejecuta. Es el "cerebro" de la terminal. | `bash`, `zsh`, `fish` | N/A | - |
| **bash** | El shell más común en Linux | El intérprete por defecto en la mayoría de distros Linux y en todos los servidores. macOS usa `zsh` por defecto desde 2019. | `#!/bin/bash` al inicio de un script | N/A | - |
| **`~` (virgulilla)** | Carpeta de inicio del usuario | Atajo que representa `/home/tu_usuario/` en Linux o `/Users/tu_usuario/` en macOS. | `cd ~` = ir a tu carpeta de inicio | N/A | - |
| **`.` (punto)** | La carpeta actual | Representa "donde estás ahora mismo". | `git add .` = preparar todo lo que hay aquí | N/A | - |
| **`..` (dos puntos)** | La carpeta superior (padre) | Sube un nivel en el árbol de carpetas. | `cd ..` = ir a la carpeta de arriba | N/A | - |

---

## Comandos Esenciales de Linux / macOS

| :--- | :--- | :--- | :--- | :--- |
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

| :--- | :--- | :--- | :--- | :--- |
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

| Término | 🔍 ¿Qué es? | 🎯 ¿Para qué sirve? | 💻 Ejemplo | ⚠️ Error común | 🔗 Relacionado |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Termux** | Terminal Linux para Android | Emula una terminal Linux completa en tu celular. **Solo desde F-Droid**, la versión de Play Store está descontinuada. | `https://f-droid.org/packages/com.termux/` | N/A | - |
| **F-Droid** | Tienda de apps Open Source | La tienda de donde se descarga la versión correcta de Termux. | `https://f-droid.org` | N/A | - |
| **pkg** | Gestor de paquetes de Termux | El equivalente de `apt` dentro de Termux. Instala herramientas del sistema. | `pkg install python git gh -y` | N/A | - |
| **pkg update && pkg upgrade** | Actualizar paquetes de Termux | Primer comando a correr al abrir Termux por primera vez. | `pkg update && pkg upgrade` | N/A | - |
| **termux-setup-storage** | Dar acceso al almacenamiento | Permite que Termux acceda a las carpetas del celular (Descargas, etc.). | `termux-setup-storage` | N/A | - |
| **Acode** | Editor de código para Android | App con resaltado de sintaxis para editar archivos de Termux cómodamente. | Disponible en F-Droid y Play Store | N/A | - |
| **root** | Superusuario del sistema | El usuario con todos los permisos. Termux **NO** requiere root. | Termux es seguro por no necesitar root | N/A | - |

---

## Variables de Entorno (Linux/macOS)

| Término | 🔍 ¿Qué es? | 🎯 ¿Para qué sirve? | 💻 Ejemplo | ⚠️ Error común | 🔗 Relacionado |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **export** | Exportar variable al entorno | Hace que la variable esté disponible para los procesos hijos de esa sesión. | `export API_KEY="mi_clave"` | N/A | - |
| **.env** | Archivo de variables de entorno locales | Guarda keys y configuración. **NUNCA** se sube a GitHub (va en `.gitignore`). | `API_KEY=mi_clave` dentro del archivo `.env` | N/A | - |

---

> 💡 **Tip:** En Termux puedes usar exactamente los mismos comandos de Linux que ves aquí. ¡Es la misma shell!

---

← [Volver al Índice del Glosario](README.md) | → [Glosario Windows](terminal-windows.md)
