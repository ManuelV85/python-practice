### Lists ###
#Una lista se usa para agrupar valores separados por coma (item) entre corchetes
#[item 1, item 1, .... item n] y puede contener item de difentes tipos.

my_list = list()
my_other_list = []

print(len(my_list))

my_list = [37, 24, 62, 52, 30, 30, 26]
print(len(my_list)) # me indica la longitud de la lista 
print(my_list)

my_other_list = [37, 1.79, "Manuel", "Villate"]
print(type(my_other_list))

for i in my_other_list: #para recorrer la lista e imprimir el tipo de dato de cada item 
    print(type(i))

print(my_other_list[2]) # para acceder a alguna posición de la lista
print(my_other_list[0])
print(my_other_list[1])
print(my_other_list[-1])
print(my_other_list[-3])
print(my_other_list.count("Manuel")) #count retorna el numero de ocurrencia de un valor 
print(my_list.count(30))

age, height, address, surname = my_other_list
print(age)

print(my_list + my_other_list) #es una forma de conquecatenar listas

#my_list = "hola python"
#print(my_list)

#las listas son mutables

my_other_list.append("ManuDev") #el append se agrega un elemento al final de la lista 
print(my_other_list)

my_other_list.insert(1,"amarillo") # insert agrega un elmento en la posición que indicamos.
print(my_other_list)

my_other_list.remove("amarillo") #remueve el item indicado
print(my_other_list)

my_list.pop() # elimina el ultimo elmento de la lista por defecto
print(my_list)

print(my_list.pop(2))
print(my_list)

my_pop_element = my_list.pop(2)
print(my_pop_element) #el pop elminia un elmeneto pero lo puedes imprimir para saber que elemento se saco
print(my_list)

del my_list[2] #del simplemenmte elminia el elemento y no se puede usar mas adelante
print(my_list)

#remove es para eliminar un elmeneot que conocemos y por lo general elimina el primero que encuentra
#en cambio DEL elimina por indice y no por el elemento conocido

print(my_other_list)
my_other_list[1] = "rojo" #modifica la posicion de la lista 
print(my_other_list) #no modifico el color, por que arriba se removio el color, por lo tanto se asigna un
#nuevo valor a la posicion indicada

my_new_list = my_list.copy() # copia la lista 
my_list.clear()
print(my_list)
print(my_new_list)

my_new_list.reverse() #imprime la lista al reves
print(my_new_list)

my_new_list.sort() #imprime la lista ordenada
print(my_new_list)
print(my_new_list[1:2]) # para imprimir sub-listas

my_new_list.reverse() 
print(my_new_list)