#Ejercicio_1

abc = "abcdefghijklmnñopqrstuvwxyz"
corrimiento = int(input("De cuanto sera el corrimiento de las letras: "))

for i in range(5):
    msj = input("Ingrese el mensaje: ")
    msj_encriptado = " "
    for letra in msj:
        if letra in abc:
            indice = abc.find(letra)
            indice = (indice+corrimiento)%26
            msj_encriptado += abc[indice]
        else:
            msj_encriptado += letra
    print(f"El msj encriptado es: {msj_encriptado}")

#Ejercicio_2
#Crear un programa que solicite el ingreso de números enteros positivos, hasta que el usuario ingrese el
#0. Por cada número, informar cuántos dígitos pares y cuántos impares tiene.
#Al finalizar, informar la cantidad de dígitos pares y de dígitos impares leídos en total

pares= 0
num = int(input("Ingrese un número entero positivo: "))
while num !=0:
    if num%2 == 0:
        pares+=1
    suma=0
    while num !=0:
        digito=num%10
        suma+=digito
        num=num//10
    print("Suma de sus dígitos:", suma)
    num=int(input("Ingrese un número entero positivo o 0 para terminar el programa: "))

print("Se ingresaron", pares, "números pares")