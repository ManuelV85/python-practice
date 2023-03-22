from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter(prefix="/user", tags=["user"])

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
@router.get("/usersjson")
async def usersjson():
    return [{"name":"Manuel", "surname":"Villate", "url":"https://github.com/ManuelV85", "age":37},
            {"name":"Solangel", "surname":"Villate", "url":"https://github.com/ManuelV85", "age":8},
            {"name":"Angelo", "surname":"Villate", "url":"https://github.com/ManuelV85", "age":2},
            ]

@router.get("/users")
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

@router.get("/user/{id}")
async def user(id: int):
    return search_user(id)

#parametros por query
#http://127.0.0.1:8000/userquery/?id=1 forma de usar query

@router.get("/user/")
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
# POST

@router.post("/user/",status_code=201)
async def user(user: User):
    #si el usuario existe no lo agrega y arroja el error, de lo contrario lo agrega 
    if type(search_user(user.id)) == User:
        raise HTTPException(status_code = 404, detail ="Users already exist")
    else:
        users_list.append(user)
        return user 

#HTTException se debe importar de FastAPI


# PUT 

@router.put("/user/")
async def user(user: User):

    found = False

    for index,  saved_user in enumerate(users_list):
        if  saved_user.id == user.id:
            users_list[index] = user
            found = True  
            return user  
        
    if not found:
        return{"error":"User not update"}


# DELETE

@router.delete("/user/{id}")
def user (id:int):

    found = False

    for index, saved_user in enumerate(users_list):
        if saved_user.id == id:
            del users_list[index]
            found = True
            return "Deleted susscefull"
        
    if not found:
         return {"error": "User not deleted"}





def search_user(id:int):
    users = filter(lambda user: user.id == id, users_list)
    try:
        return list(users)[0]
    except:
        return {"error": "User does not exist"}

"""
Por lo general el path se usa para parametros que estan fijos y 
el query para parametros que pueden que no sean necesarios para hacer una petición por ejemplo
revisar varias publicaciones las cuales se pueden llamar (ejemplo) de las 1 a la 10.
"""
