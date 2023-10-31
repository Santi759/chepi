import funciones_tp_5
#Ejercicio_1
#Escribir una función que, dado un número de DNI, retorne True si el número es 
# válido y False si no lo es. Para que un número de DNI sea válido debe tener entre 7 y 8 dígitos.

dni = input("Ingrese su número de documento: ")
ret = funciones.num_dni(dni)

if ret:
    print(f"Número de documento {dni} ")
else:
    print(f"Número de documento Falso {dni} ")
print("---------------------------------------------")
#Ejercicio_2
#Escribir una función que, dado un string, retorne la longitud de la última palabra. 
#Se considera que las palabras están separadas por uno o más espacios. También podría haber espacios al 
#principio o al final del string pasado por parámetro.

phrase = input("Ingrese una frase: ")
length = funciones.long_word(phrase)
print(f"La ultima palabra de <<<{phrase}>>> tiene {length} letras de largo")
print("---------------------------------------------")

#Ejercicio_3

print("<<< Bienvenido a RiverID >>>")
name = input("Ingrese su nombre completo: ")
back=""
while name != back:
    dni =input("Ingrese su dni: ")
    ret = funciones.num_dni(dni)
    while ret==False:
        print("Ingrese un DNI válido:")
        dni =input("Ingrese su dni: ")
        ret = funciones.num_dni(dni)
    funciones.carnet_id(name,dni)
    name = input("Ingrese su nombre completo: ")
print("---------------------------------------------")

#Ejercicio_4
#Crea un programa que pida dos número enteros al usuario y diga si alguno de ellos es múltiplo del otro. 
#Crea una función que reciba los dos números, y devuelve si el primero es múltiplo del segundo.

num_1 = int(input("Ingrese el primer número: "))
num_2 = int(input("Ingrese el segundo número: "))
funciones.multiple(num_1,num_2)
print("---------------------------------------------")

#Ejercicio_5
#Crear una función que calcule la temperatura media de un día a partir de la 
#temperatura máxima y mínima. Crear un programa principal, que utilizando la función anterior, 
#vaya pidiendo la temperatura máxima y mínima de cada día y vaya mostrando la media. 
#El programa pedirá el número de días que se van a introducir.
days = int(input("Ingrese la cantidad de días de los que desea saber la temperatura: "))
i=0
while days != i:
    maximum_temperature = float(input(f"Ingrese la temperatura máxima del día {i+1}: "))
    minimum_temperature = float(input(f"Ingrese la temperatura miníma del día {i+1}: "))
    i +=1
    print(f"la temperatura media del día {i} es {funciones.medium_temperature(maximum_temperature,minimum_temperature)}°")
print("---------------------------------------------")

#Ejercicio_6
#Crea una función que reciba como parámetro un texto y devuelve una cadena con un espacio adicional 
# tras cada letra. Por ejemplo, “Hola, tú” devolverá “H o l a , t ú “. 
# Crea un programa principal donde se use dicha función.

word = input("Ingrese una palabra: ")
print(f"{word} ---> {funciones.space(word)}")
print("---------------------------------------------")

#Ejercicio_7
#Crea una función que recibe una lista con valores numéricos y devuelve el valor máximo y el mínimo. 
#Crea un programa que pida números por teclado y muestre el máximo y el mínimo, utilizando la función anterior.

list_num = []
elements = int(input("Ingrese la cantidad de elementos de la lista: "))

for i in range(elements):
    num = float(input("Ingrese un elemento: "))
    list_num.append(num)

print(list_num)
funciones.num_may_min(list_num)
print("---------------------------------------------")
#Ejercicio_8
#Diseñar una función que calcule el área y el perímetro de una circunferencia. 
# Utiliza dicha función en un programa principal que lea el radio de una circunferencia y muestre su área y perímetro.

radio = float(input("Ingrese el radio de la circunferencia: "))
funciones.area_perimeter(radio)

