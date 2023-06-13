"""
Realizar un programa en el cual se declaren dos valores enteros por teclado utilizando el método __init__. 
Calcular después la suma, resta, multiplicación y división. Utilizar un método para cada una e imprimir los resultados obtenidos. 
Llamar a la clase Calculadora.
"""

class calculadora:
    def __init__ (self):
        self.num1=int(input("Dame el primer número "))
        self.num2=int(input("Dame el segundo número "))
    
    def suma (self):
        print("La suma de los dos números proporcionados es", str(self.num1+self.num2))

    def resta (self):
        print("La resta de los dos números proporcionados es",str(self.num1-self.num2))

    def multi (self):
        print("La multiplicación de los dos números proporcionados es", str(self.num1*self.num2))

    def divi (self):
        print("La división de los dos números proporcionados es", str(self.num1/self.num2))

micalculadora = calculadora()
micalculadora.suma()
micalculadora.resta()
micalculadora.multi()
micalculadora.divi()