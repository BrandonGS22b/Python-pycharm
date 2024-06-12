class Entero:
    def __init__(self):
        self.numeros = []

    def leer_numero(self):
        while True:
            num = int(input("Ingrese un número entero y positivo (0 para terminar): "))
            if num == 0:
                break
            self.numeros.append(num)

    def imprimir_impares(self):
        impares = []
        for num in self.numeros:
            suma_digitos = 0
            temp_num = num  # Variable temporal para preservar el número original
            while temp_num > 0:
                suma_digitos += temp_num % 10
                temp_num //= 10
            if suma_digitos % 2 != 0:
                impares.append(num)
        print("Los números cuya suma de dígitos es impar son:")
        for num in impares:
            print(num)
        print("La cantidad de números cuya suma de dígitos es impar es:", len(impares))

    def imprimir_terminados_en_7(self):
        terminados_en_7 = []
        for num in self.numeros:
            if num % 10 == 7:
                terminados_en_7.append(num)
        print("Los números terminados en 7 son:")
        for num in terminados_en_7:
            print(num)
        print("La cantidad de números terminados en 7 es:", len(terminados_en_7))

    def imprimir_mas_de_4_digitos(self):
        mas_de_4_digitos = []
        for num in self.numeros:
            if num > 9999:
                mas_de_4_digitos.append(num)
        print("Los números con más de cuatro dígitos son:")
        for num in mas_de_4_digitos:
            print(num)

resultado = Entero()
resultado.leer_numero()
resultado.imprimir_impares()
resultado.imprimir_terminados_en_7()
resultado.imprimir_mas_de_4_digitos()