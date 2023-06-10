#librerias
from random import *

#lista inicial
palitos = ['-','--','---','----']

#mezclar palitos
def mezclar(lista):
    shuffle(lista)
    return lista

#pedirle intento
def probar_suerte():
    intento = ''

    while intento not in ['1','2','3','4']:
        intento = input("elije un numero del 1 al 4: ")
    return int(intento)

#comprobobar intento
def chequear_intento(lista,intento):
    if lista[intento - 1] == '-':
        print("Eligio el que es igual a su fideo. PERDISTE")
    elif lista[intento - 1] == '--':
        print("Nice palo no tan grande como el otro pero ta bien. GANASTE")
    elif lista[intento - 1] == '---':
        print("Ta bien pero puede ser mejor, GANASTE?")
    else:
        print("Severo palo. GANASTE, NICE COCK")

palitos_nuevos = mezclar(palitos)
intento = probar_suerte()
chequear_intento(palitos_nuevos,intento)

#actividad 1
import random
 
def lanzar_dados():
    return random.randint(1,6), random.randint(1,6)
 
def evaluar_jugada(dado1, dado2):
    suma_dados = dado1 + dado2
    if suma_dados <= 6:
        return f"La suma de tus dados es {suma_dados}. Lamentable"
    elif suma_dados > 6 and suma_dados < 10:
        return f"La suma de tus dados es {suma_dados}. Tienes buenas chances"
    else:
        return f"La suma de tus dados es {suma_dados}. Parece una jugada ganadora"
    
#actividad 2
lista_numeros = [1,2,15,7,2,8]
def reducir_lista(lista):
    lista = list(set(lista))
    lista.sort()
    lista.pop(-1)
    return lista
def promedio(lista):
    valos_medio = sum(lista)/len(lista)
    return valos_medio

#actividad 3
import random
lista_numeros = [1,2,15,7,2,8]
def lanzar_moneda():
    resultado = random.choice(['Cara','Cruz'])
    return resultado

def probar_suerte(moneda, lista):
    if moneda == "Cara":
        print("La lista se autodestruirá")
        return []
    elif moneda == "Cruz":
        print("La lista fue salvada")
        return lista
