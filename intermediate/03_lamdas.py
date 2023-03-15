### Lamdas ###
"""
Son como funciones, pero son funciones anonimas ya que no
tienen nombre. Como es una función puede tener parametros de entrada.
Una función Lambda se puede almacenar en una variable.
 
"""
sum_two_values = lambda first_value, second_value: first_value + second_value

#sum_two_values() se observa que la variable se comporta como una función.
print(sum_two_values(2, 4))

multiply_values = lambda first_value, second_value: first_value * second_value -3
print(multiply_values(2, 8))


def sum_three_values(value):

    return lambda first_value, second_value: first_value + second_value + value

print(sum_three_values(5)(2,4))

