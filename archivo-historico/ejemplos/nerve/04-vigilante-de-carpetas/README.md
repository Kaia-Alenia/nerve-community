# Vigilante de Carpetas (File Watcher)

**¿Qué muestra este ejemplo?**
Muestra cómo utilizar librerías nativas o de terceros para monitorear una carpeta y detectar cuándo se crean, modifican o eliminan archivos dentro de ella.

**¿Por qué es útil?**
Muchos sistemas modernos necesitan reaccionar a cambios en tiempo real (por ejemplo, subir un archivo automáticamente cuando se guarda, o recargar una web al cambiar el código).

**Librerías usadas por lenguaje:**
- **Python**: `watchdog` (terceros, `pip install watchdog`)
- **Node.js/JavaScript**: `fs.watch` o `chokidar` (terceros, `npm install chokidar`)
- **Go**: `fsnotify` (terceros, `go get github.com/fsnotify/fsnotify`)
- **Rust**: `notify` (terceros, `cargo add notify`)

**¿Qué retos usan esta base?**
- [Reto 04 — Vigilante de carpetas](https://github.com/Kaia-Alenia/nerve-community/issues/4)
