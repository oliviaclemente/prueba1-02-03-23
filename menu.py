# Función para agregar un vehículo
def agregar_vehiculo():
    tipo = input("¿Qué tipo de vehículo desea agregar? (Coche, Formula1, Camioneta, Bicicleta, Motocicleta, Quad) ")
    color = input("Ingrese el color: ")
    
    if tipo == "Coche":
        velocidad = float(input("Ingrese la velocidad en km/h: "))
        cilindrada = int(input("Ingrese la cilindrada en cc: "))
        vehiculo = Coche(color, velocidad, cilindrada)
    elif tipo == "Formula1":
        velocidad = float(input("Ingrese la velocidad en km/h: "))
        cilindrada = int(input("Ingrese la cilindrada en cc: "))
        equipo = input("Ingrese el equipo: ")
        vehiculo = Formula1(color, velocidad, cilindrada, equipo)
    elif tipo == "Camioneta":
        velocidad = float(input("Ingrese la velocidad en km/h: "))
        cilindrada = int(input("Ingrese la cilindrada en cc: "))
        carga = int(input("Ingrese la carga en kg: "))
        vehiculo = Camioneta(color, velocidad, cilindrada, carga)
    elif tipo == "Bicicleta":
        tipo_bici = input("Ingrese el tipo de bicicleta: ")
        vehiculo = Bicicleta(color, tipo_bici)
    elif tipo == "Motocicleta":
        velocidad = float(input("Ingrese la velocidad en km/h: "))
        cilindrada = int(input("Ingrese la cilindrada en cc: "))
        tipo_moto = input("Ingrese el tipo de motocicleta: ")
        vehiculo = Motocicleta(color, tipo_moto, velocidad, cilindrada)
    elif tipo == "Quad":
        velocidad = float(input("Ingrese la velocidad en km/h: "))
        cilindrada = int(input("Ingrese la cilindrada en cc: "))
        tipo_quad = input("Ingrese el tipo de quad: ")
        modelo = input("Ingrese el modelo: ")
        carga = int(input("Ingrese la carga en kg: "))
        vehiculo = Quad(color, velocidad, cilindrada, tipo_quad, modelo, carga)
    else:
        print("Tipo de vehículo no válido.")
        return
    
    vehiculos.append(vehiculo)
    print("Vehículo agregado exitosamente.")
    print()

# Función para mostrar los vehículos
def mostrar_vehiculos():
    for i, vehiculo in enumerate(vehiculos):
        print("Vehículo", i+1)
        print(vehiculo)
        print()

# Función para salir del programa
def salir():
    print("¡Hasta luego!")
    exit()

# Lista de vehículos
vehiculos = []

# Menú principal
while True:
    print("----- MENÚ -----")
    print("1. Agregar vehículo")
    print("2. Mostrar vehículos")
    print("3. Salir")
    
    opcion = input("Ingrese una opción: ")
    
    if opcion == "1":
        agregar_vehiculo()
    elif opcion == "2":
        mostrar_vehiculos()
    elif opcion == "3":
        salir()
    else:
        print("Opción no válida. Intente de nuevo.")
        print()
