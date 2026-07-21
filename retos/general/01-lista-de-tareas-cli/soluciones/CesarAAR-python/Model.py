from pydantic import BaseModel, StrictBool, Field


class Tareas(BaseModel):
    id: int = Field(ge=1)  # ge = greater than or equal to, mayor o igual a 1
    titulo: str
    description: str
    estado: StrictBool  # Se limita a solo True o False; True = Completado, False = Pendiente.
