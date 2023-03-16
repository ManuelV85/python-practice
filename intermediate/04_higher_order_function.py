### funciones de orden superior >(higher order function ###
"""
Funciones que entran en funciones.
"""


def sume_one(value):
    return value + 1

def sume_five(value):
    return value + 5

def sum_two_values_and_add_one(first_value, second_value, f_sum): #f_sum es una función

    return f_sum(first_value + second_value)

print(sum_two_values_and_add_one (5, 2, sume_one)) #función que llama a una función.
print(sum_two_values_and_add_one (5, 2, sume_five)) #función que llama a una función.

### CLosures ###

"""
Se define una función dentro de otra función.
retorno una función
Nos puede servir para montar paradicmas que son asincronos.
"""

def sum_ten():
    def add(value):
        return value + 10
    
    return add

add_clouser = sum_ten() #función que retorna una función.
print(add_clouser(5))

#función que define una función y retorna una función.

def sum_ten(original_value):
    def add(value):
        return value + 10 + original_value
    
    return add

add_clouser = sum_ten(1) 
print(add_clouser(5))

sum_ten(5)(1) #otra forma de llamar a esta función, se llama como si fuera una LAMBDA
              #el resultado de una operación le estamos pasando el siguiente valor
print(sum_ten(5)(1))

### Built-in Higher Order Function ###

numbers = [2, 5, 10, 21, 3, 30]

#map
#la función map siempre va a necesitar un iterable (una lista)

def multiply_two(number):
    return number * 2

print(list(map(multiply_two, numbers)))
print(list(map(lambda number: number * 2, numbers)))


#map... con un listado iterable genera otro listado iterable segun la función que le pasemos 
#map recorre todos los valores y ejecuta una función sobre ellos para modificar su valor
#filter

def filter_greater_that_ten(number):
    if number > 10:
        return True
    else:
        return False

print(list(filter(filter_greater_that_ten, numbers)))
print(list(filter(lambda number: number >10, numbers))) #otra forma de hacer con LAMBDA y da exactamente el mismo resultado

#filter recorre todos los valores y ejecuta una función que retorna True o False para saber como filtrar
#los valores del iterable.

#Reduce
#reduce opera con los valores que va recorriendo 
#reduce opera con un valor más el acumulado.

from functools import reduce  #se debe importar por ser un modulo(función) independiente

def sum_two_values(first_value, second_value):
    return first_value + second_value

print(reduce(sum_two_values, numbers))

#para observar como funciona, se imprime los valores first_value y second_value
#numbers = [2, 5, 10, 21, 3, 30] para observar como se va asignando y sumando los valores
def sum_two_values(first_value, second_value):
    print(first_value)
    print(second_value)
    return first_value + second_value

print(reduce(sum_two_values, numbers))
#se obtiene un unico valor del iterable