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