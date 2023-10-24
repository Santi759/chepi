class Motorcycle:
    #Condicion de las motocicletas
    condition="nuevas"
    #Motor apagado==False
    engine=False

    #Creamos una clase vacía para los atributos de la moto
    def __init__(self,color=" ",license_plate=" ",fuel_liters=0, wheels_number=0,brand=" ",model=" ",fabrication_date="",top_speed=0,weight=0):
        self.color= color
        self.licence_plate=license_plate
        self.fuel_liters=fuel_liters
        self.wheels_number=wheels_number
        self.brand=brand
        self.model=model
        self.fabrication_date=fabrication_date
        self.top_speed=top_speed
        self.weight=weight

    #Este metodo enciende el motor
    def star_up(self):
        if self.engine==False:
            #Si el motor se encuentra apagado lo prende cambiando su valor booleano a True
            self.engine=True
            print("El motor ha arrancado")
        else:
            #Sino nos avisa q el motor ya se encontraba en marcha
            print("El motor ya estaba en marcha")

    #Este metodo apaga el motor
    def stop(self):
        if self.engine==True:
            #Si el motor esta encendido lo apaga, cambiando su valor booleano a False
            self.engine=False
            print("El motor se ha detenido")
        else:
            #Si el motor ya estaba detenido nos muestra el siguiente mensaje
            print("El motor ya estaba detenido")

    def getPrice(self,moto):
        return moto.price
        
