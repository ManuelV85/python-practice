 ### Loops ###
#es un mecanismo que nos sirve para iterar (pasar por el mism codigo varias veces)

# While

my_condition = 0

while  my_condition <=10:
    print(my_condition)
    my_condition +=1 #si yo no cambio la condicion el while imprimirá 0 infinitamente 
else: #es opcional
    print("mi condicion es mayor a 10")


while my_condition < 20:
    print(my_condition)
    my_condition +=2
    if my_condition ==15:
        print("mi condicion es 15 y se detiene la ejecución")
        break #rompe el ciclo cuando se cumple la condición

    print(my_condition)


#FOR
#un loop FOR nos sirve para iterar un listado de elementos.

my_list =[34, 25, 45, 87, 25, 25, 20]

for element in my_list:
    print(element)
#el ciclo FOR se repetira tantas veces como elementos existan en una posible iteración.

my_dict = {"Nombre": "Manuel", "Apellido": "Villate", "edad":37, 1:"python"}

for element in my_dict:
    print(element)
    if element == "edad":
        break
    print("se ejecuta")
else: #cuando rompemos el ciclo con el BREAK no toma la parte de ELSE
    print("el bucle for para el diccionario ha finalizado")

#el break hace que se salga del ciclo por completo

for element in my_dict:
    print(element)
    if element == "edad":
        continue #el continue es una especie de break que no rompe el bucle en total,  
                 # si no que lo rompe en esa linea y regrea a hacer el bucle. No es muy aconcejado en usar
    print("se ejecuta")
else: 
    print("el bucle for para el diccionario ha finalizado")