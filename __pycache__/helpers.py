class Vehiculo():
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas
    def __str__(self):
        return "Color {}, {} ruedas".format(self.color, self.ruedas)

class Coche(Vehiculo):
    def __init__(self, color, velocidad, cilindrada):
        super().__init__(color, 4)
        self.velocidad = velocidad
        self.cilindrada = cilindrada
    def __str__(self):
        return "Color {}, {} km/h, {} ruedas, {} cc".format(self.color, self.velocidad, self.ruedas, self.cilindrada)

class Formula1(Coche):
    def __init__(self, color, velocidad, cilindrada, equipo):
        super().__init__(color, velocidad, cilindrada)
        self.equipo = equipo
    def __str__(self):
        return "Color {}, {} km/h, {} ruedas, {} cc, {} equipo".format(self.color, self.velocidad, self.ruedas, self.cilindrada, self.equipo)

class Camioneta(Coche):
    def __init__(self, color, velocidad, cilindrada, carga):
        super().__init__(color, velocidad, cilindrada)
        self.ruedas = 6
        self.carga = carga
    def __str__(self):
        return "Color {}, {} km/h, {} ruedas, {} cc, {} kg".format(self.color, self.velocidad, self.ruedas, self.cilindrada, self.carga)

class Bicicleta(Vehiculo):
    def __init__(self, color, tipo):
        super().__init__(color, 2)
        self.tipo = tipo
    def __str__(self):
        return "Color {}, {} ruedas, {} tipo".format(self.color, self.ruedas, self.tipo)

class Quad(Coche, Bicicleta):
    def __init__(self, color, velocidad, cilindrada, tipo, modelo, carga):
        super().__init__(color, velocidad, cilindrada)
        self.ruedas = 4
        self.tipo = tipo
        self.modelo = modelo
        self.carga = carga
    def __str__(self):
        return "Color {}, {} km/h, {} ruedas, {} cc, {} tipo, {} modelo, {} carga".format(self.color, self.velocidad, self.ruedas, self.cilindrada, self.tipo, self.modelo, self.carga)

class Motocicleta(Bicicleta):
    def __init__(self, color, tipo, velocidad, cilindra):
        self.color = color
        self.ruedas = 2
        self.tipo = tipo
        self.velocidad= velocidad
        self.cilindra= cilindra
    def __str__(self): 
        return "Color {}, {} ruedas, {} tipo, {} km/h, {} ruedas".format( self.color, self.ruedas, self.tipo, self.velocidad, self.cilindra)
    
coche1 = Coche("Rojo", 120, 2000)
bicicleta1 = Bicicleta("Azul", "Urbana")
camioneta1 = Camioneta("Blanco", 100, 2500, 500)
#...

def catalogar(Vehiculos):
    for Vehiculo in Vehiculo:
        print("Clase:", type(Vehiculos).__name__)
        print("Atributos:")
        for atributo in dir(Vehiculos):
            if not atributo.startswith("__"):
                print("- ", atributo)
        print()

        
def ver_atributos(objeto, atributo):
    if atributo in dir(objeto):
        print(getattr(objeto, atributo))
    else:
        print("Error")
        
