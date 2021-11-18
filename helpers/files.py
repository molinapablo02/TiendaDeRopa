#1-Escribir en un archivo y si el archivo existe entonces borrar todo y que se crea de la nada
#2-Anadir algo al final del archivo
#3-Leer algo
#4-Escribir en un archivo y si no existe crearlo

#1- w
#2- a
#3- r
#4- w+

def read_file(filename):
    my_file = open(filename, 'r')
    print(my_file.read())
    my_file.close()


#Crear y escribir
my_file = open('data.txt', 'w+')
my_file.write('Pablo\nAna\nJorge\nNatalia')
my_file.close()


read_file('data.txt')

#crear otros datos
my_file = open('data.txt','w')
my_file.write('Pepe\nJorge\nNorma')
my_file.close()

read_file('data.txt')

#anadir al final

my_file = open('data.txt', 'a')
my_file.write('\nAldo\nRomina\nRicardo')
my_file.close()

#read_file('data.txt')
my_file = open('data.txt', 'r')
nombres = my_file.readlines()

for nombre in nombres:
    print(nombre)

#print(my_file.readlines(2))
my_file.close()


