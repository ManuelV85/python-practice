from fastapi import FastAPI

from routers import product, users  #importo mi archivo 
from fastapi.staticfiles import StaticFiles

app = FastAPI()


@app.get("/")
async def root():
    return "¡Hola Fast API!"

#siempre que se llame a un servidor, la función debe ser async (asincrona)
#para levantar el servidor uvicorn main:app --reload .... revisar bine la ruta de ejecición

@app.get("/url")
async def url():
    return {"url_github":"https://github.com/ManuelV85"}

#la documentación con SWAGER se crea de forma automatica con fastapi... se debe colocar /docs con el servidor levantado
#para ver la documentación de la API
# para ver la documentación con swager /docs  o con ReDoc   /redoc


# ROUTERS 

app.include_router(product.router)  #router es la instancia que se ha definido dentro del archivo product
app.include_router(users.router)
app.mount("/static", StaticFiles(directory= "static"), name="static")
