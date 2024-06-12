#la ventaja de esta sintaxis es que abre el archivo y cierra el archivo 
#sin necesidad de usar el close() como lo vimos anteriormente
#y no vamos agrea el try ni el finally donde le agragamos el cotenido al archivo
with open ('prueba.txt', 'r' , encoding='utf8' ) as archivo:
    print(archivo.read())