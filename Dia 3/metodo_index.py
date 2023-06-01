mi_texto = "Este es una prueba"
resultado = mi_texto[0]#resultado E
print(resultado)

mi_texto = "Esta es una prueba"
resultado = mi_texto.index("a")#resultado 3
print(resultado)

mi_texto = "Esta es una prueba"
resultado = mi_texto.index("a",5)#resultado 10 
print(resultado)

mi_texto = "Esta es una prueba"
resultado = mi_texto.index("n",5,10)#resultado 9
print(resultado)

#actividad 1
palabra = "ordenador"
print(palabra[4])

#actividad 2
frase = "En teoría, la teoría y la práctica son los mismos. En la práctica, no lo son."
print(frase.index("práctica"))

#actividad 3
frase = "En teoría, la teoría y la práctica son los mismos. En la práctica, no lo son."
print(frase.index("práctica",30))