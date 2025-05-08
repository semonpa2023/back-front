from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session
from typing import List
from fastapi.params import Depends

from app.api.dto.proveedorDto import ProveedorDTO
from app.api.dto.proveedorResponse import ProveedorResponse
from app.api.dto.logisticaDto import LogisticaDTO
from app.api.dto.logisticaResponse import logisticaResponse

from app.api.models.logistica import Logistica, Proveedor
#from app.api.models.proveedor import Proveedor

from app.database.connection import SessionLocal, engine


rutas=APIRouter()

#Rutina para conectarnos a la base de datos 
def conectarConBd():
    try:
        baseDeDatos=SessionLocal()
        yield baseDeDatos
    except Exception as error:
        baseDeDatos.rollback() #break
        raise error #levanto el error es como un thrw Exception en java
    finally:
        baseDeDatos.close()

#Rutina para construir servicios web
@rutas.post("/proveedor", response_model=ProveedorResponse, summary="Servicio para crear un nuevo proveedor")
def guardarProveedor(datosProveedor:ProveedorDTO , database:Session=Depends(conectarConBd)):
    try:
        proveedorToSave=Proveedor(
            nombres=datosProveedor.nombres,
            documento=datosProveedor.documento,
            direccion=datosProveedor.direccion,
            ciudad=datosProveedor.ciudad,
            representante=datosProveedor.representante,
            telefono=datosProveedor.telefono,
            correo=datosProveedor.correo,
            fechaReparto=datosProveedor.fechaReparto,
            costoEnvio=datosProveedor.costoEnvio,
            descripcion=datosProveedor.descripcion,
        )
        database.add(proveedorToSave)
        database.commit()
        database.refresh(proveedorToSave)

        proveedor_response = ProveedorResponse(**proveedorToSave.__dict__)
        return proveedor_response
        
    except Exception as error:
        database.rollback()
        raise HTTPException(status_code=400, detail=f"Error al guardar el proveedor: {error}")


@rutas.post("/logistica", response_model=logisticaResponse, summary="Servicio para crear una neuva logistica")
def guardarLogistica(datosLogistica:LogisticaDTO, database:Session=Depends(conectarConBd)):
    try:
        logisticaToSave=Logistica(
            nombreEncargado=datosLogistica.nombreEncargado,
            correoEncargado=datosLogistica.correoEncargado,
            contactoEncargado=datosLogistica.contactoEncargado,
            fechaRecepcion=datosLogistica.fechaRecepcion,
            detalles=datosLogistica.detalles,        
        )
        database.add(logisticaToSave)
        database.commit()
        database.refresh(logisticaToSave)

        logistica_response = logisticaResponse(**logisticaToSave.__dict__)
        return logistica_response
    except Exception as error:
        database.rollback()
        raise HTTPException(status_code=400, detail=f"Error al guardar la logistica: {error}")
    

    #rutina para consultar los proveedores
@rutas.get("/consultarProveedores",response_model=List[ProveedorResponse], summary="Servicio para consultar los proveedores")
def buscarProveedores(database:Session=Depends(conectarConBd)):
    try:
        proveedores=database.query(Proveedor).all()
        return proveedores
    except Exception as error:
        database.rollback()
        raise HTTPException(status_code=404, detail=f"Error al consultar los proveedores: {error}")
    

@rutas.get("/consultarLogisticas",response_model=List[logisticaResponse], summary="Servicio para consultar las logisticas")
def buscarLogisticas(database:Session=Depends(conectarConBd)):
    try:
        logisticas=database.query(Logistica).all()
        return logisticas
    except Exception as error:
        database.rollback()
        raise HTTPException(status_code=404, detail=f"Error al consultar las logisticas: {error}")
