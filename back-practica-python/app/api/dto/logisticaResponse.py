from pydantic import BaseModel,Field
from datetime import date


class logisticaResponse(BaseModel):
    id:int
    nombreEncargado:str
    correoEncargado:str
    contactoEncargado:str
    fechaRecepcion:date
    detalles:str