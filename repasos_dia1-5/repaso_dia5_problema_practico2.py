def descomponer_palabra(palabra):
    palabra = set(palabra)
    palabra_ordenada = ''.join(sorted(list(palabra)))
    return f"{palabra_ordenada}"

print(descomponer_palabra("tetrahijueputa"))