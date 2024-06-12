# una tupla guarda los valores a medida que los vayamos agregando ni tampoco eliminarlos en cambio en la lista los podemos modificar

#definir una tupla....vamos a trabajar con frutas

frutas=('Naranja ','platano','guayaba',) #debemos poner la coma al final osino no seria tupla y no se imprime guayaba
print(frutas)
#saber el largo de una tupla

print(len(frutas))

#acceder a un elemento
print(frutas[0])

#navegacion inversa
print(frutas[-1])

#acceder a un rango de valores
print(frutas[0:1]) #sin incluir el ultimos indice

#recorrer elementos
for  fruta in frutas:
    print (fruta, end =' ')# ponemos un espacion en blanco en vez de poner /n con ese espacion no saldra reglon por reglon

    #cambiar valor tupla
    #frutas[0]= 'pera'
    

    #para poder modificar los elementos de una tupla debemos o podemos modificar la tupla hacia una lista en la lista podemos modificarla y la volvemos a convertir otravez en tupla

    frutaLista =list(frutas)
    frutaLista[0]='pera'
    frutas=tuple(frutaLista)
    print('\´n',frutas)

    #podenis eliminar la tupla completamente la tupla con 
    #del frutas
    #print(frutas)