lista = ['a','b','c']

mis_tuplas = list(enumerate(lista))

print(mis_tuplas[1][0])

#actividad 1
lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]
for indice,nombre in enumerate(lista_nombres):
    print(f'{nombre} se encuentra en el índice {indice}')

#actividad 2
python = "Python"
lista_indices = list(enumerate(python))


#actividad 3
lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]

for indice,item in enumerate(lista_nombres):
    if item.startswith("M"):
        print(indice)