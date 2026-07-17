# Guía de Contribución para `nerve-community`

¡Qué emoción que quieras contribuir a este proyecto! No importa si es la primera vez que tocas código o si ya tienes años de experiencia, aquí eres bienvenido/a. 

El objetivo principal de este repositorio es **aprender**. Nadie nace sabiendo hacer Pull Requests (PRs), así que no tengas miedo de equivocarte. Sigue estos pasos y, si te trabas, ¡pregunta sin pena!

## Antes de empezar
Asegúrate de tener lo siguiente:
- Una cuenta en **GitHub**.
- **Git** instalado en tu computadora.
- **Python 3.10** o superior instalado.

---

## 🛠️ Paso 1: Haz un Fork
Un *fork* es hacer una copia exacta de este proyecto y ponerla en tu propia cuenta de GitHub. Así puedes experimentar y romper cosas en tu copia sin afectar el repositorio original.
Para hacerlo, ve a la página principal de este repositorio y dale clic al botón **Fork** que está arriba a la derecha.

---

## 💻 Paso 2: Clona tu fork en tu computadora
Abre tu terminal (línea de comandos) y escribe el siguiente comando, cambiando `TU-USUARIO` por tu nombre de usuario en GitHub:

```bash
git clone https://github.com/TU-USUARIO/nerve-community.git
cd nerve-community
```

---

##  Paso 3: Crea una rama nueva
**Nunca** trabajes directamente en la rama `main`. Es una buena práctica crear una "rama" (branch) separada para cada tarea o reto que vayas a resolver.

```bash
git checkout -b solucion-reto-01
```

---

##  Paso 4: Elige un reto
Ve a la pestaña de **Issues** en el repositorio original.
Busca los issues que tengan la etiqueta `good-first-issue` o `disponible`.
Si encuentras uno que te guste, deja un comentario que diga: *"¡Yo lo tomo!"* o *"Me gustaría intentar resolver esto"*. Así, evitamos que dos personas hagan el mismo reto al mismo tiempo.

---

## 📦 Paso 5: Instala dependencias y prueba que todo funcione
Crea un entorno virtual e instala lo necesario (si tu reto lo requiere):

```bash
# En Windows:
python -m venv env
.\env\Scripts\activate

# En Mac / Linux:
python3 -m venv env
source env/bin/activate

# Instalar Nerve (ejemplo):
pip install alenia-nerve
```

---

##  Paso 6: Escribe tu código
Entra a la carpeta correspondiente a tu reto (por ejemplo `retos/nerve/01-chat-terminal/`).
Dentro de esa carpeta encontrarás el archivo `README.md` con las instrucciones del reto.

Para guardar tu solución, debes crear una carpeta dentro de `soluciones/` en la raíz del repositorio siguiendo la convención `TuUsuario-Lenguaje`. Por ejemplo:
- `soluciones/Tacos-python/`
- `soluciones/Maria-rust/`
- `soluciones/Juan-go/`
- `soluciones/Ana-js/`

Dentro de tu carpeta personal, puedes crear los archivos necesarios para resolver el reto. ¡Diviértete programando!

### 🛠️ Instrucciones por Lenguaje

**Python:**
- Se recomienda crear un entorno virtual (`python -m venv env`).
- Si instalas dependencias, recuerda exportarlas en un `requirements.txt`.

**Rust:**
- Usa `cargo new tu-proyecto` para crear tu proyecto dentro de tu carpeta de solución.
- Verifica tu código con `cargo clippy` y formatéalo con `cargo fmt`.

**Go:**
- Inicializa tu módulo con `go mod init <nombre>`.
- Formatea tu código usando `go fmt ./...`.

**JavaScript (Node.js):**
- Inicializa tu proyecto con `npm init -y`.
- Es buena práctica usar `eslint` o `prettier` para mantener el código limpio.

---

##  Paso 7: Guarda tus cambios (Commit)
Una vez que termines y pruebes que funciona, debes guardar tus cambios en git. Asegúrate de escribir un mensaje claro de lo que hiciste.

```bash
git add .
git commit -m "Agrega solución al reto 01: chat-terminal"
```

---

##  Paso 8: Sube tu rama a tu fork
Ahora envía los cambios guardados desde tu computadora a tu repositorio en GitHub:

```bash
git push origin solucion-reto-01
```

---

##  Paso 9: Abre el Pull Request
Ve a tu repositorio fork en GitHub. Verás un botón verde gigante que dice **Compare & pull request**. ¡Dale clic!
- Llena la plantilla del PR.
- Menciona qué número de Issue estás resolviendo (ejemplo: `Closes #1`).
- Añade una captura de pantalla si tu código hace algo visual.

---

## ⏳ Paso 10: Espera revisión
Los mantenedores del proyecto revisaremos tu PR. 
Es **súper normal** que te pidamos hacer algún cambio o corrección. No te lo tomes a mal, ¡no es un rechazo! Es simplemente la mejor forma de darte *feedback* y aprender juntos. Haz los cambios en tu computadora, haz otro `commit`, haz `push` y el PR se actualizará solo.

---

## ❓ Preguntas frecuentes

- **¿Y si ya alguien más resolvió el reto que quería?**
¡No pasa nada! A veces aceptamos múltiples soluciones si tienen enfoques distintos, o simplemente puedes elegir otro reto. Pregúntanos en el Issue si tienes dudas.

- **¿Y si mi código no es perfecto?**
¡Mejor! El código perfecto no existe. Lo importante es que funcione, que intentes aprender algo nuevo y que pierdas el miedo a compartirlo.

- **¿Puedo proponer un reto nuevo?**
¡Sí! Ve a los Issues, elige "Propuesta de nuevo reto" y cuéntanos tu idea.

---

### ¡Los errores son bienvenidos!
Si algo sale mal con un comando de Git o con tu código, dínoslo. El propósito de `nerve-community` es crecer en comunidad. ¡Mucho éxito con tu primer PR!
