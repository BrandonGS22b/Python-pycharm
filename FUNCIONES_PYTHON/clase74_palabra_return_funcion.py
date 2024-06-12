def sumar (a, b):
    return a+b

resultado= sumar(5,3)
print(f'resultado de la suma: {resultado}')

#otra forma de hacerlo

def sumar (a=0, b=0) -> int:
    return a+b

resultado= sumar()
print(f'resultado de la suma: {resultado}')
print(f'Resultado sumar: { sumar(8,2)}')
