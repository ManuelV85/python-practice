from fastapi import FastAPI, Depends, HTTPException, status
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

#OAuth2PasswordBearer: Es la clase que se va a encargar de gestionar la autenticación de usuario y contraseña
#OAuth2PasswordRequestForm Es la forma en que se va a enviar a nuestro backend los criterios de autenticación. Es la 
#forma en que el cliente envia usuario y contraseña y el backend captura esta información.

app = FastAPI()

oauth2 = OAuth2PasswordBearer(tokenUrl="login")

class User(BaseModel):
    username: str
    fullname: str
    email: str
    disable: bool


class UserDB(User):
    password: str


users_db = {

    "4dev.manu": {
        "username": "4dev.manu",
        "fullname": "Manuel Villate",
        "email": "manuel.villater@gmail.com",
        "disable": False,
        "password": "123456"
    },
    "4dev.manu2": {
        "username": "4dev.manu2",
        "fullname": "Manuel Villate 2",
        "email": "manuel.villater2@gmail.com",
        "disable": True,
        "password": "654321"
    }
}

def search_user_db(username:str): #como se esta trabajando con FastApi, es importante recordar tipar todos los datos
    if username in users_db:
        return UserDB(**users_db[username]) #los ** indican que se pueden enviar varios parametros
    
def search_user(username:str): 
    if username in users_db:
        return User(**users_db[username])

#criterio de dependencia 

async def current_user(token: str = Depends(oauth2)):
    user = search_user(token)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Invalid authorization credential",
                            headers= {"WWW-Authenticate":"Bearer"})
    
    if user.disable:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="Inactive user")


    return user
   

   


#operación de autenticación
#los datos que se van a obtener es debido a que se envian datos (usuario y contraseña), por lo tanto se debe usar post

@app.post("/login")
async def login(form: OAuth2PasswordRequestForm = Depends()):
#para capturar el usuario y la contraseña vamos a usar OAuth2PasswordRequestForm
#Depends: dependencia del sistema de autenticación. Significa que la operación va a recibir datos pero no depende de nadie

  
   user_db = users_db.get(form.username)
   if not user_db:
       raise HTTPException(status_code = 404, detail ="Wrong user")
   
   user = search_user_db(form.username)
   
   #ahora se debe comprobar que la contraseña que llego coincida con la base de datos.
   if not form.password == user.password:
       raise HTTPException(status_code = 404, detail ="Wrong  password")
   
   #cuando el usuario se identifica de forma correcta, se debe devolver un acces token

   return {"access_token": user.username, "token_type":"bearer"}

@app.get("/users/me")
async def me(user: User = Depends(current_user)):
    return user

"""
Para empezar a consumir la API, una vez se haya generado un token, se haya autenticado correctamente y se devuelva el access token,
ahora se tendra que validar que el access token sea el correcto.

"""

"""
- para generar el token, hacemos el llamado (thunderclient) /login, luego seleccionamos body -> form donde tenemos que pasar
los datos que se solicitan para generar el token
"""