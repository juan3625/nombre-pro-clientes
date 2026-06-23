from fastapi import FastAPI, Depends
from typing import Annotated
from sqlmodel import Session, SQLModel, create_engine

nombre_bd = "bd_clientes.squlite3"
url_bd = f"sqlite:///{nombre_bd}"


motor_bd = create_engine(url_bd)

#definir el metodo para crear las tablas 
def crear_tablas(app: FastAPI):
    SQLModel.metadata.create_all(motor_bd)
    yield

#definir el metodo para la sesion
def obtener_sesion():
    with Session(motor_bd) as mi_sesion:
        yield mi_sesion

#Denominado inyeccion de dependecias
#registrar la sesion como dependencia
Session_dependencia = Annotated[Session, Depends(obtener_sesion)]
