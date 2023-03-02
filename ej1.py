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
    
#Realiza una función llamada catalogar() que reciba la lista de vehiculos y los recorra mostrando el nombre de su clase y sus atributos.

def catalogar(vehiculos):
    for vehiculo in vehiculos:
        print("Clase:", type(vehiculo).__name__)
        print("Atributos:")
        for atributo in dir(vehiculo):
            if not atributo.startswith("__"):
                print("- ", atributo)
        print()
        
        
c1= Coche("rojo", 40, 1200)
print(c1)
c2= Coche("amarillo", 50, 1000)
print(c2)
ca1= Camioneta("azul",  90, 3000, 200)
print(ca1)
b1= Bicicleta("lila",  "urbana")
print(b1)
m1= Motocicleta("verde", "deportiva", 10, 200)
print(m1)

#catalogar([c1, c2, ca1, b1, m1])
#catalogar([c1, c2, ca1, b1, m1], 2)
catalogar([c1, c2, ca1, b1, m1], 6)