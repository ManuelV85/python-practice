### Regular Expresion ###

"""
Las expresiones regulares no son algo propio de python, se puede usar estos metodos
de busqueda en cualquier lenguaje. (revisar documentación de expresiones regulares)
"""

import re

my_string = "Revisar videos de Hector de Leon para expresiones regulares. videos de todo"
my_other_string = "Esta es la lección 7 expresiones regulares."

match = re.match("Revisar videos de Hector de Leon", my_string, re.I)
print(match)
print(match.span()) #span me genera una tupla con un inicio y un fin indicando la cantidad de caracteres que hay en la palabra que se busca.
#por lo tanto, puedo generar 2 variables 
start, end = match.span()
print (my_string[start: end])

print(re.match("Revisar videos de Hector", my_string, re.I)) #se va a revisar que my_string contenga el parametro pasado a match
print(re.match("Revisar videos de Hector", my_other_string)) #en consola arroja NONE, por que no encuentra lo solicitado en la cadena
print(re.match("Esta es la lección", my_string)) 


match = print(re.match("Esta es la lección", my_other_string, re.I))
#if not(match == None): #otra forma de comprobar el None
# if match != None: #otra forma de comprobar el None  

if match is not None:
    print(match)
    start, end = match.span()
    print(my_other_string[start:end])

print(re.match("Expresiones Regulares", my_other_string, re.I))


#search

search = re.search(" videos ", my_string, re.I)
print(search)
start, end = search.span()
print(my_string[start: end])

#findall 

findall = re.findall("video", my_string, re.I)
print(findall)

#split
#el split busca un patron y divide a partir de ese punto
print(re.split("video", my_string))

# sub
#el sub es para sustituir
print(re.sub("Revisar", "revisar", my_string))
print(re.sub("Revisar video", "revideo", my_string)) #puede sustituir una cadena de texto

# Patterns

#para escribir un patron de una expresion regular
pattern = r'[r|R]evisar'
print(re.findall(pattern, my_string))

pattern = r'[r|R]evisar|videos'
print(re.findall(pattern, my_string))

pattern = r'[a-z]'
print(re.findall(pattern, my_string))

"""
pattern = r'[0-9]'
print(re.findall(pattern, my_string))
busca un numero en el texto en el rango indicado, si no lo encuentra regresa un array vacio
con search se puede localizar el numero pero indicando la ubicación en la cadena de texto
"""

email = "manu3585@gmail.com"
pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
print(re.match(pattern, email))
print(re.search(pattern, email))
print(re.findall(pattern, email))

email = "manu3585@gmail"
print(re.findall(pattern, email))




