"""
Desarrollar un programa que cargue los datos de un triángulo. 
Implementar una clase con los métodos para inicializar los atributos, imprimir el valor del lado con un tamaño mayor y  el tipo de triángulo que es (equilátero, isósceles o escaleno).
"""

class triangulo:
    def __init__ (self):
        self.lado1 = int(input("Dame el tamaño del primer lado: "))
        self.lado2 = int(input("Dame el tamaño del segundo lado: "))
        self.lado3 = int(input("Dame el tamaño del tercer lado: "))

    def ladoMayor (self):
        if self.lado1 > self.lado2 and self.lado1 > self.lado3:
                print("El lado mayor es el primero")
        elif self.lado2 > self.lado1 and self.lado2 > self.lado3:
                print("El lado mayor es el segundo")
        elif self.lado3 > self.lado1 and self.lado3 > self.lado2:
                print("El lado mayor es el tercero")
        else:
              print("Hay dos lados iguales")

    def tipoTriangulo(self):
        if self.lado1 == self.lado2 == self.lado3:
                print("El triángulo es equilátero")
        elif self.lado1 != self.lado2 != self.lado3:
              print("El triángulo es escaleno")
        else:
              print("El triángulo es isósceles")

triangulo1 = triangulo()
triangulo1.ladoMayor()
triangulo1.tipoTriangulo()