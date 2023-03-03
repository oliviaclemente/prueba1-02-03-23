from helpers import Vehiculo, Coche, Camioneta, Bicicleta, Motocicleta, Formula1, Quad

vehiculos=[]

coche1 = Coche("Rojo", 120, 2000)
bicicleta1 = Bicicleta("Azul", "Urbana")
camioneta1 = Camioneta("Blanco", 100, 2500, 500)
motocicleta1 = Motocicleta("Negro", "Deportiva", 180, 1000)
formula1= Formula1("Amarillo", 300, 5000, "Mercedes")
quad= Quad("Rosa", 20, 300, "Urbana", "Maxxer 300", 3)


vehiculos.append(coche1)
vehiculos.append(bicicleta1)
vehiculos.append(camioneta1)
vehiculos.append(motocicleta1)
vehiculos.append(formula1)
vehiculos.append(quad)


def catalogar(vehiculos, ruedas=None):
    if ruedas is not None:
        print("Se han encontrado {} vehículos con {} ruedas:".format(len([v for v in vehiculos if v.ruedas == ruedas]), ruedas))
    else:
        print("Todos los vehículos:")
    
    for vehiculo in vehiculos:
        if ruedas is None or vehiculo.ruedas == ruedas:
            print("- Clase: {} \n  Atributos: {}".format(vehiculo.__class__.__name__, str(vehiculo)))


catalogar(vehiculos)
