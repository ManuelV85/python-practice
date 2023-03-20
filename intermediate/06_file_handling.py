### File Handling ###

# .txt file

import os

my_file = "./my_file.txt"
txt_file = open(my_file, "w+") #si es archivo (file) no esta creado.... esto lo crea revisar (w+, r+)
#para imprimir por consola se debe comentar la linea 10 y cambiar w+ por r
txt_file.write("Mi nomnre es Manuel\n Mi apellido es Villate\n mi alias manu.dev\n mi edad 37 años \n y mi lenguaje favorito es python") #agrega la información al archivo nuevo
print(txt_file.read())
#print(txt_file.read(10)) #solo lee los 10 espacios de la primera linea
print(txt_file.readline) #lectura linea a linea del fichero
for line in txt_file.readlines(): #otra forma de llamar a todas las lineas del file.txt
    print(line)


txt_file.write("\n Aunque tambien JS")
print(txt_file.readline())

txt_file.close()

txt_file = open(my_file, "r+")
print(txt_file.read())

#os.remove(my_file)#se  guarda la ruta en la variable o se puede poner de forma directa
"""
proceso: se crea fichero, se escribe en el fichero, se cierra el fichero y se elimina.
si se quiere ver el fichero se debe descomentar la linea 23
"""


# .json file

import json

my_file2= "./my_file2.json"
json_file = open(my_file2, "w+") 
"""
json_file = open(my_file2, "w+") : si en el fichero json tengo algo escrito, borra el contenido
ya que, esto crea un fichero desde 0
"""
json_text =  {
    "name": "Manuel", 
    "surname": "Villate",
    "age":37,
    "language":["Python", "JS", "CCS", "HTML"]

}

#para escribir en el fichero json y el indent es para hacer identación.(revisar documentación de identación)
#el numero que se agrega en indent es para poner espacios delante
json.dump(json_text, json_file, indent=2 ) 

json_file.close()

with open(my_file2) as my_other_file:
    for line in my_other_file.readlines():
        print(line)

json_dic = json.load(open(my_file2))
print(json_dic)
print(type(json_dic))
# se paso una clase diccionario al fichero json y luego se recupero del fichero json a un diccionario 
print(json_dic["name"])


# .csv file
import csv

csv_file = open("./my_file3.csv", "w+")
csv_writer = csv.writer(csv_file)
csv_writer.writerow(["name", "surname", "age", "language", "alias"])
csv_writer.writerow(["Manuel", "Villate", 37, "python", "manu.dev"])


# .xlsx file
#import xlrd debe instalarse el modulo

# .xml file 
import xml

xml_file = open("./file4.xml", "w+")
#buscar en la documentación como leer y escribir