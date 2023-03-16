### File Handling ###

# .txt file

import os

txt_file = open("intermediate/my_file.txt", "r+")
print(txt_file.read())
#print(txt_file.read(10)) #solo lee los 10 espacios de la primera linea
print(txt_file.readline) #lectura linea a linea del fichero