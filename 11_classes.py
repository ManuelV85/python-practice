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
        self.name = name
        self.surname = surname

#en el siguiente ejemplo de clase, se crea una propiedad almacenada que es full_name

my_person = Person("manuel", "Villate")  #a la variable le asigno la clase
print(my_person.name)
print(f"{my_person.name} {my_person.surname}")

class PersonFull:
    def __init__(self, name, surname,):
        self.full_name = f"{name} {surname}"

#puedo crear funciones 
#la función dentro de la clase le podemos parsar el parametro self.
    def walk(self):
        print(f"{self.full_name} esta caminando")

my_person_full = PersonFull("Manuel", "Villate")
print(my_person_full.full_name)
my_person_full.walk() #forma de llamar a la función

#le podemos pasar valores por defecto "alias"
class PersonFull:
    def __init__(self, name, surname, alias = "4dev.manu"):
        self.full_name = f"{name} {surname} ({alias})"
        self.__name = name #propiedad privada: no se puede acceder para modificar

    def get_name(self):
        return self.__name  #forma de solo ver el valor que contiene name

#puedo crear funciones 
#la función dentro de la clase le podemos parsar el parametro self.
    def walk(self):
        print(f"{self.full_name} esta caminando")

my_person_full = PersonFull("Manuel", "Villate")
print(my_person_full.full_name)
print(my_person_full.get_name())
my_person_full.walk() #forma de llamar a la función

my_person_full.full_name = "Solangel (La loca del cel)"
print(my_person_full.full_name)





        
