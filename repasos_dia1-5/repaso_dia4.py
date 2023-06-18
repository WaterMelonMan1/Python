import os
import random

#parte 1 se le pregunta el nombre y se le induce al aplicativo a la persona
nombre = input("Ingresa tu nombre: ")
os.system("cls")
print(f"Hola {nombre}, pensado en un numero del 1 al 100\nTienes 8 intentos para adicinar el numero")

#parte 2 se decalara el numero y las herramientas a usar 
numero = 10
vidas = 7
cumple = False
intentos = 0
#parte 3 se empiza el ciclo de 8 veces para el juego y revision del numero sleccionado
#Se cerifica que el numero ingresado si cumpla el requisito x>=0 and x<=100
while cumple == False:
    numero_elejido = int(input("Ingresa el numero que creas que sea: "))
    if (numero_elejido < 0 or numero_elejido > 100):
        print("Haz elejido un numero que no esta permitido, elije otro")
    else:
        break
#se empieza el jueg de 8 intentos
while vidas > 0:
    intentos += 1 
    if numero_elejido == numero:
        if intentos == 1: 
            print("Felicidades haz ganado, al primer intento\nTe ganaste un golpe en la traquea")
            break
        else:
            print(f"Felicidades adivinaste que el numeor secreto era el {numero_elejido}\nNumero de intentos{intentos}")
    elif numero_elejido > numero:
        print("Incorrecto, el numero elejido esta por encima del numero secreto")
        print(f"Intento {intentos}")
        numero_elejido = int(input("Ingresa el numero que creas que sea: "))
        vidas -= 1
    else:
        print("Incorrecto, el numero elejido esta por debajo del numero secreto")
        print(f"Intento {intentos}")
        numero_elejido = int(input("Ingresa el numero que creas que sea: "))
        vidas -= 1

if vidas == 0:
    print("Te usaste tus 8 intentos, que malo eres")