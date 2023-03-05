#variable

my_string_variable = "My string variable"
print(my_string_variable)

#print puede llevar varios argumentos separados por una ","
#concatención de variables en un print 
my_int_variable = 5
my_bool_variable = True
print(my_int_variable, my_bool_variable)
print(type(my_int_variable), type(my_bool_variable), type(my_bool_variable))

#se puede transformar una variable int en un str

my_int_to_str_variable = str(my_int_variable)
print(my_int_to_str_variable) #es un str pero aun asi imprime un numero, el cual no se puede usar como numero
print(type(my_int_to_str_variable)) #para mostrar que la variable int ahora es str
print(type(print(my_int_to_str_variable))) #imprime NoneType
print("este es el valor de:", my_bool_variable)

 #Algunas funciones del sistema
print(len(my_string_variable))
print(len(my_int_to_str_variable))

#variables en una linea (mala practica)
name, surname, alias, age = "manuel", "villate", "manu", 37
print(name, surname, alias, age)

print("me llamo:", name, surname, "mi alias:", alias, "y mi edad:", age)

#inputs 
name = input('what is your name: ')
age = input('How old are you: ')
print(name)
print(age)