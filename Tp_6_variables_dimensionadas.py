import random

#Función para llenar la lista hasta que el usurio ingrese 0
def add_num(list_num):
    while True:
        num=float(input("Ingrese un nùmero. Ingrese el 0 para salir: "))
        if num==0:
            break
        list_num.append(num)

#Esta función toma el número q ingresamos y le pasamos por parametro y crea una lista con todos los números menores al
# que digitamos

def list_new(list_num,number):
    filtered_list = [x for x in list_num if x<number]
    return filtered_list

#Esta función cuenta la cantidad de veces que se repite un número en una lista
def generate_frequency_list(list_num):
    list_tupples =[]
    for num in list_num:
        count = list_num.count(num)
        # Verificar si la tupla ya existe en la lista
        if (num, count) not in  list_tupples:
            #Si la tupla no exite en la lista, crea una tupla con el número y la cantidad de veces q se repite
            list_tupples.append((num, count))
    return  list_tupples

#con esta función llenamos la lista de alumnnos de primaria
def add_list_primary(list_primary):
    print("Ingrese los nombres de los alumnos de Primario")
    while True:
        #Ingresaremos nombres hasta q el usuario ingrese unax
        name = input("Ingrese el nombre del alumno. Ingrese x para finalizar: ")
        if name.lower() == "x": #Verifica si el usuario ingreso una x
            break
        list_primary.append(name.capitalize()) #Agregamos el nombre ingresado a la lista
    return list_primary

#con esta función llenamos la lista de alumnnos de secundaria
def add_list_secundary(list_secundary):
    print("Ingrese los nombres de los alumnos de Secundario")
    while True:
        #Ingresaremos nombres hasta q el usuario ingrese unax
        name = input("Ingrese el nombre del alumno. Ingrese x para finalizar: ")
        if name.lower() == "x": #Verifica si el usuario ingreso una x
            break
        list_secundary.append(name.capitalize()) #Agregamos el nombre ingresado a la lista
    return list_secundary

#Esta función llena la lista vacia words_list[] con 50 Strings
def strings(words_list):
    while True:
        words=input("Ingrese una palabra: ")
        if len(words_list)==50: #Si la lista contiene 50 Strings el ciclo se rompera y retornara la lista llena
            break
        words_list.append(words) #Mientras la lista no llegue a 50 Strings agregaremos los string ingresados
    return words_list


def count_occurrences(words_list):
    #Creamos un diccionario vacio, donde guardaremos los caracteres
    occurrences={}
    #recorremos cada palabra de la lista
    for word in words_list:
        #recorremos cada caracter de la palabra
        for char in word:
            #guardamos en el diccionario cada caracter y si se repite lo sumamos
            occurrences[char]=occurrences.get(char,0)+1
    return occurrences

