archivo = open('prueba.txt' , 'r' , encoding='utf8')
#otra forma de buscar la ruta
#archivo = open('c:\\Users\\Admin\\Desktop\\django\\aa\\PYTHON\\manejo de archivos\\prueba.txt','r', encoding='utf8')

#print(archivo.read())

#leer algunos caracteres
#print( archivo.read(15)) #el numero 15 son la cantidad de caracteres que vamos a leer del archivo prueba.txt que llamamos por el metodo
#print(archivo.read(6))# continua donde queda la anterior
#print(archivo.read())#con esto podemos leer la linea completa


#CONTINUACION OTRO VIDEO

# leer lineas completas
# print(archivo.readline())
# print(archivo.readline())

# iterar el archivo
# for linea in archivo:
#     print(linea)

# leer lineas
# print(archivo.readlines())

# acceder a una linea de la lista
# print(archivo.readlines()[2])

# abrimos un nuevo archivo
# a - anexar informacion
archivo2 = open('copia.txt', 'a', encoding='utf8')
archivo2.write(archivo.read())

archivo.close()
archivo2.close()
print('se ha terminado el proceso de leer y copiar archivos')

#ESTO SOBRE ESCRIBE Y CREA UNA COPIA DE PRUEBA


