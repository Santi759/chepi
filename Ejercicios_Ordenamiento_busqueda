def bubble_sort(nums,aux):
    n=len(nums)
    for i in range(n-1):
        for j in range(n-1-i):
            if nums[j]>nums[j+1]:
                aux=nums[j]
                nums[j]= nums[j+1]
                nums[j+1]=aux
    return nums

def selection_sort(list_sel):
    #12,5,15,8,52,4,-2
    n=len(list_sel)
    for i in range(n-1):
        min = list_sel[i]
        position=i
        for j in range(i+1,n):
            if (list_sel[j]<min):
                min= list_sel[j]
                position=j
        if (position != i):
            aux= list_sel[i]
            list_sel[i]=list_sel[position]
            list_sel[position]=aux
    return list_sel

def insert_sort(list_ins):
    for i in range(len(list_ins)):
        position=i
        aux=list_ins[i]
        while ((position>0) and (list_ins[position-1]>aux)):
            list_ins[position]=list_ins[position-1]
            position -=1
        list_ins[position]=aux
    return list_ins

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

def linear(list_search,x):
    for ix, i in enumerate(list_search):
        if i == x:
            return ix
    return -1

def binary(list_search,low,high,x):
    if high >= low:
        mid = (high+low)//2
        if list_search[mid]==x:
            return mid
        elif list_search[mid]>x:
            return binary(list_search,low,mid-1,x)
        else:
            return binary(list_search,mid-1,high,x)
    else:
        return -1
        

#Ordenamiento burbuja (Bubble Sort)
nums=[9,3,5,1,6]
aux=0
print("Ordenamiento burbuja")
print(f"Arreglo desordenado: {nums}")
print(f"Arreglo ordenado: {bubble_sort(nums,aux)}")
print("______________________________________")
#Ordenamiento por Selección (Selection Sort)
list_sel=[12,5,15,8,52,4,-2]
print("Ordenamiento por selección ")
print(f"Arreglo desordenado: {list_sel}")
print(f"Arreglo ordenado: {selection_sort(list_sel)}")
print("______________________________________")
#Ordenamiento por Inserción (Insert Sort)
list_ins=[5,-5,26,1,-1250,10,46]
print("Ordenamiento por inserción ")
print(f"Arreglo desordenado: {list_ins}")
print(f"Arreglo ordenado: {insert_sort(list_ins)}")
print("______________________________________")
#Combinar ordenamiento (Merge Sort)
list_mer=[8,7,5,3,-5]
print("Ordenamiento por Mezcla ")
print(f"Arreglo desordenado: {list_mer}")
sort_merge = merge_sort(list_mer)
print(f"Arreglo ordenado: {sort_merge}")
print("______________________________________")
#Busqueda Linear
list_search=[10,50,-6,25,34,7,5]
x=int(input("Qué número desea encontrar: "))
print(f"El número {x} se encuentra en la posición {linear(list_search,x)}")
print("______________________________________")
#Busqueda Binaria
x=int(input("Qué número desea encontrar: "))
print(f"El número {x} se encuentra en la posición {binary(list_search,0,len(list_search)-1,x)}")
print("______________________________________")
