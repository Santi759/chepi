#Ejercicio_1
#Escribir un programa que permita procesar datos de pasajeros de viaje en una lista de tuplas con la siguiente
#forma: (nombre, dni, destino). Por ejemplo:
#[(‘Manuel Juarez’, 12345678, ‘San Juan’), (‘Silvana Paredes’, 62258472, ‘Mendoza’)]
#Además en otra lista de tuplas se almacenan los datos de cada ciudad y el país al que pertenecen. Ejemplo:
#[(‘Buenos Aires’, ‘Argentina’), (‘Lisboa’, ‘Portugal’), (‘Mendoza’, ‘Argentina’)]
#Hacer un menú iterativo que permita al usuario realizar las siguientes operaciones:
#- Agregar pasajeros a la lista de viajeros.
#- Agregar ciudades a la lista de ciudades.
#- Dado el DNI de un pasajero, ver a qué ciudad viaja.
#- Dada una ciudad, mostrar la cantidad de pasajeros que viajan a esa ciudad.
#- Dado el DNI de un pasajero, ver a qué país viaja.
#- Dado un país, mostrar cuántos pasajeros viajan a ese país.
#- Salir del programa.

#Creamos dos listas vacías, una para los pasajeros y otra para las ciudades
travellers=[]
cities=[]

#En esta función agregamos a los pasajeros, pidiendo nombre, dni y destino
def add_travellers():
    name = input("Ingrese su nombre completo:")
    dni =  int(input("Ingrese su DNI:"))
    destination = input("Ingrese su destino: ")
    travellers.append((name,dni,destination))
    print("Se agregaron los datos con exito!")

#En esta ciudad llenamos la lista de ciudades
def add_cities():
    city = input("Ingrese la ciudad: ")
    country = input("Ingrese el país al que pertenece: ")
    cities.append((city,country))
    print("Datos ingresados con exito!!")

#Esta función busca al pasajero por medio del dni y nos informa a donde viaja
def search_dni(dni):
    for passengers in travellers:
        if passengers[1]==dni:
            return passengers[2]
    return None

#Esta función nos pide una ciudad y nos informa cuantos pasajeros viajan a esa ciudad
def search_city(city):
    count=0
    for passengers in travellers:
        if passengers[2]==city:
            count +=1
    return count

#Esta función muestra al país que viaja el pasajero por medio del dni
def search_country_for_dni(dni):
    ciudad = search_dni(dni)
    for c in cities:
        if c[0] == ciudad:
            return c[1]
    return None

#Esta función pide un País al usuario y informa cuantos pasajeros viajan a ese país
def search_country(country):
    count=0
    for passengers in travellers:
        city = passengers[2]
        for c in cities:
            if c[0] == city and c[1] == country:
                count += 1
    return count
    

#Creamos un menú con opciones para relizar la operación que el usuario desee
while True:
    print("------------------------------------------------")
    print("1. Agregar pasajeros a la lista de viajeros.")
    print("2. Agregar ciudades a la lista de ciudades.")
    print("3.Buscar Ciudad por DNI ")
    print("4.Buscar pasajeros por Ciudad")
    print("5. Buscar País por DNI ")
    print("6. Buscar pasajeros por País ")
    print("7. Salir")
    print("------------------------------------------------")
    opc = int(input("Ingrese la opción que desea: "))
    #Si la opción es 1, llamaremos a la función para llenar la lista de pasajeros
    if opc == 1:
        add_travellers()
        
        #Si el usuario ingresa un 2, llamaremos a la opción para agregar ciudades 
    elif opc == 2:
        add_cities()
        
        #La opción 3 llamara a la opción para buscar un pasajero y su destino por medio del dni
    elif opc == 3:
        dni=int(input("Ingrese su dni: "))
        destination = search_dni(dni)
        if destination: #Verificamos que el dni sea correcto
            print(f"El pasajero viaja a {destination}")
        else: # si el pasajero no se encuentra mostraremos el siguiente mensaje
            print("Pasajero no encontrado")
            
            #La opción 4 llamara a la función para buscar cuantos pasajeros viajan a cierta ciudad
    elif opc == 4:
        city=input("Ingrese la ciudad: ")
        amount = search_city(city)
        print(f"<<{amount}>> es el total de pasajeros que viajan a <<{city}>>")

        #La opción 5 llamara a la función para buscar el país al que viaja el pasajero segun su dni
    elif opc == 5:
        dni=int(input("Ingrese su dni: "))
        cit = search_country_for_dni(dni)
        if cit: # verifica que el dni sea correcto
            print(f"El pasajero viaja desde <<{cit}>>")
        else: #Si no lo encuentra mostrara el siguiente mensaje
            print("Pasajero no encontrado")
            #La opción 6 llamara a la función para buscar cuantos pasajeros viajan a cierto País
    elif opc == 6:
        country = input("Ingrese al país que viaja: ")
        cnt = search_country(country)
        print(f"Hay {cnt} pasajeros que viajan a {country}.")
        #La opcion 7 Termina con el programa
    elif opc == 7:
        print("Hasta Luego!!")
        break
    #Verificamos que la opción ingresada sea correcta sino se mostrara el siguiente mensaje
    else:
        print("Opción incorrecta")

