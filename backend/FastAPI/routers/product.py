#from fastapi import FastAPI
# como se va a trabajar con rutas se importa APIRouter en vez de FastAPI
from fastapi import APIRouter


#app = FastAPI()
router = APIRouter(prefix="/product", tags=["product"], responses= {404:{"message": "Not Founded"}})
#indico en el prefijo la ruta base y la puedo eliminar de las rutas

product_list = ["product 1", "product 2", "product 3", "product 4", "product 5"]

#@router.get("/product/")
@router.get("/")
async def product():
    return product_list

#@router.get("/product/{id}")
@router.get("/{id}")
async def product(id:int):
    return product_list[id]