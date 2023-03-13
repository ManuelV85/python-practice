###Functions###

#con las funciones podemos encapsular logicas complejas
#la palabra recervada para la función es "def"

def my_function ():#forma de definir una función
    print("esto es una función")

my_function()
my_function()
my_function()



def sum_two_values (first_number, second_number):
    print(first_number + second_number)
    
sum_two_values(5,7)
sum_two_values(51235123,7512315 ) 

#las funciones pueden recibir parametros pero tambien los puede retornar.

def sum_two_values_with_return (first_value, second_value):
    return first_value + second_value

my_result = sum_two_values_with_return(10, 5) #llamo la función con los parametros (10,5) y
                                              #el resultado lo puedo guardar en una variable

print(my_result)  #imprime la variable con los resultados guardados.


def print_name(name, surname):
    print(f"{name} {surname}")

print_name("manuel", "villate")

def print_name_with_default(name, surname, alias = "sin alias"):
    print(f"{name} {surname} {alias}")

print_name_with_default("manuel", "villate", "4dev.manu")
#aunque se asigna "sin alias" en la función, igual me imprime 4dev.manu, por que es un valor por defecto.
#pero si quito ese valor por defecto, me imprime lo que tiene asignado el alias.

def print_name_with_default(name, surname, alias = "sin alias"):
    print(f"{name} {surname} {alias}")

print_name_with_default("manuel", "villate")


def print_texts(*texts): #cuando se antepone "*", se pueden pasar todos los parametros que se quiera
    print(texts)          #es un parametro dinamico

print_texts("hola", "python", "manuel")

def print_upper_texts(*texts): 
    for text in texts:
        print(text.upper())

print_upper_texts("hola", "python", "manuel")