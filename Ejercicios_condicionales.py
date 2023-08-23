print("¡Bienvenido al Sistema!")
print("Ingrese la fecha que quiere saber formato: [día, DD/MM]: ")
fecha = input("día, DD/MM")
dia_sem = fecha[0:fecha.find(",")]
dia = int(fecha[fecha.find(" ")+1: fecha.find("/")])
mes = int(fecha[fecha.find("/")+1:])

if (dia_sem.capitalize() == "Lunes" and dia <= 31 and mes <= 12):
    print(fecha, " Nivel Inicial")
    respuesta = input("¿Hubo examén? (S/N)")
    respuesta = respuesta.lower()
    if (respuesta == "s"):
        aprob = int(input("Ingrese la cantidad de alumnos que aprobaron: "))
        desaprob = int(input("Ingrese la cantidad de alumnos desaprobados: "))
        porc = aprob/(aprob+desaprob) * 100 
        porc = porc.__trunc__()
        print("El porcentaje de alumnos aprobados fue del " ,porc, "%")
elif (dia_sem.capitalize() ==  "Martes" and dia <= 31 and mes <= 12):
    print(fecha, " Nivel Intermedio")    
    respuesta = input("¿Hubo examén? (S/N)")
    respuesta = respuesta.lower()
    if (respuesta == "s"):
        aprob = int(input("Ingrese la cantidad de alumnos que aprobaron: "))
        desaprob = int(input("Ingrese la cantidad de alumnos desaprobados: "))
        porc = aprob/(aprob+desaprob) * 100 
        porc = porc.__trunc__()
        print("El porcentaje de alumnos aprobados fue del " ,porc, "%")
elif (dia_sem.capitalize() == "Miercoles" and dia <= 31 and mes <= 12):
    print(fecha, " Nivel Avanzado")
    respuesta = input("¿Hubo examén? (S/N)")
    respuesta = respuesta.lower()
    if (respuesta == "s"):
        aprob = int(input("Ingrese la cantidad de alumnos que aprobaron: "))
        desaprob = int(input("Ingrese la cantidad de alumnos desaprobados: "))
        porc = aprob/(aprob+desaprob) * 100 
        porc = porc.__trunc__()
        print("El porcentaje de alumnos aprobados fue del " ,porc, "%")
elif (dia_sem.capitalize() == "Jueves" and dia <= 31 and mes <= 12):
    print(fecha, " Practicas Habladas")
    asist = int(input("Ingrese el porcentaje de alumnos que asistieron:"))
    if (asist >= 50):
        print("Asistio la mayoría" ,asist, "%")
    else:
        print("No asistio la mayoría" ,asist, "%")
elif (dia_sem.capitalize() == "Viernes" and dia <= 31 and mes <= 12):
    print(fecha, " Inglés para Viajeros")
    if (dia == 1 and mes == 1 or mes == 7):
        print("¡Comienzo de nuevo ciclo!")
        alumn_nuevos = int(input("Ingrese la cantidad de alumnos nuevos: "))
        arancel = int(input("Ingrese el arancel por cada alumno:"))
        total = alumn_nuevos * arancel
        print("El ingreso total: $" , total)
else:
    print("Error, fecha ingresada invalida")
    exit()
