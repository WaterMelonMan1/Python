#un programa el nombre y las ventas, las ventas debes scar el 13%  que es la comision

nombre = input("Ingresa tu nombre: ")
ventas = input("Ingresa el total de ventas: ")
ventas = int(ventas)

comision = ventas * 0.13
print(f"El trabajador {nombre} tuvo unas ventas totales de {ventas}, con lo cual tiene una comision de {comision}")