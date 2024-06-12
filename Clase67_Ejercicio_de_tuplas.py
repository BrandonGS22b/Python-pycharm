#dada la siguiente tupla,
#crea una lista que solo incluya los numeros menores a 5
tupla = (13, 1, 8, 3, 2, 5, 8)
A=5
for i in tupla:
    if i < A:
        print(i)

 # como lo hize anteriormente esta mal porque tocaba usar listas
 #ASI SE HACIA 
 # Definir Listas
lista=[]
#filtamos los lementos menores a 5 de la tupla
for elemento in tupla:
    if elemento<5:
        lista.append(elemento)
        #imprimimos la lista
        print('imprimimos ',lista) 
       