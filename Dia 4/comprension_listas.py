palabra = 'python'
lista = []
for letra in palabra:
    lista.append(letra)
print(lista)

lista = [letra for letra in 'python']
print(lista)

lista = [n/2 for n in range(0,50)]
print(lista)

lista = [n for n in range(0,21,2)]
print(lista)

lista = [n for n in range(0,21,2) if n * 2 > 10]
print(lista)

lista = [n  if n * 2 > 10 else 'no' for n in range(0,21,2)]
print(lista)

pies = [10,20,30,40,50]
metros = [n / 3.281 for n in pies]
print(metros)


#actividad 1
valores = [1, 2, 3, 4, 5, 6, 9.5]
valores_cuadrado = [n ** 2 for n in valores]
#actividad 2
valores = [1, 2, 3, 4, 5, 6, 9.5] 
valores_pares = [n for n in valores if n % 2 == 0]
#actividad 3
temperatura_fahrenheit = [32, 212, 275]
grados_celsius = [((grados - 32) * (5/9)) for grados in temperatura_fahrenheit]