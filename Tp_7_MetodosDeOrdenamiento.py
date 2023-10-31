def bubble_sort(nums):
    n=len(nums)
    aux=0
    if n==1:
        return nums
    for i in range(n-1):
        for j in range(n-1-i):
            if nums[j]>nums[j+1]:
                aux=nums[j]
                nums[j]= nums[j+1]
                nums[j+1]=aux
    return nums

def selection_sort(list_words):
    n=len(list_words)
    for i in range(n-1):
        min = list_words[i]
        position=i
        for j in range(i+1,n):
            if (list_words[j]<min):
                min= list_words[j]
                position=j
        if (position != i):
            aux= list_words[i]
            list_words[i]=list_words[position]
            list_words[position]=aux
    return list_words

def bubble_sort_books(list_dic,field):
    n=len(list_dic)
    aux=0
    if n==1:
        return nums
    for i in range(n-1):
        for j in range(n-1-i):
            if list_dic[j][field] > list_dic[j+1][field]:
                list_dic[j], list_dic[j+1] = list_dic[j+1], list_dic[j]
    return list_dic

def insert_sort(list_cad):
    for i in range(1,len(list_cad)):
        position=list_cad[i]
        j=i-1
        while j>=0 and len(position)<len(list_cad[j]):
            list_cad[j+1]=list_cad[j]
            j -=1
            list_cad[j+1]=position
    return list_cad

def count_sort(list_count):
    max_value= max(list_count)
    count = [0]*(max_value+1)
    for num in list_count:
        count[num] +=1
    
    sorted_list_count=[]
    for i in range(max_value+1):
        sorted_list_count.extend([i]*count[i])
    return sorted_list_count

def merge_sort(list_mer):
    if len(list_mer)==1:
        return list_mer
    
    middle=len(list_mer)//2
    left_array = list_mer[:middle]
    right_array= list_mer[middle:]
    sorted_left_array = merge_sort(left_array)
    sorted_right_array = merge_sort(right_array)
    return merge(sorted_left_array, sorted_right_array)

def merge(left_array, right_array):
    array_result=[]
    while len(left_array)>0 and len(right_array)>0:
        if left_array[0]>right_array[0]:
            array_result.append(right_array[0])
            right_array.pop(0)
        else:
            array_result.append(left_array[0])
            left_array.pop(0)
    while len(left_array)>0:
        array_result.append(left_array[0])
        left_array.pop(0)
    
    while len(right_array)>0:
        array_result.append(right_array[0])
        right_array.pop(0)
    return array_result
#Ejercicio_1
#Creamos una lista desordenada
nums=[9,3,5,1,6]

print("Ordenamiento burbuja")
print(f"Arreglo desordenado: {nums}")
#Llamamos a la funcion que nos devuelve la lista ordenada mediante el metodo burbuja
print(f"Arreglo ordenado: {bubble_sort(nums)}")
print("______________________________________")
#Ejercicio_2
#Creamos una lista con palabras 
list_words=["hola","sol","zapato","abeja","messi"]
print(f"Arreglo desordenado: {list_words}")
#Llamamos a la funcion que nos ordena las palabras alfabeticamente mediante el metodo de seleccion
print(f"Arreglo ordenado: {selection_sort(list_words)}")
print("______________________________________")
#Ejercicio_3

#Creamos una lista de diccionario con diferentes libros
list_dic =[
    {
        "titulo":"Harry Potter y la piedra filosofal",
        "autor":"J.K.Rowling",
        "año_publicacion":1997
        },
    {
        "titulo":"Fuego y Sangre",
        "autor":"George R. Martin",
        "año_publicacion":2018
        },
    {
        "titulo":"Sherlock Holmes estudio en escarlata"
        ,"autor":"Arthur Doyle",
        "año_publicacion":1887
        }
    ]
#Ordenamos la lista de libros con el metodo burbuja y usamos su año de publicación para ordenarlo
books=bubble_sort_books(list_dic,field="año_publicacion")
print(f"Libros ordenados por fecha de publicación: {books}")
print("______________________________________")
#Ejercicio_4
#Escribe un programa que tome una lista de cadenas como entrada y las ordene en orden ascendente 
#según su longitud. Puedes utilizar el método de ordenamiento de inserción.

list_cad=["mundo","argentina","luna","programación","sol"]
print(f"Lista ordenada{insert_sort(list_cad)}")
print("______________________________________")
#Ejercicio_5
#Modifica uno de los ejercicios anteriores para ordenar la lista de números en 
#orden descendente en lugar de ascendente.
desc=bubble_sort(nums)
for i in reversed(desc):
    print(i)
print("______________________________________")
#Ejercicio_6
#Escribe un programa que tome una lista de números enteros y ordene la lista utilizando el algoritmo de 
#ordenamiento por conteo.

list_count=[9,12,152,4,9,5,12,4]
print(count_sort(list_count))
print("______________________________________")
#Ejercicio_7
num_words=["5","hola","9","futbol","3","araña"]
ord = selection_sort(num_words)
print(ord)
print("______________________________________")
#Ejercicio_8
list_merge=[152,-152,3,0,95,5,2.5,1]
array_ordered = merge_sort(list_merge)
print(array_ordered)
