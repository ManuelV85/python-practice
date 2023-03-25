#Este fichero se encargará de hacer la conexión de la base de datos con mongodb

from pymongo import MongoClient

db_client = MongoClient().local