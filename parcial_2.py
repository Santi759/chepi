
#Creamos una función para llenar nuestra matriz
def matrix_mutants(dna):
    #Creamos un ciclo donde llenaremos las filas y columnas
    for i in range(6):
        row = input(f"Ingrese la fila {i+1}. Debe contener 6 caracteres (ATCG) ").upper()
        #Comprobamos que la fila contenga 6 elemtos y sean ATCG
        if len(row)!=6 or any(char not in 'ATCG' for char in row):
            print("La fila solo puede contener 6 carácteres")
            print("La fila de carácteres ingresada solo puede contener valores (ATCG) ")
            #En caso de no ser cierta la condición anterior, creamos un bucle while, su condición de salida es que 
            #la fila contenga 6 elementos y sean ATCG
            while len(row)!=6 or any(char not in 'ATCG' for char in row)==True:
                row = input(f"Ingrese la fila {i+1}. Debe contener 6 caracteres (ATCG) ").upper()
        #Cuando verificamos que lo ingresado sea lo correcto, agregramos la fila a la matriz
        dna.append(row)
    return dna


#En esta función verificamos si el sujeto es mutante o no
def is_mutant(dna):
    #Esta lista de tuplas sera las maneras en las que buscaremos las secuencias de ADN (vertical, horizontal o diagonal)
    #El primer valor representa la fila y el segundo la columna
    directions= [(1,0),(0,1),(1,1),(-1,1)]
    #Con este bucle anidado recorreremos la matriz
    #Con este bucle recorremos las filas
    for i in range(len(dna)):
            #Este bucle recorremos las columnas
            for j in range(len(dna)):
                #Con este bucle recorremos las direcciones de los caracteres
                for dx, dy in directions:
                    count=0
                    x=i
                    y=j
                    #Este bucle while lo usamos para verificar que coordenada x y y se encuentren dentro de los 
                    #limites de la matriz y comparar los valores en las diferentes direcciones y asi poder contar
                    #si hay concidencias en la secuencia de ADN
                    while 0 <= x < len(dna) and 0 <= y < len(dna[x]) and dna[x][y] == dna[i][j]:
                        count += 1
                        x, y = x + dx, y + dy
                    
                    #Si contador es mayor o igual a 4 (Se encontraron 4 o más caracteres iguales en las diferentes direcciones)
                    #la función nos retornara True
                    if count >=4:
                        return True
    #En caso de no encontrar coincidencias la función nos retorna un False
    return False


#Creamos una lista vacía que sera con la que trabajamos
dna=[]

#Llamamos a la función que llenara nuestra matriz
dni_mutant = matrix_mutants(dna)
#Guardamos en una variable el resultado de la función is_mutant, que sirvio para comprobar el ADN
check_mutant= is_mutant(dna)


print(" ")
print("-----------------------------")
print("     <<<ADN MUTANTES>>>     ")
print("-----------------------------")
#Utilizamos un ciclo para mostrar la matriz ingresadda
for i in range(len(dni_mutant)):
    for j in range(len(dni_mutant[i])):
        print(dni_mutant[i][j],end=" ")
    print(" ")
print("-----------------------------")

#Si la función nos devuelve True, nos mostrara el siguien mensaje
if check_mutant:
    print("Se encontro ADN mutante")
else:
    print("No hay ADN mutante")


