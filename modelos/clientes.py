from pydantic import BaseModel

class ClienteBase(BaseModel):
    nombre: str
    email:str
    descripcion: str

    class ClienteCrear(ClienteBase):
        pass
        
    class cliente(ClienteBase):
        id: int | None = None