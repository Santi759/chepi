import random

def rat_escape(current_time=0):
    #En la variable choice guardaremos la opción que elige la rata. La opción se elige aleatoriamente con la función
    #random, elige entre 1 y 3
    choice=random.randint(1,3)
    
    #Si la opción fue 1 sumaremos 3 minutos a la variable current_time
    # La función vuelve a llamarse a si misma para ver que camino elegira la rata 
    if choice==1:
        print("Camino 1")
        return rat_escape(current_time+3)
    
    #Si la opción fue 2 sumaremos 5 minutos a la variable current_time
    # La función vuelve a llamarse a si misma para ver que camino elegira la rata 
    elif choice==2:
        print("Camino 2")
        return rat_escape(current_time+5)
    
    #Si la opción fue 3 sumaremos 7 minutos a la variable current_time
    #Esta vez la rata logra escapar y la función nos devuelve la cantidad de minutos que tardo la rata en escapar
    elif choice==3:
        print("Camino 3")
        return current_time+7
    

print(f"La rata tardo {rat_escape()} min en salir")
    
