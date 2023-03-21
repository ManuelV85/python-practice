from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# para levantar el server "uvicorn users:app --reload"

# Entidad user
#BaseModel genera la capacidad de crear una entidad.

class User(BaseModel):
    id: int
    name: str
    surname: str
    url: str
    age: int

users_list = [User(id = 1, name="Manuel", surname="Villate",url="https://github.com/ManuelV85", age=37 ),
         User(id = 2, name="Solangel", surname="Villate",url="https://github.com/ManuelV85", age=8 ),
         User(id = 3, name="Angelo", surname="Villate",url="https://github.com/ManuelV85", age=2 )]

#ejemplo
@app.get("/usersjson")
async def usersjson():
    return [{"name":"Manuel", "surname":"Villate", "url":"https://github.com/ManuelV85", "age":37},
            {"name":"Solangel", "surname":"Villate", "url":"https://github.com/ManuelV85", "age":8},
            {"name":"Angelo", "surname":"Villate", "url":"https://github.com/ManuelV85", "age":2},
            ]

@app.get("/users")
async def users():
    return users_list

"""
#parametros por path
@app.get("/users/{id}")
async def user(id: int):
    users = filter(lambda user: user.id == id, users_list)
    try:
        return list(users)[0]
    except:
        return {"error": "User does not exist"}

#parametros por query
#http://127.0.0.1:8000/userquery/?id=1 forma de usar query
@app.get("/userquery/")
async def user(id: int):
    users = filter(lambda user: user.id == id, users_list)
    try:
        return list(users)[0]
    except:
        return {"error": "User does not exist"}
    
    """

#otra forma de hacer lo mismo de las lineas 35 hasta la 52 es declarar una función y llamarla en el return

@app.get("/users/{id}")
async def user(id: int):
    return search_user(id)

#parametros por query
#http://127.0.0.1:8000/userquery/?id=1 forma de usar query

@app.get("/users/")
async def user(id: int):
    return search_user(id)

"""
Si se quiere buscar por otro parametro como por ejemplo el name:
@app.get("/users/")
async def user(id: int, name:str):
    return search_user(id)

y la forma de concatenar en el servidor seria: &name=Manuel
http://127.0.0.1:8000/users/?id=1&name=Manuel

"""



def search_user(id:int):
    users = filter(lambda user: user.id == id, users_list)
    try:
        return list(users)[0]
    except:
        return {"error": "User does not exist"}
