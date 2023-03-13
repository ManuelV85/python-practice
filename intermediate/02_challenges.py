### challenges ###
#reto 1 FIZZ BUZZ FIZZBUZZ
"""
Escribe un programa que muestre por consola (con print) los numeros
de 1 a 100 (ambos incluidos y con salto de linea entre cada impresion
), sustituyendo lo siguiente:
 - multiplos de 3 por la pañabra "fizz"
 - multiplos de 5 por la palabra "buzz"
 - multiplos de 3 y 5 por la palabra fizzbuzz
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


#reto 2 ¿Es un anagrama?
"""
Escribe una función que reciba 2 palabras "String" y retorne
verdadero o falso (bool), segun sean o no anagramas.
Un anagrama consiste en formar una palabra reodenando TODAS las letras
de otra palabra inicial.
No hace falta comprobar que ambas palabras existan.
Dos palabras exactamente iguales no son anagramas.
"""
def is_anagram(word_one, word_two):
    if word_one.lower() == word_two.lower(): #permite revisar que las palabras no sean iguales
         return False                        #es una de las condiciones.


    return sorted(word_one.lower()) == sorted(word_two.lower()) #primero se pasa toda la palabra a minuscula con lower() y
                                                                #luego se ordena con sorted para ver si son las mismas letras             
print(is_anagram("Amor", "Roma"))                               #y decir que es un anagrama.
    

#reto 3 sucesion de fibonacci
"""
Escribe un programa que imprima los 50 primeros numeros 
de la sucesión de Fibonacci empezando en 0.
La serie Fibonacci se compone por una sucesión de números
en lo que el siguiente siempre es la suma de los dos anteriores.
0, 1, 1, 2, 3, 5, 8, 13...
"""

def sum_fibonacci():
    prev = 0
    next = 1
    for index in range(0, 50):
        
        print(prev)

        fib = prev + next
        prev = next
        next = fib

    
    
sum_fibonacci()    