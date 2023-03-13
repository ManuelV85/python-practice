### challenges ###
#reto 1 FIZZ BUZZ FIZZBUZZ
"""
Escribe un programa que muestre por consola (con print) los numeros
de 1 a 100 (ambos incluidos y con salto de linea entre cada impresion
), sustituyendo lo siguiente:
 - multiplos de 3 por la pañabra "fizz"
 - multiplos de 5 por la palabra "buzz"
 - multiplos de 4 y 5 por la palabra fizzbuzz
 """

def fizzbuzz():
    for index in range(1, 101):
        if index % 3 == 0 and index % 5 == 0: #se comprueba el caso mas restrictivo primero
            print("fizzbuzz")
        elif index % 3 == 0:
            print("fizz")
        elif index % 5 == 0:
            print("buzz")
        else:
            print(index)
    

fizzbuzz()
