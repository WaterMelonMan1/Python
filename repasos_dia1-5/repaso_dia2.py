print("Hola soy un programa que calcula tus comisiones dependiendo de tus ventas totales")
nombre = input("Nombre del trabajador: ")
ventas = input(f"Ventas totales de {nombre}: ")
ventas = float(ventas)
comision = round(ventas * 0.13)
print(f"El trabajador {nombre} tuvo unas comisiones totales de {comision}")

