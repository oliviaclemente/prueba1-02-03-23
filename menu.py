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

def catalogar(Vehiculos):
    for Vehiculo in Vehiculo:
        print("Clase:", type(Vehiculos).__name__)
        print("Atributos:")
        for atributo in dir(Vehiculos):
            if not atributo.startswith("__"):
                print("- ", atributo)
        print()




while True:
    print("¿Qué desea hacer?")
    print("1. Mostrar todos los vehículos")
    print("2. Mostrar vehículos con 2 ruedas")
    print("3. Mostrar vehículos con 4 ruedas")
    print("4. Salir")
    opcion = input("Seleccione una opción: ")
    if opcion == "1":
        catalogar(Vehiculo)
    elif opcion == "2":
        catalogar(Vehiculo, 2)
    elif opcion == "3":
        catalogar(Vehiculo, 4)
    elif opcion == "4":
        break
    else:
        print("Opción no válida. Por favor seleccione una opción válida.")


