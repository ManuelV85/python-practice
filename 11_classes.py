 ### CLASSES ###

#Todo lo que esta dentro de una clase, debe responder a cierta lógica.
#forma de definir una clase
#la clase se debe declarar con la primera letra en mayuscula por buena practica. Por lo tanto los nombres de las clases
#se deben escribir en camel case.
#La clase puede tener constructores, pueden recibir parametros.

class MyEmptyPerson: 

    pass

print(MyEmptyPerson)  #se puede dar print de las 2 formas para la clase
print(MyEmptyPerson()) #los () seran necesarios cuando se tenga que pasar algo

class Person:
    def __init__(self, name, surname):  #constructor de la clase
        pass 

my_person = Person("manuel", "Villate")  #a la variable le asigno la clase
print(my_person)
