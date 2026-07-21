from pydantic import BaseModel, StrictBool, Field


class Tareas(BaseModel):
    id: int = Field(minimum=0)
    titulo: str
    description: str
    estado: StrictBool  # Se limita a solo True o False; True = Completado, False = Pendiente.
