#SET
planetas ={'Marte','jupiter','venus'}
print(planetas) #aqui no va imprimir en el oren que los ingresamos va a ser en desorden

#largo de los elementos
print(len(planetas))

#revisar si un elemento esta presente
print('Marte' in planetas)
# agregar un nuevo elemento
planetas.add ('tierra')
print(planetas)  
# no se pueden duplicar elementos
planetas.add ('tierra')
print(planetas)  

#eliminar elemento
planetas.remove ('tierra')
print(planetas)

#tambien tenemos la funcion de discard que nos ayuda a eliminar elementos
planetas.discard('jupiter')
print('aplicamos la funcion de discard',planetas)


#tambien tenemos la funcion clear
planetas.clear()
print('elimina todos los planetas' , planetas)

#podemos eliminar el set por completo con el del

del planetas 
print('eliminados el set ', planetas)