from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import jwt, JWTError
from passlib.context import CryptContext  #contexto de encriptación
from datetime import datetime, timedelta  #para calcular el tiempo de expiración del token

#se instala pip install "python-jose[cryptography]"
#se instala pip install "passlib[bcrypt]" se va a usar este algoritmo de encriptación

ALGORITHM = "HS256" #se puede revisar la pagina de jwt tokken para ver los diferentes codigos de algoritmos
ACCESS_TOKEN_DURATION = 1
SECRET = "201d573bd7d1344d3a3bfce1550b69102fd11be3db6d379508b6cccc58ea230b"



router = APIRouter()
oauth2 = OAuth2PasswordBearer(tokenUrl="login")

crypt = CryptContext(schemes="bcrypt")  #contexto de encriptación -- bcrypt contiene el algoritmo de encriptación

#reutilizacoms conceptos de la autenticación básica (basic_auth_users.py)

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
        "password": "$2a$12$Me48ZcpvypqDc3YhFE2REevnU3b8kxeaPIbjesVPfsHOh9T5b7ANi"
    },
    "4dev.manu2": {
        "username": "4dev.manu2",
        "fullname": "Manuel Villate 2",
        "email": "manuel.villater2@gmail.com",
        "disable": True,
        "password": "$2a$12$Ko.yneEX6m8uZUwfaju/.uhsoxn8Azc8waVvbm/PXvxw8M/AvUZ7."
    }
}

def search_user_db(username:str):
    if username in users_db:
        return UserDB(**users_db[username])
    
def search_user(username:str):
    if username in users_db:
        return User(**users_db[username])
    
async def auth_user(token:str = Depends(oauth2)):

    exception =  HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Invalid authorization credential",
                            headers= {"WWW-Authenticate":"Bearer"})

    try:

        username = jwt.decode(token, SECRET, algorithms=[ALGORITHM]).get("sub") 
        if username is None:
           raise exception
    
    except JWTError:
        raise exception
    
    return search_user(username)

         

    
async def current_user(user: User = Depends(auth_user)):

       
    if user.disable:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="Inactive user")


    return user

@router.post("/login")
async def login(form: OAuth2PasswordRequestForm = Depends()):

    user_db = users_db.get(form.username)
    if not user_db:
        raise HTTPException(
            status_code= status.HTTP_400_BAD_REQUEST, detail= "Wrong user"
        )
    
    user = search_user_db(form.username)
    
    
    #se le pasa la contraseña original que viene en el formulario y la encriptada que esta en la base de datos

    if not crypt.verify(form.password, user.password):
        raise HTTPException(
            status_code= status.HTTP_400_BAD_REQUEST, detail="Wrong password")
    
    #acces_token_expiration = timedelta (minutes= ACCESS_TOKEN_DURATION)

    
    """
    Para que expire el token se toma la hora actual del sistema con "datetime.utcnow ()"
    y se le suma el tiempo de duración que se quiera.

     jwt.encode(access_token, algorithm=ALGORITHM) para encriptar el token
    """

    access_token = {"sub": user.username, "exp": datetime.utcnow () + timedelta(minutes= ACCESS_TOKEN_DURATION)}    
    
    return {"access_token": jwt.encode(access_token, SECRET, algorithm=ALGORITHM), "token_type":"bearer"}
    

@router.get("/users/me")
async def me(user: User = Depends(current_user)):
        
    return user