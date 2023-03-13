### Diccionarios ###
my_dict = dict()
my_other_dict = {}

print(type(my_dict))
print(type(my_other_dict))

#relación clave valor, es lo que diferencia al diccionario del set. Es una estructura
#que nos sirve para relacionar datos.
my_other_dict = {
    "Nombre": "Manuel", 
    "Apellido": "Villate",
    "Edad":37,
    1:"Python"

}
print(my_other_dict)

my_dict = {
    "Nombre": "Manuel", 
    "Apellido": "Villate",
    "Edad":37,
    "Lenguajes":{"Python, Js"},
    1:"0000001",
    2:1.79

}
print(my_dict)
print(len(my_dict))
print(len(my_other_dict)) 

#para buscar dentro del diccionario
print(my_dict["Nombre"]) #solo imprime el valor. y no la clave my_dict = {clave1:valor1, clave2:valoe2}

#si quiero cambiar el valor puedo hacer:
my_dict["Nombre"]= "Angelo"
print(my_dict["Nombre"])

#para agregar un nuevo campo al diccionario
my_dict["princesa"]= "Solangel"
print(my_dict) #como es ordenado, se agrega al final.
print(my_dict["princesa"])

del my_dict["Edad"] #elimina el campo completo de edad y lo saca del diccionario. Si se desea agregar de nuevo
print(my_dict)      #es necesario volver a crear el campo.

#para comprobar si algo esta dentro de un diccionario.
print("Angelo" in my_dict)  #de esta forma se busca por calve y no por valor
print("princesa" in my_dict)#en este caso como busca por clave arroja el varlor de true

print(my_dict.items())
print(my_dict.keys())
print(my_dict.values())
print(my_dict.fromkeys(("Nombre", 1, 2))) #cuando se imprime los keys 1 y 2 arrojan NONE

#para crer un diccionario nuevo sin valores se puede hacer
my_new_dict = my_other_dict.fromkeys(("Nombre", 1)) #revisar esta misma operacion pero con ("Nombre", 1)--> con 1 solo par de ()
print(my_new_dict)

my_list = ["nombre", 1 , "casa"]
my_new_dict = my_other_dict.fromkeys((my_list)) #deja todas las keys vacias 
print(my_new_dict)

my_new_dict = my_other_dict.fromkeys(my_list, ("Manuel", "Villate")) #a cada key de my_list se le ha pasado el valor ("Manuel", "Villate")

print(my_new_dict)

may_values = my_new_dict.values()
print(type(my_new_dict))

#pruebas ... se esta rebuscando el codigo

print(my_new_dict.values())
print(list(my_new_dict.values()))
print(tuple(my_new_dict))
print(set(my_new_dict))
print(list(dict.fromkeys(list(my_new_dict.values())).keys()))
