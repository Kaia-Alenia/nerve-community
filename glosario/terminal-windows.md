# 🪟 Glosario: Terminal — Windows

Guía de la terminal para usuarios de **Windows**. Si estás en Linux o macOS, consulta el [Glosario de Linux/macOS](terminal-linux.md).

---

## ¿Qué Terminal Usar en Windows?

Windows tiene **tres** opciones de terminal. Aquí te explicamos cuál te conviene para los retos de Nerve Community:

| Terminal | 🔍 ¿Qué es? | ¿Se recomienda? |
| :--- | :--- | :--- | :--- | :--- |
| **CMD (Símbolo del Sistema)** | La terminal antigua de Windows. Comandos propios (`dir`, `copy`, `del`). | ⚠️ Funciona pero es limitada. Úsala solo si no tienes otra opción. |
| **PowerShell** | Terminal moderna de Microsoft. Más potente que CMD. | ✓ Buena opción. Viene preinstalada en Windows 10/11. |
| **Git Bash** | Terminal que emula bash de Linux dentro de Windows. Viene con Git for Windows. | ✅ **Recomendada**. Te permite usar comandos de Linux (`ls`, `cat`, `nano`) y toda la guía de los retos aplica igual. |
| **WSL (Windows Subsystem for Linux)** | Una instalación completa de Linux dentro de Windows. | ✅ **La mejor opción** si quieres la experiencia idéntica a Linux. Un poco más compleja de configurar. |

