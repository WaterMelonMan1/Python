def suma(*numeros):
    return sum(numeros)

print(suma(5,6,6,8,5,2))

#actividad 1
def suma_cuadrados(*args):
    suma = 0
    for arg in args:
        suma += arg ** 2
    return  suma
#actividad 2
def suma_absolutos(*args):
    suma = 0
    for arg in args:
        suma += abs(arg) #se usa abs para usar solo los numeros en su valor absoluto osea solo positivos
    return suma
#actividad 3
def numeros_persona(nombre,*args):
    suma_numeros = sum(args)
    return f'{nombre}, la suma de tus números es {suma_numeros}'
