#Se crea la interaccion con el usuario y 
#se oranizan las variables para ser trabajadas
texto = input("Ingrese un texto: ")
texto = texto.upper()
letra1 = input("ingresa una letra: ")
letra1 = letra1.upper()
letra2 = input("ingresa una segunda letra: ")
letra2 = letra2.upper()
letra3 = input("ingresa una tercera letra: ")
letra3 = letra3.upper()
#se crea la lista
lista_letras = [letra1,letra2,letra3]

#1. cuanats veces aparece las letras seleciconadas en el texto
print("La letra",letra1,"esta",texto.count(letra1),"veces")
print("La letra",letra2,"esta",texto.count(letra2),"veces")
print("La letra",letra3,"esta",texto.count(letra3),"veces")

#2 cuantas palabras hay en el texto
cantidad_palabras = texto.split()
print("La frase tiene un total de",len(cantidad_palabras),"palabras")

#3 primera y ultima letra
print("la primera letra del texto es",texto[0])
print("la ultima letra del texto es",texto[-1])

#4 invertir el orden de las palabras
cantidad_palabras.reverse()
print(" ".join(cantidad_palabras))

#5 encontrar la palabra python
resultado = "PYTHON" in texto
print("la palabra python se encuentra en este texto?", resultado)
