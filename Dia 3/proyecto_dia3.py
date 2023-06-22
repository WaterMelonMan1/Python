frase = input("Ingresa una frase: ")
frase = frase.lower()
letra1 = input("Ingresa una letra: ")
letra1 = letra1.lower()
letra2 = input("Ingresa otra letra: ")
letra2 = letra2.lower()
letra3 = input("Ingresa otra letra: ")
letra3 = letra3.lower()

#parte 1 mostrar cantidad de veces que sale cada letra en frase
print(f'''La letra {letra1}, esta en el texto {frase.count(letra1)}  veces.
La letra {letra2}, esta en el texto {frase.count(letra2)}  veces.
La letra {letra3}, esta en el texto {frase.count(letra3)}  veces.''')

#parte 2 cuantas palabras tiene la frase
palabras_totales = frase.split()
print(f"La frase ingresada tiene un total de {len(palabras_totales)} palabras")

#parte 3 cual es la primera letra y la ultima de la frase
print(f'''La primera letra de la frase ingresada es la {frase[0]}.
La ultima letra de la frase ingresada es la {frase[-1]}.''')

#parte 4 invertir frase
print(f"{frase[::-1]}")

#parte 5 dentro de la frase existe el string python 
print("La palabra python esta dentro de esta frase? ", "python" in frase)