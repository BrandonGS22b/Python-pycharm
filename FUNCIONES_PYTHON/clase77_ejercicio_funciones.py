#crear una funciobn para sumar los valorers recibidos de tipo numerico
#utilizando argumentos variables *args como parametro de la funcion
#y regresar como resultado la suma de todos los valores pasados como argumeros

def sumar_valores(*args):

    resultado = 0
    #Iteramos cada elemento
    for valor in args:
        #resultado=resultado + valor
          resultado += valor
    return resultado
       

#llamamos la funcion
print(sumar_valores(3,5,9))


 



