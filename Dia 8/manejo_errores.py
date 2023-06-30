def pedir_numero_entero():
    while True:
        try:
            numero = int(input("Ingresa un numero: "))
        except:
            print("Ingresa un numero entero")
        else:
            print(f"El numero ingresado fue el {numero}")
            break
    return numero

pedir_numero_entero()

#actividad 1
def suma(num1,num2):
        
    try:
        num1 + num2
    except:
        print("Error inesperado")
    else:
        print(num1 + num2)

#actividad 2
