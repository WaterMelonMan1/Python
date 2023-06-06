from random import *
numero_aleatorio = randint(1,100)
intento = 8
nombre = input("Dime tu Nombre: ")
print(f"Bueno, {nombre}, he pensado un número entre 1 y 100, \ny tienes solo ocho intentos para adivinar cuál crees que es el número")
eleccion = int(input("Ingresa tu numero: "))
booleano = eleccion > 0 and eleccion < 101
estado = ""
while booleano == True:
    while intento > 0:
        if eleccion == numero_aleatorio:
            print(f"Ganaste adivinaste que el numero era el {eleccion}")
            estado = "w"
            break
        elif eleccion > numero_aleatorio:
            print(f"Respuesta es incorrecta ha elegido un número Mayor al número secreto.")
            eleccion = int(input("Ingresa otro numero: "))
            intento -= 1
        elif eleccion < numero_aleatorio:
            print(f"Respuesta es incorrecta ha elegido un número Menor al número secreto.")
            eleccion = int(input("Ingresa otro numero: "))
            intento -= 1
    break
else:
    print(f"El numero {eleccion} esta por fuera de los parametrso permitidos(debe ser entre o y 100)")
if estado == "w":
    print("CONGRATULATION, TE GANASTE UNA BOFETADA")
else:
    print("ERES UN PUTO FRACASADO")
    print(f"EL numero secreto era {numero_aleatorio}")
