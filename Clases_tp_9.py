class MyPerson:
    #Inicializamos los atributos de la Persona
    def __init__(self,name="",age=0,dni=""):
        self._name = name
        self._age=age
        self._dni=dni
    
    #Ingresamos un nombre 
    def set_name(self,new_name):
        self._name= new_name
        
    #Ingresamos la edad
    def set_age(self,new_age):
        self._age= new_age
    
    #Ingresamos el dni
    def set_dni(self,new_dni):
        self._dni=new_dni

    #Obtenemos el nombre de la Persona
    def get_name(self):
        return self._name
    
    #Obtenemos la edad de la persona
    def get_age(self):
        return self._age
    
    #Obtenemos el dni de la persona
    def get_dni(self):
        return self._dni
    
    #Verificamos si la persona es Mayor de edad
    def is_older(self):
        if self._age >=18:
            return True
        else:
            return False

class Account:
    
    def __init__(self, holder="",amount=0):
        self._holder = holder
        self._amount = amount
    
    def set_holder(self,new_holder):
        self._holder= new_holder

    def set_amount(self,new_amount):
        if new_amount>=0:
            self.amount= new_amount
    
    def get_holder(self):
        return self._holder
    
    def get_amount(self):
        return self._amount
    
    def display(self):
        print(f"Titular: {self._holder}")
        print(f"Cantidad Disponible: {self._amount}")
    
    def deposit(self,amount):
        if amount > 0:
            self._amount +=amount
        
    def extraction(self,amount):
        if amount > 0:
            self._amount -= amount

class Triangle:

    #Inicializamos la clase, dandole el valor a sus cada lado del triángulo
    def __init__(self,side_1=5,side_2=3,side_3=2):
        self.side_1=side_1
        self.side_2=side_2
        self.side_3=side_3
    
    #Este método verifica que tipo de triángulo es
    def type_triangle(self):
        #Si tiene sus tres lados iguales es equilatero
        if(self.side_1==self.side_2 and self.side_1==self.side_3 and self.side_2==self.side_3):
            print("Triángulo Equilatero")
        
        #Si dos de sus lados son iguales y uno es diferente, es Isósceles    
        elif((self.side_1==self.side_2 and self.side_1 != self.side_3) or (self.side_1==self.side_3 and self.side_1 != self.side_2) or (self.side_2==self.side_3 and self.side_1 != self.side_2)):
            print("Triángulo Isósceles")
        #Y si ninguno de los lados del triángulo es igual es Escaleno    
        else:
            print("Triángulo Escaleno ")

    #Este método nos devuelve el lado mayor del triángulo
    def long_side(self):
        if self.side_1>self.side_2 and self.side_1>self.side_3:
            print(f"El lado 1 es el mayor, mide {self.side_1}")
        elif self.side_2>self.side_1 and self.side_2>self.side_3:
            print(f"El lado 2 es el mayor, mide {self.side_2}")
        else:
            print(f"El lado 3 es el mayor, mide {self.side_3}")

class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

class Diary:
    def __init__(self):
        self.contacts = []


    def add_contact(self, name, phone, email):
        #Esta función crea nuestro nuevo contacto, con los atributos q le pasamos por parámetro
        new_contact = Contact(name, phone, email)
        #Agregamos los contactos a la lista de contactos
        self.contacts.append(new_contact)


    def list_of_contacts(self):
        #Esta función muestra la lista de contactos
        for contact in self.contacts:
            print("------------")
            print(f"Nombre: {contact.name}")
            print(f"Teléfono: {contact.phone}")
            print(f"Email: {contact.email}")
            print("------------")

    def search_contact(self, name):
        #Con esta función buscamos contactos por el nombre
        for contact in self.contacts:
            if contact.name == name:
                print(f"Nombre: {contact.name}")
                print(f"Teléfono: {contact.phone}")
                print(f"Email: {contact.email}")
                return
            #Si no encuentra el contacto devuelve el siguiente mensaje
        print("Contacto no encontrado")

    def edit_contact(self, name, new_phone, new_email):
        #Con esta función editamos el contacto y hace la busqueda por nombre
        for contact in self.contacts:
            if contact.name == name:
                contact.phone = new_phone
                contact.email = new_email
                print("Contacto actualizado")
                return
            #Si no lo encontramos devuelve el siguiente mensaje
        print("Contacto no encontrado")

    def menu(self):
        #Esta función nos muestra el menú
        while True:
            print("\nMenú de Agenda:")
            print("1. Añadir contacto")
            print("2. Lista de contactos")
            print("3. Buscar contacto")
            print("4. Editar contacto")
            print("5. Cerrar agenda")
            #Le pedimos al usuario q ingrese un número con la opción q desea seleccioanr
            option = input("Selecciona una opción: ")

            if option == "1":
                name = input("Nombre: ")
                phone = input("Teléfono: ")
                email = input("Email: ")
                self.add_contact(name, phone, email)
            elif option == "2":
                self.list_of_contacts()
            elif option == "3":
                name = input("Nombre a buscar: ")
                self.search_contact(name)
            elif option == "4":
                name = input("Nombre a editar: ")
                new_phone = input("Nuevo teléfono: ")
                new_email = input("Nuevo email: ")
                self.edit_contact(name, new_phone, new_email)
            elif option == "5":
                #Si el usuario elige la opción 5, el ciclo se rompera y mostrara el siguiente mensaje
                print("Agenda cerrada. ¡Hasta luego!")
                break
            else:
                #Si ingresamos una opción invalida el programa nos mostrar ek siguiente mensaje
                print("Opción no válida. Inténtalo de nuevo.")
