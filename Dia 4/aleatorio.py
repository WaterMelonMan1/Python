from random import *
aleatorio = randint(1,50)
print(aleatorio)

aleatorio2 = round(uniform(1,5),1)
print(aleatorio2)

aleatorio3 = random()
print(aleatorio3)

elejido = ['litos','alejo','tiago']
aleatorio4 = choice(elejido)
print(aleatorio4)

numeros = list(range(5,50,5))
shuffle(numeros)
print(numeros)

#actividad 1
from random import randint
aleatorio = randint(1,10)
#actividad 2
from random import *
aleatorio = random()
#actividad 3
from random import *
nombres = ["Carlos", "Julia", "Nicole", "Laura", "Mailen"]
sorteo = choice(nombres)