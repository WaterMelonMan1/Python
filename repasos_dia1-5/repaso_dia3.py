frase = input("Ingresa una frase: ")
frase = frase.lower()
letra1 = input("Ingresa una letra cualquiera: ")
letra1 = letra1.lower()
letra2 = input("Ingresa otra letra cualquiera: ")
letra2 = letra2.lower()
letra3 = input("Ingresa otra letra cualquiera: ")
letra3 = letra3.lower()

#parte 1 mostrar cantidad de veces que salen las letras 
lista_letras = [letra1,letra2,letra3]

print(f'''La letra {letra1}, esta en el texto {frase.count(letra1)} veces.
La letra {letra2}, esta en el texto {frase.count(letra2)} veces.
La letra {letra3}, esta en el texto {frase.count(letra3)} veces.''')

#parte 2 cuantas palabras tiene el texto
palabras_totales = frase.split()
print(f"La frase tiene un total de {len(palabras_totales)} palabras.")

#parte 3 primera y ultima letra de la frase
print(f'''La primera letra de la frase es {frase[0]}.
La ultima letra es {frase[-1]}''')

#parte 4 invertir el texto
print(f"{frase[::-1]}")

#Parte 5 la palabra python esta dentro de la frase?
print("La palabra python esta dentro de este texto?", "python" in  frase)


