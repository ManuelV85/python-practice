from fastapi import APIRouter, HTTPException, status
from db.models.user import User
from db.schemas.user import user_schema, users_schema
from db.client import db_client



router = APIRouter(prefix="/userdb", tags=["userdb"], responses= {404:{"message": "Not Founded"}})

# para levantar el server "uvicorn users:app --reload"

# Entidad user
#BaseModel genera la capacidad de crear una entidad.


users_list = []
"""
users_list = [User(id = 1, name="Manuel", surname="Villate",url="https://github.com/ManuelV85", age=37 ),
         User(id = 2, name="Solangel", surname="Villate",url="https://github.com/ManuelV85", age=8 ),
         User(id = 3, name="Angelo", surname="Villate",url="https://github.com/ManuelV85", age=2 )]
"""


@router.get("/")
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

@router.get("/{id}")
async def user(id: int):
    return search_user(id)

#parametros por query
#http://127.0.0.1:8000/userquery/?id=1 forma de usar query

@router.get("/")
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

@router.post("/",status_code=status.HTTP_201_CREATED)
async def user(user: User):
    #si el usuario existe no lo agrega y arroja el error, de lo contrario lo agrega 
    if type(search_user_by_email(user.email)) == User:
        raise HTTPException(status_code = 404, detail ="Users already exist")

    user_dict = dict(user)
    del user_dict["id"] #para eliminar el id y que mongodb genere automaticamente un id.

    id = db_client.local.users.insert_one(user_dict).inserted_id
    #inserted_id genera un id automatico en mongodb
    #local es la carpeta que esta dentro de la base de datos local en mongo 
    
    new_user = user_schema(db_client.local.users.find_one({"_id": id})) #la clave unica mongodb la genera de esta manera _id

    return User(**new_user) 

#HTTException se debe importar de FastAPI


# PUT 

@router.put("/")
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

@router.delete("/{id}")
def user (id:int):

    found = False

    for index, saved_user in enumerate(users_list):
        if saved_user.id == id:
            del users_list[index]
            found = True
            return "Deleted susscefull"
        
    if not found:
         return {"error": "User not deleted"}



#va a ser el criterio, para verificar que no se repita el usuario

def search_user_by_email(email : str):
    
    
    try:
        user = db_client.local.users.find_one({"email" : email})
        return User(**user_schema(user))
    except:
        return {"error": "User does not exist"}

"""
Por lo general el path se usa para parametros que estan fijos y 
el query para parametros que pueden que no sean necesarios para hacer una petición por ejemplo
revisar varias publicaciones las cuales se pueden llamar (ejemplo) de las 1 a la 10.
"""
