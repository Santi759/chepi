import math

def num_dni(dni):
    num = len(dni)
    if num == 7 or num == 8:
        return True
    else:
        return False

def long_word(phrase):
    space = phrase.strip()
    word = space.split()
    if len(word) > 0:
        return len(word[-1])
    else:
        return 0
    
def carnet_id(name,dni):
    carnet = name.split()
    dig1 = dni[0]
    dig2 = dni[1]
    dig3 = dni[2]
    if len(carnet) == 3:
        name_1 = carnet[0]
        name_2 = carnet[1]
        last_name = carnet[2]
        long = len(last_name)
        print(f"Nombre--> {name_1} {name_2} {last_name}")
        print(f"DNI--> {dni}")
        print(f"ID--> {name_1}{long}{dig1}{dig2}{dig3}")
        return id
    else:
        name_1 = carnet[0]
        last_name = carnet[1]
        long = len(last_name)
        print(f"Nombre--> {name_1} {last_name}")
        print(f"DNI--> {dni}")
        print(f"ID--> {name_1}{long}{dig1}{dig2}{dig3}")
        return 
    
def multiple(num_1,num_2):
    if num_1 % num_2==0:
        return print(f"{num_1} es multiplo de {num_2}")
    else:
        return print(f"{num_1} no es multiplo de {num_2}")
    
def medium_temperature(maximum_temperature,minimum_temperature):
    medium = (maximum_temperature+minimum_temperature)/2
    return medium

def space(word):
    separate_word = " ".join(word)
    return separate_word

def num_may_min(list_num):
    bigger_num= max(list_num)
    minor_num = min(list_num)
    return print(f"{bigger_num} es el número mayor y {minor_num} es el menor de la lista")

def area_perimeter(radio):
    pi= math.pi
    area = pi*(radio**2)
    perimeter = 2*(pi)*radio
    return print(f"El área de la circunferencia = {area} y el perimetro = {perimeter}")

def login(user_name, password, attempts):
    while attempts !=0:
        if (user_name == "usuario1" and password == "asdasd"):
            return True
        else:
            attempts -=1
            print(f"Incorrecto. Intente una vez más. Intentos restantes {attempts+1}")
            user_name = input("Usuario: ")
            password = input("Contraseña: ")
    return print("Acceso Denegado")

def aplicar_descuento(trolley, discounts):
    total = 0
    
    for discount, price in trolley.items():
        if discount in discounts:
            discount = discounts[discount]
            price_with_discount = price - (price * discount / 100)
            total += price_with_discount
        else:
            total += price
    
    return total

def fold(num):
    return 2 * num

def function(fold, nums):
    result=[]
    for i in nums:
        result.append(fold(i))
    return result

def count_word_length(phrase):
    words = phrase.split()
    dictionary = {}
    for word in words:
        dictionary[word] = len(word)
    return dictionary

def vector_module(vector):
    sum_squares = sum([component ** 2 for component in vector])
    module = math.sqrt(sum_squares)
    return module

def num_pri(num):
    if num == 2 or num == 3:
        return True
    elif num %2==0 or num %3==0:
        return False
    else:
        return True
    
def factorial (n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
    
def main():
    total_numbers = 0
    
    while True:
        try:
            number = int(input("Ingrese un número (un número negativo si desea salir): "))
        except ValueError:
            print("Por favor ingrese un valor válido")
            continue
        
        if number < 0:
            break
        
        total_numbers += 1 
        result = factorial(number)
        print(f"El facotrial de {number} es: {result}")
    
    print(f"Se ingresaron un total de {total_numbers} ")

def count_occurrences(num, dig):
    number_str = str(num)
    counter = 0
    for d in number_str:
        if d == str(dig):
            counter += 1
    return counter

def sum_dig(num):
    suma = 0
    while num>0:
        digito = num%10
        suma +=digito
        num = num//10
    return suma

def big_num(num):
    bigger_number=0
    if num>bigger_number:
        bigger_number=num
    return bigger_number

def factorial_1 (bigger):
    return bigger * factorial(bigger-1)

