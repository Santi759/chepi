#Ejercicio 1

word = input("Ingrese cualquier palabra: ")

for i in range(10):
    print( i+1,":",word)

#Ejercicio 2
#Escribir un programa que pregunte al usuario su edad y muestre por pantalla 
#todos los años que ha cumplido (desde 1 hasta su edad).

age = int(input("Ingrese su edad: "))
years = 1

for i in range(age):
    print(f" Ha cumplido {years} años")
    years += 1

#Ejercicio 3
#Escribir un programa que pida al usuario un número entero positivo y 
#muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas.


num = int(input("Ingrese un número entero positivo: "))
cont = 1
array = " "
for i in range(num):
    if cont % 2 == 1:
        array += str(cont)+ " , "
    cont += 1
print(array)

#Ejercicio 4
#Escribir un programa que pida al usuario un número entero positivo y 
# muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas.

num = int(input("Ingrese un numero entero positivo: "))
cont = num
array = ""

for i in range(num+1):
    array += str(cont)+ " , " 
    cont -= 1
print(array)

# Ejercicio 5

inv = float(input("Ingrese la cantidad de dinero que desea invertir: $"))
interest = float(input("Ingrese el interés anual: "))
years = int(input("Ingrese la duración de la inversión: "))
total = 0

for n in range( 1, years+1):
    profit = ((inv/100)*interest)*n
    print(f"Las ganancias en el {n} año sera de ${profit}")

#Ejercicio 6
#Escribir un programa que pida al usuario un número entero y 
#muestre por pantalla un triángulo rectángulo como el de más abajo, de altura el número introducido.

num = int(input("Ingrese un número entero para darle altura al triángulo: "))

for i in range(num):
    print("*"*(i+1))

#Ejercicio 7
#Escribir un programa que muestre por pantalla las tablas de multiplicar del 1 al 10

for i in range(10):
    n=1
    for j in range(10):
        mult = n*(j+1)
        print(f"{i+1} * {j+1} =  {mult}")
    n +=1

#Ejercicio 8
#Escribir un programa que pida al usuario un número entero y 
# muestre por pantalla un triángulo rectángulo como el de más abajo.

num = int(input("Ingrese el tamaño del triángulo: "))

for i in range(1,num+1,2):
    for j in range(i, 0, -2):
        print(j, end=" ")
    print("")

#Ejercicio 9
# Escribir un programa que almacene la cadena de caracteres contraseña en una variable,
# pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.

password = input("Ingrese la contraseña: ")

while password != "contraseña":
    print("Contaseña incorrecta. Vuelva a  intentarlo")
    password = input("Ingrese la contraseña: ")

print("Contraseña correcta!!")


#Ejercicio 10

num = int(input("Ingrese un número entero: "))

while num > 0:
    if (num % 2 == 0):
        print(f"{num} no es primo")
    elif (num % 3 == 0):
        print(f"{num} no es primo")
    else:
        print(f"{num} es un número primo")
    num = int(input("Ingrese un número entero, si desea salir presione 0: "))

#Ejercicio 11
#Escribir un programa que pida al usuario una palabra y luego muestre por pantalla una a una las letras de 
#la palabra introducida empezando por la última.

word_input = input("Ingrese una palabra: ")
ret=-1

for i in range(len(word_input)):
    print(word_input[ret])
    ret = ret-1

#Ejercicio 12
#Escribir un programa en el que se pregunte al usuario por una frase y una letra, y 
# muestre por pantalla el número de veces que aparece la letra en la frase.

phrase = input("Ingrese una frase: ")
letter = input("Ingrese una letra: ")
let=phrase.count(letter)

for i in range(let):
    print(letter)

#Ejercicio 13
#Escribir un programa que muestre el eco de todo lo que el usuario introduzca hasta que el 
#usuario escriba “salir” que terminará.
word = input("Ingrese una palabra: ")
while word.lower() != "salir":
    print(word.lower())
    word = input()

#Ejercicio 14
#Escriba un programa que pida dos números enteros y escriba 
#qué números son pares y cuáles impares desde el primero hasta el segundo.

num_1 = int(input("Ingrese un número entero:"))
num_2 = int(input("Ingrese otro número entero:"))
if num_2 > num_1:
    num_eld = num_2
    num_min = num_1
else:
    num_eld = num_1
    num_min = num_2

for i in range(num_min, num_eld+1):
    if i %2==0:
        print(i," número par")
    else:
        print(i," Número impar")


#Ejercicio 15

num = int(input("Ingrese un número entero mayor a 0: "))
div = 1

for i in range(num):
    if (num % div ==0):
        print(f"{div} es divisor de {num}")
    div += 1

#Ejercicio 16
#Escriba un programa que pregunte cuántos números se van a introducir, 
#pida esos números y escriba cuántos negativos ha introducido.

question = int(input("Ingrese cuantos números se van a introducir: "))
coun = 0
for i in range(question):
    num =int(input("Ingrese un número: "))
    if num < 0:
        coun += 1 

print("Se introdujeron " ,coun, "negativos")

#Ejercicio 17
#Solicitar al usuario que ingrese una frase y luego imprimir un 
#listado de las vocales que aparecen en esa frase (sin repetirlas).

phrase = (input("Ingrese una frase: "))

