lista = ['a','b','c','d']
for letra in lista:
    numero_letra = lista.index(letra) + 1
    print(f"{numero_letra}°: {letra}")
print("________________")
masturbanda = ["Alejo","Julio","Litos","Tiago","Correa"]
leter = "P"
for nombres in masturbanda:
    if nombres.startswith(leter):
        print(f"{nombres} empieza por la letra {leter}")
print("________________")
numeros = [1,2,3,4,5]
mi_numero = 0
for num in numeros:
    mi_numero = mi_numero + num
    print(f"{mi_numero}")
print("________________")
palabra = "Python <3 "
for letre in palabra:
    print(f"{letre}") 
print("________________")
palabra = "Java </3"
for letre in palabra:
    print(f"{letre}") 
print("________________")
for a,b in [[1,2], [3,4], [5,6]]:
    print(a, b)
print("________________")
dic = {'clave1':'a','clave2':'b','clave3':'c'}
for item in dic:
    print(item)
for a,b in dic.items():
    print(a,b)
print("________________")
print("________________")
print("________________")
#actividad 1
alumnos_clase = ["María", "José", "Carlos", "Martina", "Isabel", "Tomás", "Daniela"]
for alumno in alumnos_clase:
    print(f"Hola {alumno}")
print("________________")
#actividad 2
lista_numeros = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]
suma_numeros = 0
for num in lista_numeros:
    suma_numeros = suma_numeros + num
print(suma_numeros)
print("________________")
#actividad 3
lista_numeros = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]
suma_pares = 0
suma_impares = 0 

for num in lista_numeros:
    if num % 2 == 0:
        suma_pares = suma_pares + num
    else:
        suma_impares = suma_impares +num
print(suma_pares)
print(suma_impares)