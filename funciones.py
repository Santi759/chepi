#Esta función solo muestra el dibujo creado
def draw(j):
    s=j
    print("|___________")
    print("|           |")
    print("|           O")
    print("|          <|>")
    print("|          / \ ")
    return s


def cycles(space,att,ran,j):
    #en la variable bar guardamos la cantidad de guiones segun la cantidad de letras que tiene la palabra seleccionada
    bar = ["_"] * space
    print(" ".join(bar))
    s=j
    #Creamos un ciclo while donde tendra 6 intentos, si no acierta la letra se restaran los intentos
    while att >0:

        #le pedimos al usuario que ingrese un caracter
        char=input("Ingrese una letra: ").lower()

        #evaluamos que sea un caracter válido
        if not char.isalpha():
            print("Por favor, ingrese una letra válida.")
            continue

        #evaluamos si el caracter se encuentra en la palabra
        if char in ran:
            #si el caracter se encuentra en la palabra, el siguiente ciclo for buscara la posición del caracter
            for i in range(len(ran)):
                #cuando encuentre la posicion del caracter, cambiara el guion por la letra
                if ran[i] == char:
                    bar[i] =char
            print("Correcto")
            print(" ".join(bar))
        #si el caracter ingresado no se encuentra en la palabra, el programa restara un intento    
        else:
            att -=1
            print(f"Le quedan {att} intentos ")

        #el programa evalua si ingresamos todos los caracteres y si es igual a la palabra seleccionada, si es igual el programa terminara    
        if "".join(bar) == ran:
            print(f"¡Ganaste! La palabra es: |{ran}|")
            print("<<<|FIN DEL JUEGO :D |>>>")
            break
    #una vez terminado los intentos el programa evalua que la palabra ingresada y la seleccionada por el programa sean diferentes y no muestra el siguiente mensaje
    if "".join(bar) != ran:
        print("|___________")
        print("|           |")
        print("|           O")
        print("|          <|>")
        print("|          / \ ")
        print(f"La palabra era |{ran}| ")
        print("<<<|FIN DEL JUEGO :( |>>>)")
    return s
