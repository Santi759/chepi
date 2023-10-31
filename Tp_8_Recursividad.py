import funciones_recursivas
#Ejercicio_1

#Escribir una función que reciba un número positivo n y devuelva la cantidad de dígitos que tiene.
num_1 = int(input("Ingrese un número: "))
digits = funciones_recursivas.number_digits(num_1)
print(digits)

#Ejercicio_2
#Escribir una función que reciba 2 enteros n y b y devuelva True si n es potencia de b.

num_n=int(input("Ingrese un número entero: "))
num_b=int(input("Ingrese un número entero: "))

print(f"{funciones_recursivas.powers(num_n,num_b)}")

#Ejercicio_3
#Escribir una funcion recursiva que reciba como parámetros dos strings a y b, y 
#devuelva una lista con las posiciones en donde se encuentra b dentro de a. Ejemplo:

string_a = input("Ingrese una texto: ")
string_b = input("Ingrese la subcadena que quiere encontrar: ")
print(funciones_recursivas.search_string(string_a,string_b))

#Ejercicio_4

num = 5
if funciones_recursivas.odd(num):
    print(f"{num} es impar.")
else:
    print(f"{num} es par.")

#Ejercicio_5

elemt_max=[1,3,5,10,9,25,2,4]
result=funciones_recursivas.search_elderly(elemt_max)
print(f"El valor más grande de la lista es {result}")

#Ejercicio_6

list_num =[1,3,3,7]
replicate=int(input("ingrese la cantidad de veces que quiere replicar los elementos: "))
list_replicate=funciones_recursivas.replicate_element(list_num,replicate)
print(list_replicate)

#Ejercicio_7
n=int(input("Ingrese el valor de n: "))
p=int(input("Ingrese el valor de p: "))
result=funciones_recursivas.summation(n,p)
print(f"El valor de K({n},{p}) es {result}")

#Ejercicio_8
n = 4
k = 2
resultado = funciones_recursivas.pascal(n, k)
print(f"El valor en la fila {n} y la columna {k} del Triángulo de Pascal es {resultado}")

#Ejercicio_9
list_char = ['$', 'a', '&']
k = 2
funciones_recursivas.combinations(list_char, k)

#Ejercicio_10
n = 3  # Cambia N al número que desees
length,width = funciones_recursivas.measured_sheets_A(n)
print(f"Las medidas de la hoja A{n} son: Ancho = {length} mm, Largo = {width} mm")
