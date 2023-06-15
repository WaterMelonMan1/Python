texto = "Este es el texto de Alejo"
resultado = texto.upper()
print(resultado)

texto = "Este es el texto de Alejo"
resultado = texto.upper()
print(resultado)

texto = "Este es el texto de Alejo"
resultado = texto[2].upper()
print(resultado)

texto = "Este es el texto de Alejo"
resultado = texto.lower()
print(resultado)

texto = "Este es el texto de Alejo"
resultado = texto.split()
print(resultado)

texto = "Este es el texto de Alejo"
resultado = texto.split("e")
print(resultado)

a = "Hola"
b = "me"
c = "llamo"
d = "Alejo"
resultado = " ".join([a,b,c,d])
print(resultado)

texto = "Este es el texto de Alejo"
resultado = texto.find("s")
print(resultado)

texto = "Este es el texto de Alejo"
resultado = texto.replace("Alejo","Dios")
print(resultado)

texto = "Este es el texto de Alejo"
resultado = texto.replace("e","Dios")
print(resultado)

#actividad 1
frase = "Especialmente en las comunicaciones electrónicas, la escritura enteramente en mayúsculas equivale a gritar."
print(frase.upper())

#actividad 2
lista_palabras = ["La","legibilidad","cuenta."]
resultado = " ".join(lista_palabras)
print(resultado)

#actividad 3
frase = "Si la implementación es difícil de explicar, puede que sea una mala idea."
frase = frase.replace("difícil","fácil")
frase = frase.replace("mala","buena")
print(frase)
