def number_digits(n):
    if n<10:
        return 1
    else:
        return 1 + number_digits(n//10)
    
def powers(n,b):
    if n==1:
        return True
    if n<b:
        return False
    
    return powers(n/b,b)

def search_string(a,b,start=0):
    index=a.find(b,start)
    if index==-1:
        return []
    return [index] + search_string(a,b,index+1)

def pair(n):
    if n == 0:
        return True
    else:
        return odd(n - 1)

def odd(n):
    if n == 0:
        return False
    else:
        return pair(n - 1)

def search_elderly(lst, index=0, max_val=None):
    if index == 0:
        max_val = lst[index] 

    if index < len(lst):
        if lst[index] > max_val:
            max_val = lst[index]
        return search_elderly(lst, index + 1, max_val)  
    else:
        return max_val if max_val is not None else None 
    
def replicate_element(lst,n):
    if n<=1:
        return lst
    return replicate_element([elemento for elemento in lst for _ in range(n)],1)

def summation(n,p):
    if n==1:
        return p
    return n*p + summation(n-1,p)

def pascal(n, k):
    if k == 0 or k == n:
        return 1
    else:
        return pascal(n - 1, k - 1) + pascal(n - 1, k)

def combinations(list_char, k, combination=""):
    if k == 0:
        print(combination)
        return
    for char in list_char:
        combinations(list_char, k - 1, combination + char)

def measured_sheets_A(n):
    if n == 0:
        # Caso base: A0
        return (841, 1189)
    else:
        # Llamada recursiva para calcular A(N) a partir de A(N-1)
        previous_width, previous_length = measured_sheets_A(n - 1)
        new_width = previous_length // 2
        new_long = previous_width
        return (new_width, new_long)






