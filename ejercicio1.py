"""
Realizar un programa que conste de una clase llamada Alumno que tenga como atributos el nombre y la nota del alumno. 
Definir los métodos para inicializar sus atributos, imprimirlos y mostrar un mensaje con el resultado de la nota y si ha aprobado o no.
"""

class alumno:
    def __init__ (self, nom, nota):
        self.nombre=nom
        self.nota=nota
        print("Se ha registrado el alumno correctamente")

    def imprimir (self):
        print("Nombre:",self.nombre)
        print("Nota:",self.nota)

    def aprobado (self):
        if self.nota >= 5:
            print(self.nombre+" ha aprobado")
        else:
            print(self.nombre+" no ha aprobado")

alumno1 = alumno ("Ainhoa", 8)
alumno2 = alumno ("Fran", 4)
alumno1.imprimir()
alumno1.aprobado()
alumno2.imprimir()
alumno2.aprobado()