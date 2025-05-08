from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


Base=declarative_base()

class Logistica(Base):
    __tablename__ = 'logistica'
    id= Column(Integer, primary_key=True, autoincrement=True)
    nombreEncargado= Column(String(50))
    correoEncargado= Column(String(100))
    contactoEncargado= Column(String(50))
    fechaRecepcion= Column(Date)
    detalles= Column(String(200))


class Proveedor(Base):
    __tablename__ = 'proveedor'
    id= Column(Integer, primary_key=True, autoincrement=True)
    nombres= Column(String(50))
    documento= Column(String(20))
    direccion= Column(String(50))
    ciudad=Column(String(20))
    representante= Column(String(50))
    telefono= Column(String(20))
    correo= Column(String(50))
    fechaReparto= Column(Date)
    costoEnvio= Column(Integer)
    descripcion= Column(String(200))