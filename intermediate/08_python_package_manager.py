### Python Package Manager ###

"""
Si vamos a usar cualquier modulo que no tenemos dentro de python debemos usar el package manager
"pip"  package installer de python    pagina para revisar pypi.org

para revisar la version pip --version
si no se tiene, se puede instal haciendo pip install pip
"""

"""
que se instalo durante la practica:
- numpy
"""

import numpy

numpy_array = numpy.array([35, 24, 52, 30, 17])
print(type(numpy_array))

print(numpy_array * 2)

#import pandas #pip install pandas

#pip list podemos ver las librerias por defecto de python mas las que se han instalado
#pip uninstall para desinstalar librerias
#pip show 
#pip install requests


import requests

response = requests.get("https://pokeapi.co/api/v2/pokemon?limit=151")
print(response)
print(response.status_code)
print(response.json())


from mypackage import arithmetics

print(arithmetics.sum_two_values(1, 4))