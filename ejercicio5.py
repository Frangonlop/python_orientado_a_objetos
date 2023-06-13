"""
Realizar una clase que administre una agenda. Se debe almacenar para cada contacto el nombre, el teléfono y el email.
Además deberá mostrar un menú con las siguientes opciones
 -Añadir contacto
 -Lista de contactos
 -Buscar contacto
 -Editar contacto
 -Cerrar agenda

"""
class agenda:
    def __init__ (self):
        self.contactos = []
    
    def menu (self):
        print("1. Añadir contacto")
        print("2. Lista de contactos")
        print("3. Buscar contacto")
        print("4. Editar contacto")
        print("5. Cerrar agenda")
        opcion=int(input("Introduzca el número de la operación que desea realizar "))
        if opcion == 1:
            self.add()
        elif opcion == 2:
            self.lista()
        elif opcion == 3:
            self.buscar()
        elif opcion == 4:
            self.edit()
        elif opcion == 5:
            print("Cerrando agenda")
            exit()
        else:
            print("Por favor, introduzca una opción válida")
            print("---------------------------------------")
            self.menu()

    def add(self):
        print("---------------------")
        print("Añadir nuevo contacto")
        print("---------------------")
        nom = input("Introduzca el nombre: ")
        dni = input("Introduzca el dni: ")
        self.contactos.append({'nombre':nom, 'dni':dni})
        print("Contacto guardado correctamente")
        self.menu()

    def lista(self):
        print("------------------")
        print("Lista de contactos")
        print("------------------")
        if len(self.contactos) == 0:
            print("Introduzca primero algún contacto")
        else:
            for x in range(len(self.contactos)):
                print(self.contactos[x]['nombre'])
        self.menu()

    def buscar(self):
        print("---------------")
        print("Buscar contacto")
        print("---------------")
        nom = input("Introduzca el nombre del contacto ")
        for x in range(len(self.contactos)):
            if nom == self.contactos[x]['nombre']:
                print("Datos del contacto")
                print("Nombre:",self.contactos[x]['nombre'])
                print("Dni:", self.contactos[x]['dni'])
        

    def edit(self):
        print("---------------")
        print("Editar contacto")
        print("---------------")
        data = self.buscar()
        print("1. Nombre")
        print("2. Dni")
        print("3. Volver")
        option = int(input("Dime que quieres editar: "))
        if option == 1:
            nom = input("Introduzca el nuevo nombre: ")
            self.contactos[data]['nombre'] = nom
        elif option == 2:
            dni = input("Introduzca el nuevo dni: ")
            self.contactos[data]['dni'] = dni
        elif option == 3:
            print("Saliendo del modo edición")
            self.menu()
        else:
            print("Introduzca una opción válida")
            print("----------------------------")
            self.edit()
        self.menu()
newagenda = agenda()
newagenda.menu()