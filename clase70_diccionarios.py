# dict (key, value)
diccionario = {
'IDE':'Integrated Development Environment',
'00P':'0bject Oriented Programming',
'DBMS':' Database Management System',
}
print(diccionario)
#largo
print (len (diccionario))
# acceder a un elemento (key)
print( diccionario['IDE'])
# otra forma de recUperar un elemento
print(diccionario.get ('00P'))
# modificando elementos
diccionario ['IDE'] = 'integrated development environment '

print ('para modificar elementos del diccionario',diccionario)