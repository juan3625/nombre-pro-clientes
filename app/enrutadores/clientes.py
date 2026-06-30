from fastapi import APIRouter, HTTPException  
from modelos.clientes import Cliente, ClienteCrear, ClienteEditar
from listas import lista_clientes 
from conexion_bd import Session_dependencia
from sqlmodel import select

rutas_clientes = APIRouter()  
#lista_clientes: list[Cliente] = []


@rutas_clientes.get("/clientes", response_model=list[Cliente])
async def listar_clientes(sesion: Session_dependencia):
    lista_cli = sesion.exec(select(Cliente)).all()
    return lista_cli


@rutas_clientes.get("/clientes/{cliente_id}", response_model=Cliente)
async def listar_cliente(cliente_id: int, mi_sesion: Session_dependencia):
    for i, obj_cliente in enumerate(lista_clientes):
        if obj_cliente.id == cliente_id:
            return obj_cliente
    raise HTTPException(
        status_code=400, detail=f"El cliente con id{cliente_id}, no esxiste,"
    )


@rutas_clientes.post("/clientes", response_model=Cliente)
async def crear_cliente(datos_cliente: ClienteCrear, mi_sesion: Session_dependencia):
    Cliente_val = Cliente.model_validate(datos_cliente.model_dump())
    mi_sesion.add(Cliente_val)
    mi_sesion.commit()
    mi_sesion.refresh(Cliente_val)
    return Cliente_val


@rutas_clientes.patch("/clientes{cliente_id}", response_model=Cliente)
async def editar_cliente(cliente_id: int, datos_cliente: ClienteEditar):
    for i, obj_cliente in enumerate(lista_clientes):
        if obj_cliente.id == cliente_id:
            Cliente_val = Cliente.model_validate(datos_cliente.model_dump())
            Cliente_val.id = cliente_id
            lista_clientes[i] =  Cliente_val
            return Cliente_val
    raise HTTPException(
        status_code=400, detail=f"El cliente con id {cliente_id}, no existe."
    )


@rutas_clientes.delete("/clientes{cliente_id}", response_model=Cliente)
async def eliminar_cliente(cliente_id: int):
    for i, obj_cliente in enumerate(lista_clientes):
        if obj_cliente.id == cliente_id:
            Cliente_eliminado = lista_clientes.pop(i)
            return Cliente_eliminado
    raise HTTPException(
        status_code=400, detail=f"El cliente con id {cliente_id}, no existe."
    )
