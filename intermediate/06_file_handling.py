### File Handling ###

# .txt file

import os

my_file = "./my_file.txt"
txt_file = open(my_file, "r+")
print(txt_file.read())
#print(txt_file.read(10)) #solo lee los 10 espacios de la primera linea
print(txt_file.readline) #lectura linea a linea del fichero
for line in txt_file.readlines():
    print(line)


txt_file.write("\n Aunque tambien JS")
print(txt_file.readline())


