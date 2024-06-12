#sintaxis de range (inicia<opcionl>, fin < requerido >, incrementa< opcional)

#Ejercicio1 . Iterar un rango de 0 a 10 e imprimir numeros divisibles entre 3
print ('Rango de 0 a 10 con numeros divisibles entre 3')
for i in range(11):
    if i % 3 == 0:
        print (i)

#Ejercicio 2 : crear un rango de numeros de 2 a 6, e imprimirlos
print('Rango de 0 a 10 con numeros divisibles entre 3')
rango =(2,7)  
for i in rango:
    print(i)          

#Ejercicio3. crear un rango de 3 a 10, pero con incremento de 2 en 2 , en la

print('Rango con valores de inicio = 3 , fin = 10, incremento = 2')
rango= range(3,11,2)
for i in rango:
    print(i)