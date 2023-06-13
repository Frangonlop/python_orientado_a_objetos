"""
Desarrollar un programa que conste de una clase padre Cuenta y dos subclases PlazoFijo y CajaAhorro. 
Definir los atributos titular y cantidad y un método para imprimir los datos en la clase Cuenta. 
La clase CajaAhorro tendrá un método para heredar los datos y uno para mostrar la información.
La clase PlazoFijo tendrá dos atributos propios, plazo e interés. 
Tendrá un método para obtener el importe del interés (cantidad*interés/100) y otro método para mostrar la información, datos del titular plazo, interés y total de interés.
Crear al menos un objeto de cada subclase.
"""
class Cuenta:
    def __init__(self, titular, cantidad):
        self.titular = titular
        self.cantidad = cantidad
    
    def mostrar(self):
        print("El titular de la cuenta es",self.titular,"y tiene una cantidad de",self.cantidad)

class CajaAhorro(Cuenta):
    def __init__ (self, titular, cantidad):
        super().__init__(titular, cantidad)
    
    def imprimir(self):
        print("Cuenta Caja Ahorro")
        super().mostrar()

class PlazoFijo(Cuenta):
    def __init__ (self, titular, cantidad, plazo, interes):
        super().__init__(titular, cantidad)
        self.plazo = plazo
        self.interes = interes

    def importe(self):
        ganancia = self.cantidad*self.interes/100
        print("El importe de interes es:", ganancia)
    
    def imprimir(self):
        print("Cuenta Plazo Fijo")
        super().mostrar()
        print("El plazo en dias es:",self.plazo)
        print("El interés es:", self.interes)

caja1 = CajaAhorro("Ainhoa", 1000)
caja1.imprimir()
caja2 = PlazoFijo("Fran", 1000, 10, 2)
caja2.imprimir()
caja2.importe()