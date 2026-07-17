# ¿CÓMO HACER TU PRIMER PULL REQUEST (PR)?

Si esta es la primera vez que escuchas sobre Git, GitHub o un "Pull Request", estás en el lugar correcto. En este documento te explicaremos paso a paso y con palabras sencillas cómo contribuir a este (o a cualquier) proyecto open source.

---

##  Mini Glosario (Para que no te suene a chino)

- **Git:** Es un programa en tu computadora que actúa como una "máquina del tiempo". Guarda el historial de todos los cambios que haces en tus archivos de código.
- **GitHub:** Es una página web (una red social para programadores) donde subimos nuestro código usando Git.
- **Fork:** Es como darle al botón de "Compartir -> Crear una copia". Haces un clon exacto del proyecto de alguien más y lo guardas en tu propia cuenta.
- **Clone:** Es descargar tu "Fork" (tu copia en GitHub) hacia tu computadora física para que puedas editar los archivos.
- **Branch (Rama):** Es una línea de tiempo paralela. Creas una rama para no arruinar el código principal (`main`) mientras intentas algo nuevo.
- **Commit:** Es como un punto de guardado (Save State) en un videojuego. Guarda tus cambios permanentemente con un pequeño mensaje explicando qué hiciste.
- **Push:** Es subir tus "Commits" (puntos de guardado) de tu computadora a GitHub.
- **Pull Request (PR):** Es cuando le dices al dueño del proyecto original: *"Oye, mira estos cambios que hice en mi copia. ¿Te gustan? ¿Los quieres añadir a tu proyecto oficial?"*.

---

##  El diagrama del flujo (Visualiza el proceso)

```text
[Proyecto Original] 
       
        (1. Fork)
       
[Tu copia en GitHub] 
                           (6. Pull Request y Revisión)
        (2. Clone)        
                          
[Tu computadora]           
        (3. Branch)       
        (4. Escribir)     
        (5. Commit/Push) 
```

---

##  Preparativos (Sólo se hace una vez en la vida)

1. **Instala Git:** 
   - Windows: Descarga [Git for Windows](https://gitforwindows.org/) e instálalo.
   - Mac: Abre la terminal y escribe `git --version`. Si no lo tienes, te pedirá instalarlo.
   - Linux: Escribe `sudo apt install git` en tu terminal.
2. **Identifícate ante Git:**
   Abre tu terminal y escribe esto (cambiándolo por tu nombre y tu email de GitHub):
   ```bash
   git config --global user.name "Tu Nombre Aquí"
   git config --global user.email "tu_correo@ejemplo.com"
   ```
3. **Autentícate con GitHub:**
   GitHub ya no permite usar contraseñas normales en la terminal. La forma más amigable es instalar la [GitHub CLI (gh)](https://cli.github.com/).
   Una vez que la instales, abre tu terminal y escribe:
   ```bash
   gh auth login
   ```
   Sigue las instrucciones: elige `GitHub.com`, luego `HTTPS`, luego `Yes` para autenticar con tus credenciales, y finalmente `Login with a web browser`. Se abrirá tu navegador para dar permiso. ¡Y listo!

   *( Alternativa manual: Si no quieres instalar `gh`, debes ir a tu perfil de GitHub -> **Settings > Developer Settings > Personal access tokens > Tokens (classic)**, generar un nuevo token marcando la casilla "repo", y usar ese código larguísimo como si fuera tu contraseña cuando la terminal te lo pida al hacer `git push`).*

---

## ‍ Paso a Paso Práctico

### 1. El Fork
Ve arriba a la derecha de este repositorio y presiona el botón que dice **Fork**. Esto creará una copia del proyecto en `https://github.com/TU-USUARIO/nerve-community`.

### 2. El Clone
Abre tu terminal en la carpeta donde guardas tus proyectos (por ejemplo, en Documentos) y escribe:
```bash
git clone https://github.com/TU-USUARIO/nerve-community.git
cd nerve-community
```

### 3. Crear una Branch (Rama)
Nunca trabajes en la rama `main`. Vamos a crear una dimensión paralela para tu trabajo:
```bash
git checkout -b solucion-reto-01
```

### 4. Haz tus cambios
Usa tu editor de texto favorito (VS Code, Cursor, PyCharm, el bloc de notas) y escribe tu código para resolver el reto. Pruébalo.

### 5. Crea el Commit
Revisa qué archivos cambiaste:
```bash
git status
```
Dile a Git que prepare todos los archivos modificados:
```bash
git add .
```
Guarda el punto de control con un mensaje claro:
```bash
git commit -m "Termino el reto 01 de chat en terminal"
```

### 6. El Push
Sube tu rama desde tu computadora hacia tu copia en GitHub:
```bash
git push origin solucion-reto-01
```

### 7. Abre el Pull Request
Ve a la página de tu copia en GitHub. Arriba verás un banner amarillo/verde que dice "Compare & pull request". Dale clic.
Rellena la plantilla explicando qué hiciste. ¡Envía tu Pull Request!

---

##  Errores Comunes de Principiante

- **"Escribí código directamente en main por accidente":** No pasa nada. No hagas `git commit` todavía. Simplemente escribe `git checkout -b nueva-rama` y tus cambios "flotarán" a la nueva rama.
- **"Hice un commit pero me equivoqué en el mensaje":** Escribe `git commit --amend -m "Mensaje corregido"`.
- **"Dice que tengo conflictos de merge":** Esto pasa si alguien más editó los mismos archivos que tú. En VS Code, abre los archivos con conflictos y verás resaltadas las diferencias. Elige qué código quieres mantener, guarda el archivo, haz `git add .` y luego `git commit -m "Resuelve conflictos"`.

¡Tú puedes! Recuerda que nadie rompe un proyecto Open Source por accidente; para eso están las revisiones de Pull Requests. Anímate.
