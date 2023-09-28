#Importamos las funciones random y funciones(creada por nosotros)
import random, funciones

#Creamos una lista con palabras referidas a la prog. Estás palabras será elegida al azar por el programa
list =["python","java","html","funciones","codigos"]

#Creamos una variable con la cantidad de intentos
att=6

#Esto retornara la variable en las dos funciones(creada para que no retornara un valor none)
j=""

#creamos una variable donde guardaremos la palabra que eligio el programa
ran = random.choice(list)

#en space guardaremos la cantidad de espacios que tiene la palabra elegida
space = len(ran)


print("<<<Bienvenido a AHORCADOS>>>")
print("")

#inovocamos nuestra primer función, llamada draw, se trata de un dibujo para darle una animación al programa
print(funciones.draw(j))
print("")

#La segunda función, contiene nuestro codigo del juego
print(funciones.cycles(space,att,ran,j))
