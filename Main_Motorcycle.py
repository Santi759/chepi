#Importamos la clase Motorcycle
from Motorcycle import Motorcycle

#Inicializamos la primer moto y les damos valores a sus atributos
moto1=Motorcycle (
    color="Rojo",
    license_plate="15T2Y78M",
    fuel_liters=10,
    wheels_number=2,
    brand="Ducati",
    model="DesertX",
    fabrication_date="2020",
    top_speed=220,
    weight=180
)

#Inicializamos la segunda moto
moto2=Motorcycle(
    color="Negro",
    license_plate="R9V12P18",
    fuel_liters=10,
    wheels_number=2,
    brand="BMW",
    model="R1200 GS",
    fabrication_date="2004",
    top_speed=240,
    weight=244
)

print("|------------------|")
print("|Prueba Primer Moto|")
print("|------------------|")
#Probamos el motor de la primer moto, encendiendolo
moto1.star_up()
#Apagamos el motor
moto1.stop()
print("_____________________")

print("|------------------|")
print("|Prueba Segunda Moto|")
print("|------------------|")
#Prendemos el motor de la segunda moto
moto1.star_up()
#Detenemos el motor de la segunda moto
moto1.stop()
print("_____________________")


print("Precio Moto 1:")
# Agrego un atributo precio a la clase motocicleta.
# Este atributo solo tiene un valor asignado al objeto moto1
Motorcycle.price=None
moto1.price=6,631,643
print("  <<<Moto 1>>>")
print("|--------------|")
print(f"|{moto1.brand}        |")
print(f"|{moto1.model}       |")
print(f"|{moto1.fabrication_date}          |")
print(f"|{moto1.color}          |")
print(f"|{moto1.licence_plate}      |")
print("|--------------|")
print(f"|{moto1.price}$|")
print("|--------------|")

#Si el concesionario no hubiera mostrado el precio de la Moto 1 se podría pedir el precio por medio de un método
#La segunda moto no puede usar este método ya que el atributo solo fue asigando al primer objeto

# Le pasamos el objeto a la funcion y la funcion nos devuelve el valor del atributo del objeto
print("La moto 1 Cuesta:")
print("",moto1.getPrice(moto1))
print()

#Si intentamos hacerlo con la Moto 2 nos devolvera None
print("La moto 2 cuesta:")
print("",moto2.getPrice(moto2))
print()
