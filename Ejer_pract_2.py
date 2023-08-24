"""                         Trabajo Práctico 1.2        """

#Ejercicio_1
b = float(input("Ingrese la base del rectángulo: "))
h = float(input("Ingrese la altura del rectángulo: "))
perimetro = 2*(b+h)
print("El perímetro del rectángulo es de: " ,perimetro)

#Ejercicio_2
cateto_1 = float(input("Ingrese el valor del cateto 1: "))
cateto_2 = float(input("Ingrese el valor del cateto 2: "))
h = (cateto_1 ** 2) + (cateto_2 ** 2)
hipotenusa = h**0.5
print("El valor de la hipotenusa es: " ,hipotenusa) 

#Ejercicio_3
n_1 = float(input("Ingrese el primer número: "))
n_2 = float(input("Ingrese el segundo número: "))
suma = n_1 + n_2
resta = n_1 - n_2 
mult = n_1 * n_2 
div = n_1 / n_2  
print(n_1, " + " ,n_2, " = " ,suma )
print(n_1, " - " ,n_2, " = " ,resta )
print(n_1, " * " ,n_2, " = " ,mult )
print(n_1, " / " ,n_2, " = " ,div )

#Ejercicio_4
f = float(input("Ingrese los grados farenheit: "))
c = (f-32) * 5/9
print(f, " farenheit son " ,c, " grados celsius" ) 

#Ejercicio_5
#   A)  a = input(nombre, “¿Cuál es tu canción favorita? ”)
#El problema es que se quizo usar la variable "nombre" dentro del input() pero este solo admite texto de salida
#para mostrar el contenido de una variable se puede usar un print() previamente de la siguiente forma:
nombre = "Rodrigo"
print(nombre, "¿Cual es tu canción favorita?")
a = input()

# B) precio = input(“Precio: “)
#    total = precio + (precio * 0.1)

# En este ejemplo, "precio" esta gadando una cadena de texto y luego se esta queriendo multiplicar
# lo correcto seria lo siguiente:

precio = float(input("Precio: "))
total = precio + (precio*0.1)
print(total)

# C) edad = int(input(“Edad: “))
#    print(tu edad es, edad)

# El problema es que al devolver un texto no se usaron comillas.
# Lo correcto sería hacerlo así:

edad= int(input("Edad: "))
print("tu edad es " ,edad)

# D) edad = int(input(“Edad: “))
#    print(“Veamos si tu edad es 18…”, edad=18)

# El problema del ejemplo es que se estaba asignando el valor "18" a una variable dentro de un print()
# lo correcto, para comprobar si "edad" es igual a "18", sería lo sig:

edad = int(input("Edad: "))
print("Veamos si tu edad es 18...")


#Ejercicio_6
num_1 = float(input("Ingrese el primer número a promediar: "))
num_2 = float(input("Inrese el segundo número a promediar: "))
num_3 = float(input("Inrese el tercer número a promediar: "))
promedio = (num_1 + num_2 + num_3)/3
print("El promedio de los tres números ingresados es: " ,promedio)

#Ejercicio_7
minutos = float(input("Ingrese los minutos: "))
horas = int (minutos/60)
horas_1 = minutos % 60
print (minutos, " minutos son: " ,horas, "hs y " ,horas_1, " minutos")

#Ejercicio_8
sueldo_base = 5000
comision = .10
total = sueldo_base+sueldo_base *(comision * 3)
print("El sueldo a fin de mes sera $",total)

#Ejercicio_9
precio = float(input("Ingrese el precio del producto: "))
descuento = precio*0.15
precio_final = precio-descuento
print("El precio final del producto es de $",precio_final)

#Ejercicio_10
p_1 = 70
p_2 = 80
p_3 = 50
prom_parc = (p_1+p_2+p_3)/3
e_f = 80
t_f = 50
nota_final = (prom_parc * 0.55) + (e_f * 0.30) + (t_f * 0.15)
print("Su nota final es " ,nota_final)

#Ejercicio_11
valor_ini = float(input("Ingrese el valor inicial:"))
valor_final = float(input("Ingrese el valor final: "))
distancia = (valor_final - valor_ini)
print("La distancia entre " ,valor_ini, " y " ,valor_final, " es " ,distancia)

#Ejercicio_12
num = int(input("Ingrese un número: "))
raiz_cua = (num ** 0.5)
raiz_cub = num ** (1/3)
print("La raíz cuadrada de " ,num, " es " ,raiz_cua, " y la raíz cubíca es " ,raiz_cub)

#Ejercicio_13
num_1 = int(input("ingrese el primer número: "))
num_2 = int(input("ingrese el segundo número: "))
lista = [num_1, num_2]
lista.reverse()
print(lista)

#Ejercicio_14
a = input("Ingrese el valor de A: ")
b = input("Ingrese el valor de B: ")
c = a
a = b
b = c
print("El valor de A: " ,a)
print("El valor de B: " ,b)

#Ejercicio_15
hh = 15
mm = 30
ss = 0
t = 1800

ss = ss+t
if ss> 59:
    mm = mm + ss/60
    ss = 0

if mm > 59:
    hh = hh + mm/60
    mm = 0

if hh > 24:
    hh = 0

print("La hora de llegada a la ciudad B sera a las " , hh, ":" ,mm, ":" ,ss)

#Ejercicio_16
nombre = "Pedro"
apellido = "Rodriguez"
print (nombre[0])
print (apellido[0])

#Ejercicio_17
usuario = input("Ingrese su nombre: ")
print("Ahora esta en la Matrix " ,usuario)

#Ejercicio_18
costo_cen = float(input("Ingrese el costo: "))
costo_cen += costo_cen * 0.062
costo_cen += costo_cen *0.10
print(f"EL costo final, incluyendo servicios y propinas es ${costo_cen}")

#Ejercicio_19
print("Bienvenido-Ingrese los siguientes datos dd/mm/aaaa")
dia = int(input("Ingrese el día de su nacimiento: "))
mes = int(input("Ingrese el mes de nacimiento: "))
año = int(input("Ingrese el año de nacimiento: "))
print(f"Fecha de nacimiento {dia}/{mes}/{año}")

#Ejercicio_20
fecha =[int(input("Día de nacimiento: ")), int(input("Mes de nacimiento: ")), int(input("Año de nacimiento: "))] 
print(fecha)

#Ejercicio_21
km_lit =float(input("Ingrese los km que puede recorrer con un litro de combustible: "))
cap_tanq = float(input("Ingrese la capacidad, en litros, del tanque: "))
km_reco = float(input("Ingrese los km que recorrerán: "))
km_tanq = (km_lit * cap_tanq)
tanq_total = (km_reco/km_tanq).__trunc__()

print("Usará " ,tanq_total, " tanques para recorrer " ,km_reco, "km")
