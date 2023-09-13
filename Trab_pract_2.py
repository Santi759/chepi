#Ejercicio 1

años = int(input("Ingrese la cantidad de años que tiene su computador: "))

if años < 0:
    print("Fecha ingresada inválida")
elif años <= 2:
    print("El computador es nuevo")
else:
    print("El computador es viejo")

#Ejercicio 2

num = int(input("Ingrese un número entero: "))
if num < 0:
    print("ERROR")

#Ejercicio 3

nombre_1 = input("Ingrese el primer nombre: ")
nombre_2 = input("Ingrese el segundo nombre: ")

primera_letra_nom_1 = nombre_1[0].lower()
primera_letra_nom_2 = nombre_2[0].lower()

if primera_letra_nom_1 == primera_letra_nom_2:
    print("Coincidencia")
else:
    print("No hay coincidencia")

#Ejercicio 4

print("¡Bienvenido a las Elecciones! Presione la letra indicada entre parentesis segun el candidato que desea votar")
print("Partido Rojo (A)")
print("Partido de la Verdad (B)")
print("Partido Azul (C)")
voto = input("Seleccione un partido (A-B-C)")

if voto.upper() == "A":
    print("Usted ha votado por el Partido Rojo")
elif voto.upper() == "B":
    print("Usted ha votado por el Partido de la Verdad")
elif voto.upper() == "C":
    print("Usted ha votado por el Partido Azul")
else:
    print("Opción incorrecta")


#Ejercicio 5

letra = input("Ingrese una letra: ")
if len(letra) >= 2:
    print("Solo debe ingresar una letra")
    exit()
elif letra.upper() == "A":
    print(letra, " Es una vocal")
elif letra.upper() == "E":
    print(letra, " Es una vocal")
elif letra.upper() == "I":
    print(letra, " Es una vocal")
elif letra.upper() == "O":
    print(letra, " Es una vocal")
elif letra.upper() == "U":
    print("Es una vocal")
else:
    print(letra, " Es una consonante")

#Ejercicio 6

año = int(input("Ingrese un año: "))

if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
    print(f" {año} Es bisiesto")
else:
    print(f"{año} No es bisiesto")

#Ejercicio 7

num_1 = int(input("Ingrese un número entero"))
num_2 = int(input("Ingrese un número entero"))
num_3 = int(input("Ingrese un número entero"))

if (num_1<num_2 and num_1<num_3):
    print(num_1, "Es el menor de los tres")
elif (num_2<num_1 and num_2<num_3):
    print(num_2, "Es el menor de los tres")
else:
    print(num_3," Es el menor de los tres")

#Ejercicio 8

usuario = input("Nombre de usuario: ")
contraseña = input("Contraseña: ")

if (usuario == "Gwenevere" and contraseña == "excalibur"):
    print("Usuario y contraseña correctos!!Puede ingresar a Camelot--->")
else:
    print("Acceso Denegado X")

#Ejercicio 9

#Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre. 
#El grupo A está formado por las mujeres con un nombre anterior a la M y los hombres con un nombre posterior a la
#N y el grupo B por el resto. Escribir un programa que pregunte al usuario su nombre y sexo, 
#y muestre por pantalla el grupo que le corresponde.

nombre = input("Ingrese su nombre: ")
nombre= nombre.capitalize()
sexo = input("ingrese su sexo (M-F): ")
sexo = sexo.capitalize()

if (sexo == "F") and (nombre[0] == "A" and "B" and "C" and "D" and "E" and "F" and "G"  and "H" and "I" and "J" and "K" and "L" and "M"):
    print("Grupo A")
elif (sexo.lower == "m" and nombre[0].lower() == "n" and "ñ" and "o" and "p" and "q" and "f" and "r"  and "s" and "t" and "u" and "v" and "w" and "x" and "y" and "z"):
    print("Grupo A")
else:
    print("Grupo B")


#Ejercicio 10

print("¡¡Bienvenido a Arcade!!")
edad = int(input("Para ingresar primero dinos tu edad: "))

if edad < 4:
    print("Puede ingresar sin costo!!")
elif edad >= 4 and edad <=18:
    print("El costo para ingresar es de $500")
elif edad > 18:
    print("EL costo para ingresar es de $1000")

#Ejercicio 11

print("<<<Bienvenido a Pizzeria BELLA NAPOLI>>>")
print("<<PIZZA VEGETARIANA>>")
print("Igredientes ---> mozzarella -- tomate ---> Agregados:  Pimiento o Tofu")
print("<<PIZZA NO VEGETARIANA>>")
print("Igredientes ---> mozzarella -- tomate ---> Agregados:  Peperoni, Jamón o Tofu:")
opcion =input("¿Cuál opcion desea prober pedir? Vegetariana (presione V) No vegetariana (Presione N)")

if opcion.upper() == "V":
    ingredientes = input("Opcion Vegetariana ---> Desea agregarle Pimiento (P) o Tofu (T): ")
    if ingredientes.upper() == "P":
        print("Su pedido esta en proceso: Pizza Vegetariana --> mozzarella, tomate y Pimiento")
    else:
        print("Su pedido esta en proceso: Pizza Vegetariana --> mozzarella, tomate y Tofu")
else:
    ingredientes = input("Opcion No Vegetariana ---> Desea agregarle Peperoni (P) -- Jamón (J) o Salmón (S): ")
    if ingredientes.upper() == "P":
        print("Su pedido esta en proceso: Pizza No Vegetariana --> mozzarella, tomate y Peperoni")
    elif ingredientes.upper() == "J":
        print("Su pedido esta en proceso: Pizza No Vegetariana --> mozzarella, tomate y Jamón")
    else:
        print("Su pedido esta en proceso: Pizza No Vegetariana --> mozzarella, tomate y Salmón")

