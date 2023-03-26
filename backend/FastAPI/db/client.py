#Este fichero se encargará de hacer la conexión de la base de datos con mongodb

from pymongo import MongoClient


#Base de datos local
#db_client = MongoClient().local

"""
Como el cliente apunta a la base de datos local....  cuando se llame a de_client se puede hacer 
id = db_client.users.insert_one(user_dict).inserted_id, sin el local... ya que se hace referencia.
"""

#Base de datos remota.

db_client = MongoClient(
    "mongodb+srv://test:test123@cluster0.koonogc.mongodb.net/?retryWrites=true&w=majority").test 