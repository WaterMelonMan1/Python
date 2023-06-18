def devolver_distintos(num1,num2,num3):
    lista_numeros = [num1,num2,num3]
    if sum(lista_numeros) > 15:
        return f"La suma de los numeros da {sum(lista_numeros)} el cual es mayor a 15\nEl numeor mayor es el {max(lista_numeros)}"
    elif sum(lista_numeros) < 10:
        return f"La suma de los numeros da {sum(lista_numeros)} el cual es menor a 10\nEl numero menor es el {min(lista_numeros)}"
    else:
        lista_numeros.sort()
        return f"La suma de los numeros da {sum(lista_numeros)} el cual esta entre 10 y 15\nEl numero intermedio es el {lista_numeros[1]}"

print(devolver_distintos(5,7,3))
