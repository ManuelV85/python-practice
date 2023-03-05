#strings#
#para definir la variable str
my_string = "hola"
my_other_str = 'hola de nuevo'
#las variables se pueden declarar con "" o ' ' 

print(len(my_string), "y la otra str", len(my_other_str))

#con \n podemos hacer un salto de linea en la terminal
my_str_line = "este str tiene\nsalto de linea"
print(my_str_line)
#cpn \t podemos dar tabulación en la terminal
my_str_line2 = "\teste str con tabulación"
print(my_str_line2)

#formateo

name, surname, age = "manuel", "villate", 37
print("mi nombre es {} {} y mi edad es {}".format(name, surname, age)) #
print("mi nombre es %s %s y mi edad es %d" %(name, surname, age)) #es la mejor forma para imprimir 
# %s marcador de posicion para valores de cadena  %d marcador de posición para valores entero
print("mi nombre es " + name +" " + surname +" " + "y mi edad es " + str(age))
print(f"mi nombre es {name} {surname} y mi edad es {age} ") #inferencia de datos

#desempaquetado de caracteres
language = "python"
a, b, c, d, e, f = language
print(a)
print(b)

#division
lenguage_slice = language[1:4]
print(lenguage_slice)
lenguage_slice = language[1:]
print(lenguage_slice)
lenguage_slice = language[-2]
print(lenguage_slice)
lenguage_slice = language[0:6:4]
print(lenguage_slice)

#reversa
reversed_language = language[::-1]
print(reversed_language)

#funciones

print(language.capitalize()) #pone la primera letra en mayuscula
print(language.upper()) #pone todo en mayuscula
print(language.count("t")) #cuantas letras iguales hay en 1 palabra
print(language.isnumeric())# pregunta que si la variable "lenguage" es un numero
print("1".isnumeric())
print(language.lower())
print(language.lower().isupper)
print(language.startswith("py"))


