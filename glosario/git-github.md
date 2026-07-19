# 🔧 Glosario: Git y GitHub

Todo lo que necesitas saber sobre el control de versiones y la plataforma GitHub para contribuir en cualquier proyecto Open Source, incluyendo Nerve Community.

---

## Conceptos Fundamentales

| Término | 🔍 ¿Qué es? | 🎯 ¿Para qué sirve? | 💻 Ejemplo | ⚠️ Error común | 🔗 Relacionado |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Git** | Programa de control de versiones | Es como una "máquina del tiempo" para tu código. Guarda el historial completo de todos los cambios que hiciste, quién los hizo y cuándo. | `git --version` (para verificar que está instalado) | N/A | - |
| **GitHub** | Plataforma web para guardar código | Una "red social para programadores" donde subes tu código con Git y puedes colaborar con otros. Nerve Community vive aquí. | `https://github.com/Kaia-Alenia/nerve-community` | N/A | - |
| **Repositorio (Repo)** | Carpeta de proyecto con historial | Contiene todos los archivos del proyecto más el historial completo de cambios. Es lo que "clonas" cuando quieres trabajar en un proyecto. | `https://github.com/Kaia-Alenia/nerve-community` | N/A | - |
| **Open Source** | Código abierto y público | Software cuyo código fuente es visible para todos y puede ser modificado y distribuido libremente. Nerve y este repo son Open Source. | Licencia GNU GPL v3 que usa este repo | N/A | - |

---

## Flujo de Trabajo Básico

| Término | 🔍 ¿Qué es? | 🎯 ¿Para qué sirve? | 💻 Ejemplo | ⚠️ Error común | 🔗 Relacionado |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Fork** | Copia personal del repositorio | Crea una copia exacta de un repo ajeno en tu cuenta de GitHub. Es como sacarle una fotocopia a un libro de la biblioteca para poder rayarlo sin arruinar el original. | Botón "Fork" en GitHub | N/A | - |
| **git clone** | Descarga del repo a tu computadora | Trae los archivos de GitHub a tu máquina local. Es como llevarte esa fotocopia desde la nube a tu disco duro para trabajar. Siempre clonas *tu fork*. | `git clone https://github.com/...` | N/A | - |
| **Branch (Rama)** | Línea de trabajo independiente | Crea una "dimensión paralela" de tu código. Trabajas en una rama separada para no tocar ni romper la rama principal (`main`). | `git checkout -b solucion-reto-01` | N/A | - |
| **Checkout** | Cambiar de rama | Te "teletransporta" entre ramas. También sirve para crear ramas nuevas con la bandera `-b`. | `git checkout main` o `git checkout -b mi-rama` | N/A | - |
| **git add** | Preparar archivos para el commit | Marca qué archivos quieres incluir en el próximo punto de guardado. Con `.` preparas todos los archivos modificados. | `git add .` o `git add mi_archivo.py` | N/A | - |
| **Commit** | Punto de guardado permanente | Guarda los cambios preparados con un mensaje descriptivo. Es el "Save State" del videojuego, pero para código. | `git commit -m "feat: agregar solución al reto 01"` | N/A | - |
| **Push** | Subir commits a GitHub | Envía los commits que tienes en tu computadora hacia tu repositorio en GitHub (en la nube). | `git push origin solucion-reto-01` | N/A | - |
| **Pull** | Bajar/actualizar desde GitHub | Descarga los cambios más recientes que existan en GitHub hacia tu computadora local. | `git pull origin main` | N/A | - |
| **Pull Request (PR)** | Solicitud de integración de cambios | Le dices al dueño del repo original: *"Oye, hice estos cambios en mi fork, ¿los quieres agregar al proyecto oficial?"* | Clic en "Compare & pull request" en GitHub después de hacer push | N/A | - |
| **Merge** | Fusionar código | Acción de aceptar un Pull Request y unir el código nuevo con el proyecto principal. Lo hacen los maintainers. | "¡Felicidades, hicimos merge de tu PR!" | N/A | - |

---

## Sincronización y Resolución de Problemas

