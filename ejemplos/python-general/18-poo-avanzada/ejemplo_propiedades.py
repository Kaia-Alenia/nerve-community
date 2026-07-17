class Libro:
    def __init__(self, titulo: str, autor: str, año_publicacion: int):
        self.titulo = titulo
        self.autor = autor
        self.año_publicacion = año_publicacion

    @property
    def resumen(self) -> str:
        """
        Una propiedad computada de SOLO LECTURA.
        No guarda el string 'resumen' en memoria, lo calcula al vuelo
        cada vez que se consulta.
        """
        return f"'{self.titulo}' escrito por {self.autor} en {self.año_publicacion}."

if __name__ == "__main__":
    # Instanciamos la clase Libro
    mi_libro = Libro("El Principito", "Antoine de Saint-Exupéry", 1943)
    
    # Consultamos atributos normales
    print(f"Título: {mi_libro.titulo}")
    
    # Consultamos la @property. Nota que NO se usan paréntesis como en resumen()
    # Se consulta igual que si fuera un atributo estático.
    print(f"Resumen: {mi_libro.resumen}")
    
    # Si intentamos reasignar una @property sin un @setter definido, Python dará error:
    try:
        mi_libro.resumen = "Otro resumen inventado"
    except AttributeError as e:
        print("\n❌ Error esperado al intentar sobreescribir la propiedad:")
        print(f"   {e}")