# Función para crear un tablero de cartas
def create_board(rows, columns):
    numbers = list(range(1, (rows * columns) // 2 + 1))
    cards = numbers + numbers
    random.shuffle(cards)
    board = [[0] * columns for _ in range(rows)]
    for i in range(rows):
        for j in range(columns):
            board[i][j] = cards.pop()
    return board

# Función para imprimir el tablero actual
def print_board(board, rows, columns):
    for i in range(rows):
        for j in range(columns):
            if board[i][j] == 0:
                print(" ", end=" ")
            else:
                print(f"{board[i][j]:2}", end=" ")
        print()

# Función para jugar al juego de Memoria
def play_memory():
    rows = 4 # Cambia el número de filas del tablero
    columns = 4 # Cambia el número de columnas del tablero
    board = create_board(rows, columns)
    revealed_cards = [[False] * columns for _ in range(rows)]

    while True:
        print_board(board, rows, columns)
        letter1 = input("Ingrese la fila y columna de la primera carta (ejemplo: 1 2): ")
        row1, column1 = map(int, letter1.split())
        card2 = input("Ingrese la fila y columna de la segunda carta (ejemplo: 2 3): ")
        row2, column2 = map(int, card2.split())

        if (row1 < 1 or row1 > rows or column1 < 1 or column1 > columns or
            row2 < 1 or row2 > rows or column2 < 1 or column2 > columns or
            revealed_cards[row1 - 1][column1 - 1] or revealed_cards[row2 - 1][column2 - 1] or
            (row1 == row2 and column1 == column2)):
            print("Entrada inválida. Inténtalo de nuevo.")
            continue

        if board[row1 - 1][column1 - 1] == board[row2 - 1][column2 - 1]:
            print("¡Encontraste una pareja!")
            revealed_cards[row1 - 1][column1 - 1] = True
            revealed_cards[row2 - 1][column2 - 1] = True
        else:
            print("No es una pareja válida. Intenta de nuevo.")

        if all(all(row) for row in revealed_cards):
            print("¡Felicidades, has ganado!")
            break


def get_diagonals(matriz):
    dimension = len(matriz) # Obtiene la dimensión de la matriz (el número de filas o columnas)
    main_diagonal = [matriz[i][i] for i in range(dimension)] # Obtiene la diagonal principal
    reverse_diagonal = [matriz[i][dimension - i - 1] for i in range(dimension)] # Obtiene la diagonal inversa
    return main_diagonal, reverse_diagonal


print("_____________________________________________________________________")

#Ejercicio_1
#Solicitar al usuario que ingrese números, estos deben guardarse en una lista. 
#Para finalizar el usuario debe ingresar 0, el cual no debe guardarse.

#creamos una lista vacía
list_num =[]

print("Llene la lista vacía")

#llamamos a la función para llenar la lista
add_num(list_num)
print(list_num)

print("_____________________________________________________________________")

#Ejercicio_2
#A continuación, solicitar al usuario que ingrese un número y, 
#si el número está en la lista, eliminar su primera ocurrencia. Mostrar un mensaje si no es posible eliminar.

#Le pedimos al usuario un número para eliminar
delete_num = float(input("Ingrese el nùmero que desea eliminar: "))

#Verificamos que el núm este en la lista
if delete_num in list_num:
    list_num.remove(delete_num)#Si lo encuentra lo elimina
else:
    print(f"No se encontro el numero {delete_num}")#Si no se encuentra en la lista mostrara el siguiente mensaje

print(list_num)

print("_____________________________________________________________________")

#Ejercicio_3
#Imprimir la sumatoria de todos los números de la lista.

print("Suma de todos los números que componen la lista: ")
#Imprime la suma de todos los números que componen la lista
print(sum(list_num))

print("_____________________________________________________________________")

#Ejercicio_4
#Solicitar al usuario otro número y crear una lista con los elementos de la lista original, 
# que sean menores que el número dado. Imprimir esta nueva lista, iterando por ella.

#Le pedimos al usuario un número
number = float(input("Ingrese un nùmero: "))

#llamamos a la funcíon para crear la lista nueva
filtered_list = list_new(list_num,number)
for i in filtered_list:
    print(i)
print(filtered_list)

print("_____________________________________________________________________")


#Ejercicio_5
#Generar e imprimir una nueva lista que contenga como elementos a tuplas, cada una compuesta por 
# un número de la lista original y la cantidad de veces que aparece en ella. Por ejemplo, 
# si la lista original es [5,16,2,5,57,5,2], la nueva lista contendrá: [(5,3),(16,1),(2,2),(57,1)]


#Llamamos a la función generate_frequency_list para crear una lista compuesta de tuplas
frequency_list = generate_frequency_list(list_num)
print("Nueva lista de tuplas (elemento, cantidad de veces que aparece):")
#imprimimos la nueva lista con tuplas
print(frequency_list)

print("_____________________________________________________________________")

#Ejercicio_6

#Creamos dos listas vacias una para los alumnos de primaria y otra para los de secundaria
list_primary =[]
list_secundary =[]

#llamamos a las funciones, que llenaran nuestras listas vacias
list_name_primary= add_list_primary(list_primary)
list_name_secundary= add_list_secundary(list_secundary)

#Creamos una lista nueva con todos los alumnos (Primaria y Secundaria) sin nombres repetidos
all_names =list(set(list_name_primary+list_name_secundary))
print("Nombres de todos los alumnos sin repeticiones:")
for name in all_names:
    print(name)

#Creamos otra lista con los alumnos que se repiten en ambos niveles
repeated_name= list(set(list_name_primary) & set(list_name_secundary))
print("Nombres que se repiten en ambos niveles:")
print(repeated_name)

#Creamos una lista con los alumnos de nivel primario que no se encuentran en el nivel secundario
primary_names_without_repetitions = list(set(list_name_primary) - set(list_name_secundary))
print("Nombres de nivel primario que no se repiten en nivel secundario:")
print(primary_names_without_repetitions)

print("_____________________________________________________________________")

#Ejercicio_7
#Escribir un programa que procese strings ingresados por el usuario. 
#La lectura finaliza cuando se hayan procesado 50 strings. Al finalizar, informar la cantidad total de 
#ocurrencias de cada carácter, en todos los strings ingresados. Ejemplo:
#‘r’:5
#‘%’:3
#‘a’:8

#Creamos una lista vacia, que guardara 50 Strings
words_list=[]

#Llamamos a la función que llenara la lista
strings(words_list)
#Llamamos a la función que contara las ocurrencias
occurrences = count_occurrences(words_list)

#mostramos todas las ocurrencias encontradas con sus claves, sus claves son la cantidad de veces que aparecen
print("Ocurrencias de caracteres en todas las palabras ingresadas:")
for char, count in occurrences.items():
    print(f"'{char}': {count}")

print("_____________________________________________________________________")
#Ejercicio_8
#Diez equipos de la liga inter-barrial identificados con los números 1, 2, 3, 4, …, 10, participaron en un campeonato de fútbol con modalidad todos contra todos.
#Los goles anotados en cada encuentro se registraron en el siguiente cuadro:
#Escriba un programa que:
#	Lea el cuadro de goles en un arreglo de dos dimensiones.
#	Muestre para cada equipo la cantidad de triunfos, empates y derrotas.
#	Muestre la diferencia entre el total de goles marcados y el total de goles recibidos.
#	Determine la cantidad de puntos obtenidos por cada equipo.

#Este cuadro, representa los equipos y sus goles
#Las filas representa un equipo y las columnas el equipo contra el jugo Ej: en la fila 1 columna 2 el equipo 1 convirtio
# 2 goles al equipo 2 y el equipo 2 le convirtio 5 goles al equipo 1 entonces el equipo 2 gano ese partido

goals = [
#   1--2--3--4--5--6--7--8--9--10  
    [0, 4, 2, 1, 5, 3, 2, 3, 3, 5],  #1
    [5, 0, 3, 2, 2, 1, 1, 0, 0, 1],  #2
    [0, 0, 0, 3, 5, 5, 2, 3, 0, 3],  #3
    [1, 0, 2, 0, 1, 0, 3, 1, 0, 1],  #4
    [2, 4, 1, 0, 0, 2, 1, 0, 2, 0],  #5
    [0, 0, 0, 5, 3, 0, 2, 1, 1, 1],  #6
    [1, 2, 0, 1, 1, 2, 0, 1, 2, 0],  #7
    [0, 3, 0, 1, 2, 1, 2, 0, 2, 1],  #8
    [2, 0, 1, 1, 0, 2, 1, 1, 0, 1],  #9
    [0, 0, 1, 1, 2, 0, 1, 1, 0, 0]   #10
]

# Crear listas para almacenar los resultados de cada equipo
club = [i for i in range(1, 11)]
triumphs = [0] * 10
ties = [0] * 10
defeats = [0] * 10
goals_scored = [0] * 10
goals_received = [0] * 10
points = [0] * 10

# Calcular los resultados para cada equipo
for i in range(10):
    for j in range(10):
        if i != j:
            if goals[i][j] > goals[j][i]:
                triumphs[i] += 1
                points[i] += 3
            elif goals[i][j] < goals[j][i]:
                defeats[i] += 1
            else:
                ties[i] += 1
                points[i] += 1
            goals_scored[i] += goals[i][j]
            goals_received[i] += goals[j][i]

# Mostrar los resultados para cada equipo
for i in range(10):
    print(f"Equipo {club[i]} - Triunfos: {triumphs[i]}, Empates: {ties[i]}, Derrotas: {defeats[i]}")
    print(f"Goles Marcados: {goals_scored[i]}, Goles Recibidos: {goals_received[i]}")
    print(f"Puntos: {points[i]}\n")
print("_____________________________________________________________________")

#Ejercicio_9
#Escribir un programa que simule el juego clásico de Memoria (Memotest) 
#utilizando matrices. El juego consiste en un tablero de cartas boca abajo y el objetivo es 
# encontrar todas las parejas de cartas iguales.

if __name__ == "__main__":
    play_memory()

print("_____________________________________________________________________")


#Ejercicio_10


# Ejemplo de uso:
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
#Llamamos a la función para obtener las matrices
main_diagonal, reverse_diagonal = get_diagonals(matriz)

print("Diagonal Principal:", main_diagonal)
print("Diagonal Inversa:", reverse_diagonal)

print("_____________________________________________________________________")

#Ejercicio_11
#Escribir un programa que guarde en una variable el diccionario {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}, 
#pregunte al usuario por una divisa y muestre su símbolo o un mensaje de aviso si la divisa no está en el diccionario.

#Creamos un diccionario con las claves Euro, Dollar y Yen
money={
    "Euro":"€",
    "Dollar":"$",
    "Yen":"¥"
}

#Pedimos las divisas que desea ver al usuario
badge=input("Que divisa desea visualizar?: ")
badge=badge.capitalize()

#Verificamos si la moneda que ingresamos se encuentra en el diccionario
if badge in money:
    simbol = money[badge] #Si se encuentra en el diccionario, obtenemos la divisa correspondiente
    print(f"{simbol} es el simbolo de {badge}")
else:
    print(f"{badge} no se encuentra en el diccionario") #Si la moneda ingresada no se encuentra en el diccionario mostraremos el siguiente mensaje

print("_____________________________________________________________________")

#Ejercicio_12
#Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono y lo guarde en un diccionario. 
#Después debe mostrar por pantalla el mensaje ‘<nombre> tiene <edad> años, vive en <dirección> y su número de 
#teléfono es <teléfono>’.

#Pedimos al usuario que ingrese su nombre, edad, direccion y num de telefono
name=input("Ingrese su nombre: ")
age=input("Ingrese su edad: ")
addres = input("Ingrese su dirección: ")
contact_num =input("Ingrese su número de telefono: ")

#Guardamos en un diccionario las variables que ingresamos con sus claves
info_usuary={
    "nombre":name,
    "edad":age,
    "dirección":addres,
    "telefono":contact_num
}
#imprimimos cada uno de los elementos del diccionario con el siguien mensaje
print(f"{info_usuary['nombre']} tiene {info_usuary['edad']} años, vive en {info_usuary['dirección']} y su número de teléfono es {info_usuary['telefono']}")

print("_____________________________________________________________________")

#Ejercicio_13
#Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla, pregunte al 
#usuario por una fruta, un número de kilos y muestre por pantalla el precio de ese número de kilos de fruta. 
#Si la fruta no está en el diccionario debe mostrar un mensaje informando de ello.

print("|---------------------------|")
print("|naranja 20$ por 100gr      |")
print("|manzana:20, por 100gr      |")
print("|frutillas 50$ por 100gr    |")
print("|kiwi 60$ por 100gr         |")
print("|durazno 10$ por 100gr      |")
print("|---------------------------|")

#Creamos un diccionario con las frutas que tenemos y sus precios en gramos(100gr)
fruit_dictionary={
    "naranja":20,
    "manzana":20,
    "frutillas":50,
    "kiwi":60,
    "durazno":10
}

#Le pedimos al usuario la fruta que desea llevar y la cantidad de kg 
fruit = input("Ingrese la fruta que llevara: ")
kg= int(input("Ingrese los kilos que llevara: "))
fruit = fruit.lower()

#Verificamos que la fruta se encuentre en el diccionario
if fruit in fruit_dictionary:
    #Si la fruta se encuentra en el diccionario realizamos una suma (la cantidad de kg lo multiplicamos por el precio de fruta en gramos)
    buy=kg*(fruit_dictionary[fruit]*10)
    #Mostramos la fruta que lleva y el valor 
    print(f"{kg} kg de {fruit} son {buy}$")
else:
    #Si la fruta no se encuentra en el diccionario el programa mostrara el siguiente mensaje
    print(f"No tenemos {fruit}")