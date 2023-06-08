if 5 == 2:
    print("Es correcto")
else:
    print("No es correcto")

if 5 == 5:
    print("Es correcto")
else:
    print("No es correcto")

mascota = "conejo"
if mascota == "gato":
    print("Tienes un gato")
elif mascota == "perro":
    print("Tienes un perro")
elif mascota == "Pez":
    print("Tienes un pez")
else:
    print("No se que animal tienes")


edad = 17
calificacion = 3.1
if edad < 18:
    print("Eres menor de edad")
    if calificacion >= 3:
        print("Aprovaste")
    else:
        print("No aprovaste")
else:
    print("Eres un adulto")

#actividad 1
num1 = int(input("Ingresa un número:"))
num2 = int(input("Ingresa otro número:"))

if num1 > num2:
    print(f"{num1} es mayor que {num2}")
elif num2 > num1:
    print(f"{num2} es mayor que {num1}")
else:
    print(f"{num1} y {num2} son iguales")

#actividad 2
edad = 16
tiene_licencia = False

if edad >= 18 and tiene_licencia == True:
    print("Puedes conducir")
elif edad < 18:
    print("No puedes conducir aún. Debes tener 18 años y contar con una licencia")
else:
    print("No puedes conducir. Necesitas contar con una licencia")

#actividad 3
habla_ingles = True
sabe_python = False

if habla_ingles == True and sabe_python == True:
    print("Cumples con los requisitos para postularte")
elif habla_ingles != True and sabe_python != True:
    print("Para postularte, necesitas saber programar en Python y tener conocimientos de inglés")
elif habla_ingles != True and sabe_python == True:
    print("Para postularte, necesitas tener conocimientos de inglés")
elif habla_ingles == True and sabe_python != True:
    print("Para postularte, necesitas saber programar en Python")