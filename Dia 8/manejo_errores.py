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
def cociente(num1,num2):
        
    try:
        division = num1 / num2
    except TypeError:
        print("Los argumentos a ingresar deben ser números")
    except ZeroDivisionError:
        print("El segundo argumento no debe ser cero")
    else:
        print(division)

#actividad 3
def abrir_archivo(nombre_archivo):
    
    try:
        archivo = open(nombre_archivo)
    except FileNotFoundError:
        print("El archivo no fue encontrado")
    except:
        print("Error desconocido")
    else:
        print("Abriendo exitosamente")
    finally:
        print("Finalizando ejecución")
    