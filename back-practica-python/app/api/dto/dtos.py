from pydantic import BaseModel,Field
from datetime import date

#los dto, son objetos de transferencia de datos
class ProveedorDTO(BaseModel):
    nombres:str
    documento:str
    direccion:str
    ciudad:str
    representante:str
    telefono:str
    correo:str
    fechaReparto:date
    costoEnvio:int
    descripcion:str



class ProveedorResponse(BaseModel):
    id:int
    nombres:str
    documento:str
    direccion:str
    ciudad:str
    representante:str
    telefono:str
    correo:str
    fechaReparto:date
    costoEnvio:int
    descripcion:str



class LogisticaDTO(BaseModel):
    nombreEncargado:str
    correoEncargado:str
    contactoEncargado:str
    fechaRecepcion:str
    detalles:str
    

class logisticaResponse(BaseModel):
    id:int
    nombreEncargado:str
    correoEncargado:str
    contactoEncargado:str
    fechaRecepcion:str
    detalles:str