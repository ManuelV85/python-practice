### Error types ###

"""
Se revisan los errores y la solución que se presenta en consola.
"""

# SyntaxError

# print "Hola comunidad"  #Error
print("Hola comunidad") #Solución

#NameError

#print(var) #como la variable ono esta definida, genera el error.
var = "variable"
print(var)

#IndexError

my_list = ["python", "js", "css", "HTML", "flask"]
print(my_list[3])
print(my_list[-1]) #recorre la lista de derecha a izquierda
print(my_list[2])
#print(my_list[5])  #genera el IndexError por que no esta definido el elemento.

#ModuleNotFoundError

#import maths #se intenta importar un modulo que no existe
import math 

#AtributeError

#print(math.PI) #genera error por que PI no es modulo de math
print(math.pi)

# KeyError

my_dict = {
    "Nombre": "Manuel", 
    "Apellido": "Villate",
    "Edad":37,
    1:"Python"

}
print(my_dict["Edad"])
#print(my_dict["Ead"]) #genera error en la clave (key)

# TypeError
#basicamente  es cuando se accede por un error de tipo a algo.

#print(my_list["0"])
print(my_list[0])

#ImportError

#from math import PI
from math import pi

print(pi)

# ValueError
my_int = "10"
print(type(my_int))

my_int = int("10")
print(type(my_int))

#my_int = int("10 años") #error se genera al tratar de transformar (años) a im int
#print(type(my_int))

#ZeroDivisionError

print(4/2)
#print(4/0) # error, los numeros no se pueden divir entre 0


