from pydantic import BaseModel,Field
from datetime import date

class LogisticaDTO(BaseModel):
    nombreEncargado:str
    correoEncargado:str
    contactoEncargado:str
    fechaRecepcion:date
    detalles:str
    