### Exception Handling ###

#manejo de errores. 

"""
try:
    { Run this code}
except:
    { Execute this code when there is an exception}
else:
    {no exceptions? run this code}
finally:
    {always run this code}
"""

number_one =5
number_two =1
number_two ="1"

#print(number_one + number_two) #se genera un error por que no se puede usar un int con str
"""
if number_one > 3:
    print(number_one + number_two)
else:
    print("no se compilo")
"""
#como se observa cuando se compila, estp sogue generando un error por lo tanto, el IF and ELSE no sutituyen el TRY and EXCEPTION

try:
    print(number_one + number_two)
    print("No se ha producido un error") #si en la linea 30 se genera un error, la linea 31 no se lee y pasa al siguiente bloque (EXCEPT)
except:
    #se ejecutasi se produce una excepción
    print("se ha producido un error") 

#try except else

try:
    print(number_one + number_two)
    print("No se ha producido un error") #si en la linea 30 se genera un error, la linea 31 no se lee y pasa al siguiente bloque (EXCEPT)
except:
    print("se ha producido un error") 
else:
    #se ejecuta si no se produce una excepción
    print("la ejecucion continua correctamente")


#try except else finally

try:
    print(number_one + number_two)
    print("No se ha producido un error") #si en la linea 30 se genera un error, la linea 31 no se lee y pasa al siguiente bloque (EXCEPT)
except:
    print("se ha producido un error") 
else:
    #se ejecuta si no se produce una excepción
    print("la ejecucion continua correctamente")
finally:
    #se ejecuta siempre, haya error o no
    print("la ejecución continua")

#si hay un TRY debe existir un EXCEPT, la parte de ELSE y FINALLY son opcionales

#excepciones por tipo
try:
    print(number_one + number_two)
    print("No se ha producido un error") #si en la linea 30 se genera un error, la linea 31 no se lee y pasa al siguiente bloque (EXCEPT)
except TypeError:
    
    print("se ha producido un typeerror") 
except ValueError:
    
    print("se ha producido un valueerror") 

#como se pueden producir errores de diferentes tipos se pueden poner excepciones para capturar estos errores.

# Captura de la información de la excepción

try:
    print(number_one + number_two)
    print("No se ha producido un error") 
except ValueError as error:
    print(error) 