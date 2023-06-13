"""
Realizar un programa que tenga una clase Persona con las siguientes características. La clase tendrá como atributos el nombre y la edad de una persona. 
Implementar los métodos necesarios para inicializar los atributos, mostrar los datos e indicar si la persona es mayor de edad o no.
"""

class persona:
    def __init__ (self, nom, edad):
        self.nombre=nom
        self.edad=edad
        print("Se ha registrado la persona correctamente")
    
    def imprimir (self):
        print("Nombre:",self.nombre)
        print("Edad:",self.edad)

    def mayorDeEdad (self):
        if self.edad >= 18:
            print(self.nombre,"es mayor de edad")
        else:
            print(self.nombre,"no es mayor de edad")

persona1 = persona("Ainhoa", 18)
persona1.imprimir()
persona1.mayorDeEdad()
persona2 = persona("Fran",17)
persona2.imprimir()
persona2.mayorDeEdad()