class Vehiculo():
     def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas
     def __str__(self):
        return "Color {}, {} ruedas".format( self.color, self.ruedas )

class Coche(Vehiculo):
    def __init__(self, color, velocidad, cilindrada):
        self.color = color
        self.ruedas = 4
        self.velocidad = velocidad
        self.cilindrada = cilindrada
    def __str__(self):
        return "color {}, {} km/h, {} ruedas, {} cc".format(self.color, self.velocidad, self.ruedas, self.cilindrada )
    
class Camioneta(Coche):
    def __init__(self, color, velocidad, cilindrada,carga):
        self.color = color
        self.ruedas = 6
        self.velocidad = velocidad
        self.cilindrada = cilindrada
        self.carga= carga
    def __str__(self):
        return  "color {}, {} km/h, {} ruedas, {} cc, {} kg".format(self.color, self.velocidad, self.ruedas, self.cilindrada, self.carga)
    
class Bicicleta(Vehiculo):
    def __init__(self, color, tipo):
        self.color = color
        self.ruedas = 2
        self.tipo = tipo
    def __str__(self): 
        return "Color {}, {} ruedas, {} tipo".format( self.color, self.ruedas, self.tipo )

class Motocicleta(Bicicleta):
    def __init__(self, color, tipo, velocidad, cilindra):
        self.color = color
        self.ruedas = 2
        self.tipo = tipo
        self.velocidad= velocidad
        self.cilindra= cilindra
    def __str__(self): 
        return "Color {}, {} ruedas, {} tipo, {} km/h, {} ruedas".format( self.color, self.ruedas, self.tipo, self.velocidad, self.cilindra)


vehiculos = []

coche1 = Coche("Rojo", 120, 2000)
bicicleta1 = Bicicleta("Azul", "Urbana")
camioneta1 = Camioneta("Blanco", 100, 2500, 500)
motocicleta1 = Motocicleta("Negro", "Deportiva", 180, 1000)

vehiculos.append(coche1)
vehiculos.append(bicicleta1)
vehiculos.append(camioneta1)
vehiculos.append(motocicleta1)

def catalogar(vehiculos, ruedas=None):
    if ruedas is not None:
        print("Se han encontrado {} vehículos con {} ruedas:".format(len([v for v in vehiculos if v.ruedas == ruedas]), ruedas))
    else:
        print("Todos los vehículos:")
    
    for vehiculo in vehiculos:
        if ruedas is None or vehiculo.ruedas == ruedas:
            print("- Clase: {} \n  Atributos: {}".format(vehiculo.__class__.__name__, str(vehiculo)))


catalogar(vehiculos)
