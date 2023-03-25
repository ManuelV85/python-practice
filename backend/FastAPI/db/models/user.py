from pydantic import BaseModel

class User(BaseModel):
    id: str | None
    username: str
    email: str
   
"""
el id es opcional y por eso se pone |None, por que puede ser que no llegue.
por otro lado el id en mongodb por defecto es un str 
"""