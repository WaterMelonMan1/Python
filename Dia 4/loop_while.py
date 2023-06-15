monedas = 5

while monedas > 0:
    print(f"Tengo {monedas} monedas")
    monedas -= 1
else:
    print("Me quede sin dinero")
print("__________________")

respuesta = 's'

while respuesta == 's':
    respuesta = input("Quieres seguir? (s/n) : ")
else:
    print("Gracias por participar")

print("__________________")
for letra in "Federico":
    if letra == "i":
        break
    print(letra)

print("__________________")
for letra in "Federico":
    if letra == "r":
        continue
    print(letra)

#actividad 1
numero = 10
while numero >= -5:
    print(numero)
    numero -= 1

#actividad 2
numero = 50
while numero >= 0:
    if numero % 5 == 0:
        print(numero)
    numero -= 1

#actividad 3
lista_numeros = [4,5,8,7,6,9,8,2,4,5,7,1,9,5,6,-1,-5,6,-6,-4,-3]
for num in lista_numeros:
    if num < 0:
        break
    else:
        print(num)