#Ejercicio 12

año_actual =int(input("Ingrese el año actual: "))
cualq_año = int(input("Ingrese un año cualquiera: "))

if año_actual > cualq_año:
    dist = (año_actual-cualq_año)
    print(f"Han pasado {dist} años desde {cualq_año}")
else:
    dist = (cualq_año-año_actual)
    print(f"Faltan {dist} años para llegar a {cualq_año}")

#Ejercicio 13

num_1 = int(input("Ingrese el primer número: "))
num_2 = int(input("Ingrese el segundo número: "))

if (num_1 <= 0 or num_2 <=0):
    print("No se pueden ingresar valores nulos o negativos")
else:
    if num_1 > num_2:
        mayor = num_1
        menor = num_2
        if mayor % menor ==0:
            print(f"{mayor} es multiplo de {menor}")
        else:
            print(f"{mayor} no es multiplo de {menor}")
    else:
        mayor = num_2
        menor = num_1
        if mayor % menor ==0:
            print(f"{mayor} es multiplo de {menor}")
        else:
            print(f"{mayor} no es multiplo de {menor}")

#Ejercicio 14

valor_a = float(input("Ingrese el valor de a: "))
valor_b = float(input("Ingrese el valor de b: "))
if a==0:
    if b==0:
        print("La ecuación tiene infinitas soluciones (0x + 0 = 0)")
    else:
         print("La ecuación no tiene solución (0x + {} = 0)".format(b))
else:
    x = -b / a
    print("La solución de la ecuación {}x + {} = 0 es x = {}".format(a, b, x))
    

#Ejercicio 15

preg = input("¿Qué desea Calcular? Si desea calcular el área de un triángulo ingrese T o t y si desea calcular el área de un círculo ingrese C o c: ")

if preg.upper() =="T":
    b = float(input("Ingrese la base del triángulo: "))
    h = float(input("Ingrese la altura del triángulo: "))
    area = (b*h)/2
elif preg.upper() == "C":
    r = float(input("Ingrese el radio del círculo: "))
    import math
    area = (math.pi * r**2)
    print(f"El área del círculo es {area} ")
else:
    print("Debe ingresar T o C para realizar algún calculo")

#Ejercicio 16
#Haz una calculadora básica pida al usuario dos valores, a y b.
#Según la opción que desean, realizar la operación:
#Si operación es 1 entonces debemos ver el resultado de a + b
#Si operación es 2 entonces debemos ver el resultado de a * b
#Si operación es 3 entonces debemos ver el resultado de a - b
#Si operación es 4 entonces debemos ver el resultado de a / b

num_a = float(input("Ingrese el valor de a: "))
num_b = float(input("Ingrese el valor de b: "))
print("Calculadora ---> (1---> suma) (2---> multiplicación) (3---> resta) (4---> división"))
func = int(input("Ingrese el número según la función que desea hacer:"))

if func == 1:
    suma = num_a+num_b
    print(suma)
elif func == 2:
    mult = num_a*num_b
    print(mult)
elif func == 3:
    resta = num_a-num_b
    print(resta)
elif func == 4:
    if num_b == 0:
        print("Math Error!")
    else:
        div = num_a/num_b
        print(div)
else:
    print("Error")

#Ejercicio 17

dia = input("Ingresar día de la semana: ")

if dia.capitalize() == "Lunes":
    print("Buen comienzo de semana")
elif dia.capitalize() == "Viernes":
    print("Ultimo día de la semana laboral")
elif (dia.capitalize() == "Sabado" or dia.capitalize() == "Domingo"):
    print("Buen fin de semana")
else:
    print("Disfrute su semana")

#Ejercicio 18
#Preguntar al usuario el total de horas trabajadas en el mes y el salario por hora.
#La jornada de trabajo mínima es de 48 horas. 
# Calcular, dadas las horas trabajadas, si trabajó horas extras y mostrar esta cantidad.
#Mostrar su salario total, tomando en cuenta que las horas extras serán pagadas un 10% más que las horas 
#laborales comunes.

horas = int(input("Total de horas trabajadas: "))
min = 1000
if horas <= 48:
    print(f"Usted cumplio con la jornada min {horas} hs su salario es de usd{min}")
elif horas > 48:
    extra = (horas-48)*0.1
    porc = min*extra
    salario = porc+min
    print(f"usted trabajo {horas} su salario es de usd{salario}")

#Ejercicio 19
#Determinar cuánto se debe pagar por una cantidad de lápices considerando que si son 1000 o más, 
#existe un descuento de 7% y teniendo en cuenta que el costo por lápiz es de $60; 
#de lo contrario no hay descuento.

lapices = int(input("Ingrese la cantidad de lapices que llevara: "))
costo = 60

if lapices >= 1000:
    descuento = 60 * 0.7
    total= lapices*descuento
    print(f"El total a pagar por {lapices} lapices es de ${total}")
else:
    total = lapices*costo
    print(f"El precio final por {lapices} lapices es de ${total} no hay descuento")

#Ejercicio 20

nota_1 = float(input("Ingrese la nota 1: "))
nota_2 = float(input("Ingrese la nota 2: "))
nota_3 = float(input("Ingrese la nota 3: "))
nota_4 = float(input("Ingrese la nota 4: "))

prom = (nota_1 + nota_2 + nota_3 + nota_4)/4

if prom >= 6:
    print(f"Felicidades, su promedio es de {prom} usted aprobo")
else:
    print(f"Usted ha desaprobado con un promedio de {prom}")