#Ejercicio_2

def get_addresses_invoices(purchases):
    addresses = set()
    for purchase in purchases:
        customer, _, _, address = purchase
        addresses.add(address)
    return list(addresses)

shopping = [('Nuria Costa', 5, 1234.5, 'Calle 1 - 456'), ('Jorge Russo', 7, 3999, 'Calle 2 - 741')]
addresses_invoices = get_addresses_invoices(shopping)
print(addresses_invoices)

#Ejercicio_3

#Creamos un diccionario con los socios fundadores
partners = {
    1: {"nombre": "Amanda Núñez", "ingreso": "17/03/2009", "cuota_al_dia": True},
    2: {"nombre": "Bárbara Molina", "ingreso": "17/03/2009", "cuota_al_dia": True},
    3: {"nombre": "Lautaro Campos", "ingreso": "17/03/2009", "cuota_al_dia": False},
    4:{"nombre":"Mauro Lombardo","ingreso":"13/03/2018" ,"cuota_al_dia":False}
}

#Esta función imprime los socios con sus respectivos datos (Num de socio, Nombre, Fecha de ingreso y si tiene o no la cuota al dia)
def print_partners(partners):
    print("Listado de Socios:")
    for num, data in partners.items():
        share = "al día" if data["cuota_al_dia"] else "pendiente"
        print(f"Socio n°{num}: {data['nombre']}, ingresó: {data['ingreso']}, cuota {share}")

#Esta función muestra el menú de opciones y realiza cambios
def main():
    while True:
        print("\nOpciones:")
        print("1. Informar cantidad de socios")
        print("2. Registrar pago de cuotas")
        print("3. Modificar fecha de ingreso")
        print("4. Dar de baja a un socio")
        print("5. Imprimir listado de socios")
        print("6. Salir")

        #Le pedimos al usuario que ingrese una opción 
        option = input("Elija una opción (1-6): ")
        
        #La opción 1 mostrara la cantidad de socios
        if option == "1":
            print(f"El club tiene {len(partners)} socios.")

            #La opcion 2 registra el pago de los socios que tienen cuota pendiente
        elif option == "2":
            partner_number = int(input("Ingrese el número de socio que ha pagado todas las cuotas adeudadas: "))
            if partner_number in partners:
                partners[partner_number]["cuota_al_dia"] = True
                print(f"Cuotas del socio n°{partner_number} han sido registradas como pagadas.")
            else: #Verifica que el socio ingresado exista
                print("Socio no encontrado.")

        # La opción 3 modifica la fecha de ingreso, solo para los socios que ingresaron el 13/03/2018
        elif option == "3":
            for num, data in partners.items():
                if data["ingreso"] == "13/03/2018":
                    data["ingreso"] = "14/03/2018"
            print("Fecha de ingreso modificada para todos los socios que ingresaron el 13/03/2018.")
        #La opción 4 elimina a un socio    
        elif option == "4":
            discharge_name = input("Ingrese el nombre y apellido del socio que desea dar de baja (nombre apellido): ").strip()
            for num, data in partners.items():
                if data["nombre"] == discharge_name: #Verifica que el nombre ingresado exista y sale del ciclo
                    del partners[num]
                    print(f"{discharge_name} ha sido dado de baja.")
                    break
            else:
                print(f"No se encontró a {discharge_name} en la lista de socios.")
                #La opción 5 llama a la funcion print_partners y imprime la lista de socios
        elif option == "5":
            print_partners(partners)
            #Con esta opción salimos del programa
        elif option == "6":
            print("¡Hasta luego!")
            break
        #Verificamos que las opción ingresada sea válida
        else:
            print("Opción no válida. Por favor, elija una opción válida.")

if __name__ == "__main__":
    main()


            


    













            


    