| Término | 🔍 ¿Qué es? | 🎯 ¿Para qué sirve? | 💻 Ejemplo | ⚠️ Error común | 🔗 Relacionado |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **origin** | Nombre del repo remoto por defecto | Es el "apodo" que Git le da a tu repositorio en GitHub cuando clonas. Cuando dices `git push origin`, empujas hacia ahí. | `git push origin main` | N/A | - |
| **upstream** | El repositorio original (del que hiciste fork) | Se usa para mantener tu fork sincronizado con los cambios del proyecto original. Se configura una sola vez. | `git remote add upstream https://github.com/Kaia-Alenia/nerve-community.git` | N/A | - |
| **git status** | Estado actual de tu trabajo | Muestra qué archivos modificaste, cuáles están preparados (staged) y cuáles no. Úsalo antes de hacer commit. | `git status` | N/A | - |
| **Conflict (Conflicto)** | Dos versiones del mismo código chocan | Ocurre cuando tú y otra persona editaron la misma línea del mismo archivo. Git no sabe cuál versión elegir y te pide que lo resuelvas manualmente. | "CONFLICT (content): Merge conflict in archivo.py" | N/A | - |
| **Rebase** | Reorganizar historial de commits | Mueve o reaplica tus commits encima de otra rama, como si tu trabajo lo hubieras empezado después de los últimos cambios. Más avanzado que merge. | `git rebase main` | N/A | - |
| **git log** | Historial de commits | Muestra una lista de todos los commits que se han hecho en la rama actual, con autor, fecha y mensaje. | `git log --oneline` | N/A | - |
| **git diff** | Ver qué cambió exactamente | Muestra las diferencias línea por línea entre tu versión actual y la última guardada en un commit. Útil antes de hacer commit. | `git diff mi_archivo.py` | N/A | - |
| **git stash** | Guardar cambios temporalmente | "Guarda" tus cambios sin hacer commit para que puedas cambiar de rama limpiamente y recuperarlos después. | `git stash` y luego `git stash pop` | N/A | - |
| **git commit --amend** | Corregir el último commit | Modifica el mensaje o los archivos del commit que acabas de hacer, sin crear uno nuevo. Solo funciona si aún no hiciste push. | `git commit --amend -m "Mensaje corregido"` | N/A | - |

---

## GitHub: Conceptos de Plataforma

| Término | 🔍 ¿Qué es? | 🎯 ¿Para qué sirve? | 💻 Ejemplo | ⚠️ Error común | 🔗 Relacionado |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Issue** | Ticket o tarea dentro de GitHub | Un foro donde se reportan bugs, se piden funciones nuevas o se listan los retos disponibles. En Nerve Community cada reto tiene su propio Issue. | [Issue #1 — Reto 01 Chat Terminal](https://github.com/Kaia-Alenia/nerve-community/issues/1) | N/A | - |
| **Maintainer** | Mantenedor del proyecto | La persona (o equipo) que tiene permisos para hacer merge de PRs y tomar decisiones sobre el proyecto. Alejandro es el maintainer de Nerve Community. | `@Alenia-Studios` | N/A | - |
| **Contribuidor (Contributor)** | Persona que ha enviado código | Cualquier persona cuyo Pull Request haya sido aceptado (merged) en el proyecto. ¡Tú puedes ser uno! | Ver sección "Cumpliendo Retos" en el README | N/A | - |
| **Label (Etiqueta)** | Categoría de un Issue o PR | Tags de colores que clasifican un Issue. Ejemplos: `good-first-issue` (ideal para principiantes), `bug`, `disponible`. | `good-first-issue`, `python-general`, `disponible` | N/A | - |
| **Squash and Merge** | Fusionar aplastando todos los commits en uno | Cuando se hace merge de un PR, todos los commits de esa rama se "aplastan" en un solo commit limpio en `main`. | "Squashed and merged pull request #47" | N/A | - |
| **gh CLI** | GitHub CLI, la línea de comandos de GitHub | Herramienta oficial de GitHub para usar la plataforma desde la terminal: crear PRs, ver issues, autenticarte, etc. | `gh pr create`, `gh auth login`, `gh pr list` | N/A | - |
| **GitHub Actions** | Automatizaciones del repositorio | Scripts automáticos que se ejecutan cuando ocurre algo en el repo (ej: alguien abre un PR). En Nerve Community, se usa para revisar formato del código automáticamente. | El Linter Compasivo que formatea Python con `black` | N/A | - |
| **README.md** | El archivo de presentación del repo | Es el primer archivo que GitHub muestra al entrar a un repositorio. Explica qué es el proyecto, cómo usarlo y cómo contribuir. | Este mismo archivo que estás leyendo | N/A | - |
| **Sparse-Checkout** | Clonar solo una carpeta específica | Técnica avanzada para descargar únicamente la parte del repositorio que necesitas, en vez de todo el proyecto. Ideal si tienes datos limitados (ej: en Termux). | `git sparse-checkout set retos/general/01-lista-de-tareas-cli` | N/A | - |
| **.gitignore** | Archivo de ignorados | Un archivo especial que le dice a Git qué archivos o carpetas NO debe rastrear ni subir (ej. contraseñas, dependencias como `node_modules`). | Archivo llamado `.gitignore` | N/A | - |

---

> 💡 **IMPORTANTE:** No tienes que memorizar todo esto de golpe. Con que recuerdes el ciclo básico — **fork → clone → branch → commit → push → PR** — ya puedes hacer tu primera contribución. ¡El resto lo aprenderás con la práctica! 🚀

---

← [Volver al Índice del Glosario](README.md)
