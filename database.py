def catalogar(vehiculos):
    for vehiculo in vehiculos:
        print("Clase:", type(vehiculo).__name__)
        print("Atributos:")
        for atributo, valor in vehiculo.__dict__.items():
            print("- {}: {}".format(atributo, valor))
        print()

import database

coche1 = database.Coche("Rojo", 180, 2000)
bicicleta1 = database.Bicicleta("Azul", "Montaña")
quad1 = database.Quad("Negro", 150, 1000, "Deportivo", "Modelo X", 500)
motocicleta1 = database.Motocicleta("Verde", "Deportiva", 250, 1000)

vehiculos = [coche1, bicicleta1, quad1, motocicleta1]

database.catalogar(vehiculos)
