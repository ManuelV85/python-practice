### sets ###

#Los sets son una estructura de datos uasda para almacenar elementos de una manera muy similar a las listas
#pero con algunas diferencias. Los sets permiten almacenar varios elementos y acceder a ellos de una forma muy similar a las listas.
#La diferencia es que:
# los elementos de un set son únicos, lo que significa que no deben haber elementos duplicados.
#son desordenados, lo que significa que no mantienen un orden cuando son declarados
#deben ser inmutables.

my_set = set() #forma de crear un set con la palabra receberpada
my_other_set = {} #inicialmente si se aplica type, indica que es un diccionario
print(type(my_set))
print(type(my_other_set))

my_other_set = {"Manuel", "Villate", 37}
print(type(my_other_set)) #despues de introducir item, se convierte en set

len(my_other_set)
print(len(my_other_set)) #indica cantidad de elementos dentro del set

my_other_set.add("manu_dev") #agrega un elemento al set de forma desordenada, por lo tanto es una diferencia de la lista
print(my_other_set)          #ya que su estructura no es ordenada.

#cuando se intenta incluir otro elemento no lo toma ya que el set no acepta elementos repetidos

print("Manuel" in my_other_set) #sintaxis para compronar que el elemento existe en el set
print("Manue" in my_other_set)

my_other_set.remove("Villate")
print(my_other_set)

my_other_set.clear()
print(my_other_set)
print(len(my_other_set))

del my_other_set    #la diferencia entre del y clear, es que del elimina por completo el (set, tupla o lista) creado
#print(my_other_set) error  #clear solo limpia el contenido perdo deja el set creado
                     #del len type... son operaciones propias del sistema y por eso van antes de la palabra


my_set = {"manuel", "villate", 37}
my_list = list(my_set)
print(type(my_set))

my_other_set = {"python", "js", "flask", }
my_new_set = my_set.union(my_other_set)

print(my_new_set)

print(my_new_set.union(my_new_set).union({"angelo","solangel"})) #no se agregarn elementos repetidos, pero se puede agregar
                                                                 # un nuevo set sin declarar una variable, de forma directa.

print(my_new_set.difference(my_set))
print(my_new_set)