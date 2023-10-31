from Class_tp_9 import MyPerson,Account,Triangle,Diary
#Ejercicio_1

#Inicializamos el objeto person1
person1 = MyPerson(
    name="",
    age=0,
    dni=""
)

#Le damos un valor al atributo nombre
new_name=input("Ingrese su nombre: ")
person1.set_name(new_name)
print("----------------------------------------------------------------------")
#Le damos un valor al atributo edad
new_age=int(input("Ingrese su edad: "))
person1.set_age(new_age)
print("----------------------------------------------------------------------")
#Le damos un valor al atributo dni
new_dni=input("Ingrese su dni: ")
person1.set_dni(new_dni)
print("----------------------------------------------------------------------")
#Mostramos los datos de el objeto creado
print(f"Nombre: {person1.get_name()} --- Edad: {person1.get_age()} --- DNI: {person1.get_dni()} ")
print("----------------------------------------------------------------------")

#Verificamos si es mayor de edad
if (person1.is_older()==True):
    print(f"{person1.get_name()} Es mayor de edad")
else:
    print(f"{person1.get_name()} Es menor de edad")

#Ejercicio_2

#Inicializamos el oobjeto cuenta_1
account_1 = Account(
    holder="",
    amount=0
)
print("----------------------------------------------------------------------")
#Verificamos que ingrese un nombre para el titular
while account_1.get_holder()=="":
    new_holder=input("Ingrese el nombre del titular: ")
    account_1.set_holder(new_holder)

#Le damos un valor al metodo deposit
print("----------------------------------------------------------------------")
new_amount=float(input("Ingrese la cantidad de dinero que depositara: "))
account_1.deposit(new_amount)

account_1.set_amount(new_amount)
print("----------------------------------------------------------------------")
#Mostrar Datos
account_1.display()
print("----------------------------------------------------------------------")
#Retirar dinero
extraction=float(input("Ingrese el monto que desea retirar: "))
account_1.extraction(extraction)
print("----------------------------------------------------------------------")
#Mostramo los datos actualizados
account_1.display()
print("----------------------------------------------------------------------")
#Ejercicio_3

#Inicializamos el objeto Triángulo
triangle_1=Triangle()
print("----------------------------------------------------------------------")
#Hacemos uso del método para ver que tipo de triángulo es
triangle_1.type_triangle()
#Hacedmos uso del método para ver cuál es su lado mayor
triangle_1.long_side()
print("----------------------------------------------------------------------")

#Ejercicio_4

#Inicializamos el objeto my_diary
my_diary = Diary()
my_diary.menu()
