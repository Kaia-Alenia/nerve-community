# Solución 01 lista de tareas CLI

La solución usa librerias como Pandas para el manejo de csv (importación/exportación) y un manejo más limpio de las tareas por medio de dataframes.

## Opciones

Existen las siguientes opciones en el código:
1. Insertar Tarea.
2. Modificar Tarea. 
3. Actualizar Estado de Tarea. 
4. Eliminar Tarea. 
5. Ver Tarea Específica.
6. Ver Lista de Tareas.
7. Importar lista desde un archivo CSV.
8. Salir (Exporta y actualiza el csv subido.)

## Estructura
```text
CesarAAR-python/
├── Functions.py       # Módulos con funciones secundarias
├── Main.py
├── Model.py           # Definición de modelos o lógica de datos
├── README.md
├── requirements.txt   # Los requerimientos para ser instalados.
└── test.csv           # Un csv para que vea la estructura del documento.
```

### Aclaraciones

La columna estado puede ser True|False.
- True = Completado.
- False = Pendiente.