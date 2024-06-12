class Persona:
    def __init__(self, nombre='Juan', apellido='Perez', edad=28):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

persona1 = Persona()
print(persona1.nombre)
print(persona1.apellido)
print(persona1.edad)