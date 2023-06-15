def chequear_3_cifras(numero):
    return numero in range(100,1000)
print(chequear_3_cifras(893))


def chequear_3_cifras(numero):
    return numero in range(100,1000)
suma = 586 + 408
print(chequear_3_cifras(suma))




def chequear_3_cifras(lista):
    for n in lista:
        if n in range(100,1000):
            return True
    return False
print(chequear_3_cifras(lista = [12,15,30,960]))




def chequear_3_cifras(lista):
    lista_cifras = []
    for n in lista:
        if n in range(100,1000):
            lista_cifras.append(n)
        else:
            pass
    return lista_cifras
print(chequear_3_cifras(lista = [12,150,30,960,95,654]))

#actividad 1
lista_numeros = [1,-2,6,8,-9]
def todos_positivos(lista_numeros):
    for n in lista_numeros:
        if n < 0:
            return False
        else: 
            pass
    return True

#actividad 2
lista_numeros =[100,200,1002,1,-5] 
def suma_menores(lista_numeros):
    suma = 0
    for n in lista_numeros:
        if n > 0 and n < 1000:
            suma = n + suma
        else:
            pass
    return suma
#actividad 3
lista_numeros = [1,2,3,4,5,6,7,8,9]
def cantidad_pares(lista_numeros):
    contador = 0
    for n in lista_numeros:
        if n % 2 == 0:
            contador += 1
        else:
            pass
    return contador