> 💡 **Recomendación para los retos:** Instala **Git for Windows** (incluye Git Bash) y usarás los mismos comandos que aparecen en todas las guías del repo. Descárgalo en [gitforwindows.org](https://gitforwindows.org/).

---

## Conceptos Universales de Terminal

Estos términos aplican en cualquier sistema operativo.

| Término | 🔍 ¿Qué es? | 🎯 ¿Para qué sirve? | 💻 Ejemplo | ⚠️ Error común | 🔗 Relacionado |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Terminal** | Interfaz de texto para tu sistema | Un programa donde escribes comandos de texto. En Windows: CMD, PowerShell o Git Bash. | `Win + R` → escribe `cmd` → Enter | N/A | - |
| **Prompt** | La línea de espera | El símbolo que indica que la terminal espera un comando. | CMD: `C:\Users\alejandro>` / Git Bash: `alejandro@PC MINGW64 ~$` | N/A | - |
| **Comando** | Instrucción para la terminal | Una palabra que le dices a la terminal que ejecute. | `cd`, `python`, `git` | N/A | - |
| **Flag / Bandera** | Modificador de un comando | Modifica el comportamiento. Empieza con `/` en CMD o `-`/`--` en PowerShell y Git Bash. | `dir /a` (CMD) o `ls -la` (Git Bash) | N/A | - |
| **Ruta (Path)** | Dirección de un archivo o carpeta | La ubicación exacta de un archivo. En Windows usa `\`, en Git Bash usa `/`. | `C:\Users\alejandro\Documents\` o `/c/Users/alejandro/Documents/` (Git Bash) | N/A | - |
| **Ruta Absoluta** | Ruta completa desde la raíz | En Windows empieza con la letra de unidad (`C:\`). | `C:\Users\alejandro\nerve-community\README.md` | N/A | - |
| **Ruta Relativa** | Ruta desde la carpeta actual | Funciona igual que en Linux: `.`, `..`, nombre de carpeta. | `..\README.md` (CMD) o `../README.md` (Git Bash) | N/A | - |
| **`.` (punto)** | La carpeta actual | Igual que en Linux. | `git add .` = preparar todos los cambios | N/A | - |
| **`..` (dos puntos)** | La carpeta superior | Igual que en Linux. | `cd ..` = subir un nivel | N/A | - |

---

## Comandos: Comparativa CMD vs Git Bash

Aquí el equivalente de cada comando de Linux en CMD nativo de Windows, para que entiendas qué hace cada uno sin importar desde dónde lo veas en la documentación:

| Función | CMD (Windows nativo) | Git Bash / PowerShell |
| :--- | :--- | :--- | :--- | :--- |
| Ver dónde estás | `cd` (sin argumentos) | `pwd` |
| Listar archivos | `dir` | `ls` o `ls -la` |
| Cambiar de carpeta | `cd nombre-carpeta` | `cd nombre-carpeta` |
| Crear carpeta | `mkdir nombre` | `mkdir nombre` |
| Copiar archivo | `copy origen destino` | `cp origen destino` |
| Mover/renombrar | `move origen destino` | `mv origen destino` |
| Borrar archivo | `del archivo.py` | `rm archivo.py` |
| Mostrar contenido | `type archivo.txt` | `cat archivo.txt` |
| Limpiar pantalla | `cls` | `clear` |
| Buscar texto | `findstr "texto" archivo` | `grep "texto" archivo` |
| Imprimir texto | `echo Hola mundo` | `echo "Hola mundo"` |
| Encadenar comandos | `comando1 && comando2` | `comando1 && comando2` |

> ✅ **Con Git Bash instalado**, puedes usar directamente la columna de Git Bash/PowerShell, que es la misma sintaxis que usan todas las guías de los retos.

---

## Python en Windows

| Comando | 🔍 ¿Qué hace? | 💻 Ejemplo |
| :--- | :--- | :--- | :--- | :--- |
| **Instalar Python** | Descarga el instalador oficial | [python.org/downloads](https://www.python.org/downloads/) — marca "Add Python to PATH" durante la instalación |
| **python** (o `python3`) | Ejecutar un script Python | `python mi_script.py` o `python3 mi_script.py` |
| **python --version** | Ver versión instalada | `python --version` → `Python 3.11.2` |

> ⚠️ En Windows, el comando puede ser `python` (sin el `3`) si solo tienes Python 3 instalado. Si tienes ambas versiones, usa `py -3` para asegurarte.

---

## Abrir la Terminal en Windows

| Método | Cómo hacerlo |
| :--- | :--- | :--- | :--- |
| **CMD** | `Win + R` → escribe `cmd` → Enter |
| **PowerShell** | `Win + X` → selecciona "Windows PowerShell" |
| **Git Bash** | Clic derecho en cualquier carpeta → "Git Bash Here" |
| **Terminal de Windows** | Busca "Terminal" en el menú inicio (Windows 11 ya la incluye) |
| **Desde VS Code** | `Ctrl + ` ` ` (acento grave) — abre la terminal integrada |

---

## Variables de Entorno en Windows

| Término | 🔍 ¿Qué es? | 🎯 ¿Para qué sirve? | 💻 Ejemplo | ⚠️ Error común | 🔗 Relacionado |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Variable de entorno** | Variable global del sistema | Disponible para todos los programas. Se usa para API keys y configuración. | `API_KEY=abc123` | N/A | - |
| **PATH** | Lista de carpetas donde buscar ejecutables | Cuando escribes `python`, Windows busca en las carpetas del PATH. Si Python no se encuentra, no está en el PATH. | Panel de control → Variables de entorno → PATH | N/A | - |
| **set** | Crear variable temporal (CMD) | Crea una variable solo para esa sesión del CMD. | `set API_KEY=mi_clave` | N/A | - |
| **$env:** | Crear variable en PowerShell | Equivalente a `set` pero en PowerShell. | `$env:API_KEY = "mi_clave"` | N/A | - |

---

## WSL (Windows Subsystem for Linux) — Opción Avanzada

WSL te permite tener una distribución completa de Linux (Ubuntu, Debian, etc.) corriendo dentro de Windows, sin máquina virtual.

| Concepto | Descripción |
| :--- | :--- | :--- | :--- |
| **¿Qué es WSL?** | Una capa de compatibilidad que permite correr Linux nativo dentro de Windows 10/11. |
| **¿Por qué usarlo?** | Tienes acceso a todos los comandos de Linux (`ls`, `nano`, `apt`, etc.) y la experiencia es idéntica a un servidor real. Los retos más avanzados (Rust, Go) funcionan mucho mejor en WSL que en Windows nativo. |
| **¿Cómo instalarlo?** | Abre PowerShell como administrador y ejecuta: `wsl --install` (instala Ubuntu por defecto). Requiere reiniciar. |
| **¿Dónde viven mis archivos?** | Puedes acceder a tus archivos de Windows desde WSL en `/mnt/c/Users/tu_usuario/`. |

---

> 💡 **Resumen para empezar rápido en Windows:**
> 1. Instala **Git for Windows** → [gitforwindows.org](https://gitforwindows.org/)
> 2. Instala **Python 3** → [python.org/downloads](https://www.python.org/downloads/) (marca "Add to PATH")
> 3. Usa **Git Bash** como tu terminal principal
> 4. Con eso, todos los comandos de las guías del repo funcionarán igual en tu Windows 🚀

---

← [Volver al Índice del Glosario](README.md) | → [Glosario Linux/macOS](terminal-linux.md)
