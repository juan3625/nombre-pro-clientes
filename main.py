from fastapi import FastAPI, HTTPException
from modelos.clientes import Cliente, ClienteCrear, ClienteEditar

app = FastAPI()

lista_clientes:list[Cliente] = []



@app.get("/clientes", response_model=list[Cliente])
async def listar_clientes():
    return lista_clientes



@app.get("/clientes/{cliente_id}", response_model=Cliente)
async def listar_cliente(cliente_id: int):
    for i, obj_cliente in enumerate(lista_clientes):
        if obj_cliente.id == cliente_id:
            return obj_cliente



@app.post("/clientes", response_model=Cliente)
async def crear_cliente(datos_cliente: ClienteCrear):
    Cliente_val = Cliente.model_validate(datos_cliente.model_dump())
    id_cliente = len(lista_clientes) + 1
    Cliente_val.id = id_cliente
    lista_clientes.append(Cliente_val)
    return Cliente_val


@app.patch("/clientes{cliente_id}", response_model=Cliente)
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