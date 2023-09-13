#Ejercicio_1_1
x = 0

while x <= 30:
    x +=1
    if x==15:
        break
    if (x == 4 or x==6 or x==10):
        print(f"El valor de x: {x} fue salteado")
        continue
    print("El valor del bucle x:" ,x)

print(f"El bucle se rompio cuando el valor de x era {x}")

print("-------------------------------------------------------------")

#Ejercicio_1_2
#Escriba un programa que acepte una secuencia de líneas e imprima todas las 
#líneas convertidas en mayúsculas. Deje una línea en blanco para indicar que ha finalizado la entrada de líneas.
phrase = []
print("Escirba una frases, cuando desee finalizar deje el espacion en blanco")
while True:
    esp = input()
    if esp:
        esp = phrase.append(esp.upper())
    else:
        break

for i in phrase:
    print(i)

print("-----------------------------------------------------------------")

#Ejercicio_2

while True:
    ext = input("Presione D para depositar  --- Presione R para retirar  --- Deje un espacio en blanco para salir ")
    if ext.upper() == "D":
        d = int(input("Desposito : "))
        if d<0:
            print("No puede ingresar un valor negativo")
            d -= d 
    elif ext.upper() == "R":
        r = int(input("Retiro: "))
        if r>d:
            print("No puede retirar más de lo q tiene")
            r -= r 
        d -= r
    elif ext == "":
        break
    else:
        print("Ingrese un cáracter válido")

print(f"Monto restante ${d}")  
print("-----------------------------------------------------------------")

#Ejercicio_3
num = int(input("Ingrese un numero mayor a 1: "))
prime=0

while num>1:
    if (num %2==0 or num %3==0):    
        print("")
    else:
        prime +=1
    num = int(input("Ingrese un numero mayor a 1: "))
    if num == 0:
        break
print(f"Se ingresaron {prime} números primos")
print("-----------------------------------------------------------------")

#Ejercicio_4

year_1 = int(input("Ingrese el primer año: "))
year_2 = int(input("Ingrese el segundo año año: "))
year_may = 0
year_min = 0

if year_2>year_1:
    year_may=year_2
    year_min=year_1
else:
    year_may=year_1
    year_2=year_min

for i in range(year_min, year_may+1):
    if (i % 4 == 0 and i % 100 != 0) or (i % 400 == 0):
        print(f"{i} es año bisiesto")
    else:
        continue
    if (i %10==0):
        print(f"{i} es un año multiplo de 10")
    else:
        continue
print("-----------------------------------------------------------------")

#Ejercicio_5

for i in range(21):
    if i %2==1:
        continue
    print(i)
print("-----------------------------------------------------------------")

#Ejercicio_6
num =[1,5,85,49,67,759,7,18,45,28,56,100,9,8,4]
search = int(input("Ingrese el número que desea encontrar: "))
array = 0

for i in num:
    if i == search:
        break
    else:
        print(i)
    array +=1

print(f"el número {search} se encontro en la posición {array}")
print("-----------------------------------------------------------------")

#Ejercicio_7

while True:
    print("---- MENÚ ----")
    print("----OPCION 1 (Presione 1)----")
    print("----OPCION 2 (Presione 2)----")
    print("----OPCION 3 (Presione 3)----")
    print("---- SALIR (Presione 0) ----")
    option = input("Seleccione una opción: ")
    if option == "1":
        print("----------------------------")
        print("Usted eligió la opción 1")
        print("----------------------------")
    elif option =="2":
        print("----------------------------")
        print("Usted eligió la opción 2")
        print("----------------------------")
    elif option =="3":
        print("----------------------------")
        print("Usted eligió la opción 3")
        print("----------------------------")
    elif option =="0":
        break
    else:
        print("----------------------------")
        print("Usted eligió una opción no válida")
        print("----------------------------")

print("---- Hasta Pronto ----")
    