for i in range(1):
    if "a" in phrase:
        print("Se encontro: a")
    if "e" in phrase:
        print("Se encontro: e")
    if "i" in phrase:
        print("Se encontro: i")    
    if "o" in phrase:
        print("Se encontro: o")
    if "u" in phrase:
        print("Se encontro: u")

#Ejercicio 18
#Crear un algoritmo que muestre los primeros 10 números de la sucesión de Fibonacci. 
#La sucesión comienza con los números 0 y 1 y, a partir de éstos, 
#cada elemento es la suma de los dos números anteriores en la secuencia: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55…
    
fib = int(0)
fib_2 = int(1)
result = int(0)
while result < 55:
    for i in range (0, 10-1):
        result = (fib) + (fib_2)
        fib =  fib_2
        fib_2 = result
        print(result)

#Ejercicio 19
#Escriba un programa que simule una alcancía. El programa solicitará primero una cantidad, 
#que será la cantidad de dinero que queremos ahorrar. A continuación, el programa solicitará 
#una y otra vez las cantidades que se irán ahorrando, hasta que el total ahorrado iguale o supere al objetivo. 
#El programa deberá comprobar que las cantidades ingresadas sean positivas.
savings = float(input("Ingrese la cantidad de dinero que desea alcanzar: "))
cash = float(0.0)

while cash < savings:
    money = float(input("Cuánto dinero guardara: "))
    if money < 0:
        while money<0:
            money = float(input("Debe ingresar una cantidad de dinero positiva: ")) 
    cash += money


#Ejercicio 20

num = int(input("Ingrese un número entero: "))
sum = 0
while num != 0:
    sum += num
    num = int(input("Ingrese otro número para sumar o 0 si desea salir: "))

print(f"La suma total es {sum}")

#Ejercicio 21
#Leer números enteros positivos de teclado, hasta que el usuario ingrese el 0. 
#Informar cuál fue el mayor número ingresado.
num = int(input("Ingrese un número entero: "))
eld = num
while num != 0:
    num = int(input("Ingrese otro número o 0 si desea salir: "))
    if num > eld:
        eld= num

print(f"El número mayor fue {eld}")

#Ejercicio 22
#Solicitar al usuario que ingrese números enteros positivos y, por cada uno, 
# imprimir la suma de los dígitos que lo componen. La condición de corte es que se ingrese el 
# número -1. Al finalizar, mostrar cuántos de los números ingresados por el usuario fueron números pares.

nums = 0
digits_sum = 0
pair = 0
while nums != "-1":
    nums = input("Ingrese un número: ")
    if nums == "-1":
        break
    for x in nums:
        if x == "-":
            continue
        else:
            digits_sum += int(x)
    print("La suma de los dígitos del número ingresado es: ", digits_sum)
    print("Para terminar ingrese el número -1.")
    if int(nums) % 2 == 0:
            pair += 1
    digits_sum = 0
print(pair, " de los números ingresados fueron números pares.")

#Ejercicio 23
#Crear un programa que permita al usuario ingresar 
# los montos de las compras de un cliente 
#(se desconoce la cantidad de datos que cargará, la cual puede cambiar en cada ejecución), 
#cortando el ingreso de datos cuando el usuario ingrese el monto 0.

cost = int(0)
while True:
    mount = int(input("Ingrese el monto del producto o 0 si termino de cargar los productos: "))
    cost = cost + mount
    if mount == 0:
        break
print(f"El costo total es de: $ {cost}")

#ejercicio 24

print("<<<Bienvenido al sistema>>>")
mount = 1
total = 0
end_loop = 1
while end_loop != 0:
    mount = int(input("Ingrese el monto a pagar por su producto o 0 si termino de cargar los productos: $"))
    if mount < 0:
        print("Por favor, ingrese un monto válido")
        continue
    elif mount == 0:
        print("El total final a pagar es de: $", total)
        end_loop = 0
        break
    else:
        total += mount
    print("Total a pagar: $", total)
if total > 1000:
    total = total - (total * 0.10)
    print("Por exeder los $1000 obtienes un descuento del 10%. El total final a pagar es de: $", total)

#Ejercicio 24
#Si ingresa un monto negativo, no se debe procesar y 
# se debe pedir que ingrese un nuevo monto. 
# Al finalizar, informar el total a pagar teniendo en cuenta que, si 
# las ventas superan el total de $1000, se le debe aplicar un 10% de descuento.
print("<<<Bienvenido al sistema>>>")
mount = 1
total = 0
end_loop = 1
while end_loop != 0:
    mount = int(input("Ingrese el monto a pagar por su producto o 0 si termino de cargar sus productos: $"))
    if mount < 0:
        print("Por favor, ingrese un monto válido")
        continue
    elif mount == 0:
        print("El total final a pagar es de: $", total)
        end_loop = 0
        break
    else:
        total += mount
    print("Total a pagar: $", total)
if total > 1000:
    total = total - (total * 0.10)
    print("Por exeder los $1000 obtienes un descuento del 10%. El total final a pagar es de: $", total)

#Ejercicio 25

num = int(input("Ingrese el número del que desea saber el factorial: "))
cont = num
numero = num

for i in range(num-1):
    cont = cont-1
    fact = (num * cont)
    num = fact
    print(numero,"*" ,cont, " = ", fact )

print(f"El factorial de {numero} es {fact}")
