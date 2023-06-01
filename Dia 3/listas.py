mi_lista = ['a','b,','c']
print(type(mi_lista))

mi_lista = ['a','b,','c']
resultado = len(mi_lista)
print(resultado)

mi_lista = ['a','b,','c']
resultado = mi_lista[0]
print(resultado)

mi_lista = ['a','b,','c']
resultado = mi_lista[0:2]
print(resultado)

mi_lista = ['a','b,','c']
mi_lista2 = ['d','e,','f']
resultado = mi_lista[0]
print(mi_lista + mi_lista2)

mi_lista = ['a','b,','c']
mi_lista2 = ['d','e,','f']
mi_lista3 = mi_lista + mi_lista2
print(mi_lista3)

mi_lista = ['a','b,','c']
mi_lista2 = ['d','e,','f']
mi_lista3 = mi_lista + mi_lista2
mi_lista3[0] = "0"
print(mi_lista3)

mi_lista = ['a','b,','c']
mi_lista2 = ['d','e,','f']
mi_lista3 = mi_lista + mi_lista2
mi_lista3.append('g')
print(mi_lista3)

mi_lista = ['a','b,','c']
mi_lista2 = ['d','e,','f']
mi_lista3 = mi_lista + mi_lista2
mi_lista3.pop()
print(mi_lista3)

mi_lista = ['a','b,','c']
mi_lista2 = ['d','e,','f']
mi_lista3 = mi_lista + mi_lista2
mi_lista3.pop(2)
print(mi_lista3)

mi_lista = ['a','b,','c']
mi_lista2 = ['d','e,','f']
mi_lista3 = mi_lista + mi_lista2
eliminado = mi_lista3.pop(2)
print(mi_lista3)
print(eliminado)

lista = ['g','o','b','m','c']
lista.sort()
print(lista)

lista = ['g','o','b','m','c']
lista.reverse()
print(lista)

lista = ['g','o','b','m','c','g']
lista.sort()
lista.reverse()
print(lista)
print(lista.count('g'))
#actividad 1
mi_lista = ['litos','tiago','alejo','juli','correa']

#actividad 2
medios_transporte = ["avión", "auto", "barco", "bicicleta"]
medios_transporte.append("motocicleta")

#actividad 3
frutas = ["manzana", "banana", "mango", "cereza", "sandía"]
eliminado = frutas.pop(2)