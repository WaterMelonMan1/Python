def mi_funcion():
    lista = []
    for x in range(1, 5):
        lista.append(x * 20)
    return lista

print(mi_funcion())

def mi_generador():
    for x in range(1, 5):
        yield x * 20

g = mi_generador()
print(next(g))
print(next(g))
print(next(g))

def generador_por_pasos():

    x = 1
    yield x

    x += 1
    yield x

    x += 1
    yield x

g_p = generador_por_pasos()
print(next(g_p))
print(next(g_p))
print(next(g_p))

#actividad 1
def generador():
    num = 1
    while True:
        yield num
        num += 1

gen = generador()
while True:
    print(next(gen))
    input("Enter para continuar")