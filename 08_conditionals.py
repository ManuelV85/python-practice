### COnditionals###


my_condition = False

if my_condition: #Es lo mismo que if my_condition == TRUE
    print("Se ejecuta la condición del IF")

print("La ejecución continua")

#como la condicion es FALSE no se imprime el print dentro del condicional
#por eso en la terminal solo indica el print fuera de la condicion.

my_condition = 5 * 2

if my_condition == 10: 
    print("Se ejecuta la condicion del segundo if ")

print("La ejecución continúa")

#cuando se desee hacer algo cuando la condicion no se cumpla

if my_condition > 10: 
    print("Es mayot que 10 ")
else:
    print("Es menor o igual que 10")

print("La ejecución continúa")

# if --> condicional
# elif --> condicional, por lo tanto necesita una condicion
#else --> no necesita condición, se ejecuta por defecto.

my_string = "" #cuando se tiene un str vacia arroja un valor como FALSE
                #si pongo las " "(con un espacio), me interpreta que no es vacia.

if my_string:
    print("mi cadena de texto no es vacia") #por lo tanto no imprimira nada 

     
if not my_string:
    print("mi cadena de texto es vacia")