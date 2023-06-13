"""
En un banco tienen clientes que pueden hacer depósitos y extracciones de dinero. 
El banco requiere también al final del día calcular la cantidad de dinero que se ha depositado.
Se deberán crear dos clases, la clase cliente y la clase banco. 
La clase cliente tendrá los atributos nombre y cantidad y los métodos __init__, depositar, extraer, mostrar_total.
La clase banco tendrá como atributos 3 objetos de la clase cliente y los métodos __init__, operar y deposito_total.

"""
class cliente :
    def __init__ (self, nom):
        self.nombre = nom
        self.cantidad = 0

    def depositar(self, cant):
        self.cantidad = self.cantidad + cant
    
    def extraer(self, cant):
        self.cantidad = self.cantidad - cant
    
    def cantidad(self):
        return self.cantidad

    def mostrar(self):
        print("El cliente ",self.nombre," tiene una cantidad total de ", self.cantidad)

class banco :
    def __init__ (self):
        self.cliente1 = cliente("Ainhoa")
        self.cliente2 = cliente("Fran")
        self.cliente3 = cliente("Maria")
    
    def operar (self):
        self.cliente1.depositar(1000)
        self.cliente2.depositar(500)
        self.cliente3.depositar(300)
        self.cliente3.extraer(200)
    
    def deposito_total(self):
        self.cliente1.mostrar
        self.cliente2.mostrar
        self.cliente3.mostrar
        print("La cantidad total que hay en el banco es ",self.cliente1.cantidad+self.cliente2.cantidad+self.cliente3.cantidad)

banco1 = banco()
banco1.operar
banco1.deposito_total