print("---------------------------------------------")
#Ejercicio_9
#Crear una subrutina llamada “login”, que recibe un nombre de usuario y una contraseña y te devuelve 
# Verdadero si el nombre de usuario es “usuario1” y la contraseña es “asdasd”. Además recibe el número de intentos que 
# se ha intentado hacer login y si no se ha podido hacer login incremente este valor.
#Crear un programa principal donde se pida un nombre de usuario y una contraseña y se intente hacer 
# login, solamente tenemos tres oportunidades para intentarlo.

user_name = input("Usuario: ")
password = input("Contraseña: ")
attempts = 2
funciones.login(user_name, password, attempts)

print("---------------------------------------------")
#Ejercicio_10
#Escribir una función que aplique un descuento a un precio. 
#Esta función tiene que recibir un diccionario con los precios y porcentajes del carrito de compra, 
#aplicar los descuentos a los productos del carrito  y devolver el precio final de la compra.

trolley = {
    'producto1': 100,
    'producto2': 50,
    'producto3': 200
}

discounts = {
    'producto1': 10,
    'producto3': 15
}

final_price = funciones.aplicar_descuento(trolley, discounts)
print(f'El precio final de la compra es: ${final_price}')

print("---------------------------------------------")
#Ejercicio_11
#Escribir una función que reciba otra función y una lista, y devuelva otra lista con el resultado de 
#aplicar la función dada a cada uno de los elementos de la lista.

nums =[1,2,3,4,5]
results = funciones.function(funciones.fold,nums)

print(f"Lista original {nums}")
print(f"Lista duplicada {results}")

print("---------------------------------------------")
#Ejercicio_12
#Escribir una función que reciba una frase y devuelva un diccionario con las palabras que contiene y su longitud
phrase = input("Ingrese una frase: ")
result = funciones.count_word_length(phrase)
print(result)

print("---------------------------------------------")
#Ejercicio_13
vector = [3, 4]  
result = funciones.vector_module(vector)
print("El módulo del vector es:", result)

print("---------------------------------------------")
#Ejercicio_14
#Requerir al usuario que ingrese un número entero e informar si es primo o no, 
#utilizando una función booleana que lo decida.

num=int(input("Ingrese un número: "))
while num !=0:
    cousin = funciones.num_pri(num)
    if cousin == True:
        print(f"{num} es primo")
    else:
        print(f"{num} no es primo")
    num=int(input("Ingrese un número. Para salir ingrese 0: "))

print("---------------------------------------------")
#Ejercicio_15
if __name__ == "__main__":
    funciones.main()

print("---------------------------------------------")
#Ejercicio_16
#Solicitar al usuario un número entero y luego un dígito. 
# Informar la cantidad de ocurrencias del dígito en el número, 
# utilizando para ello una función que calcule la frecuencia.

num = int(input("Por favor, ingresa un número entero: "))
dig = int(input("Por favor, ingresa un dígito: "))
occurrences = funciones.count_occurrences(num, dig)
print(f"El dígito {dig} aparece {occurrences} veces en el número {num}.")

print("---------------------------------------------")

#Ejercicio_17
#Solicitar al usuario el ingreso de números primos. 
# La lectura finalizará cuando ingrese un número que no sea primo. Por cada número, 
# mostrar la suma de sus dígitos. También solicitar al usuario un dígito e informar 
# la cantidad de veces que aparece en el número (frecuencia). Al finalizar el programa, 
# mostrar el factorial del mayor número ingresado.


cicle=True

while cicle != False:
    num=int(input("Ingrese un número. Para salir ingrese un número no primo: "))
    cicle=funciones.num_pri(num)
    if cicle == False:
        break
    print("Suma de los digitos:")
    bigger = funciones.big_num(num)
    print(funciones.sum_dig(num))
    dig = int(input("Por favor, ingresa un dígito: "))
    occurrences = funciones.count_occurrences(num, dig)
    print(f"El dígito {dig} aparece {occurrences} veces en el número {num}.")
print(funciones.factorial_1(bigger))



