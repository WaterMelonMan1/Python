menor = min(58,69,72,64,35)
mayor = max(58,69,72,64,35)
print(menor)
print(mayor)

lista = [58,69,72,64,35]
print(max(lista))
print(f"El mayor es {max(lista)} y el menor es {min(lista)}")

lista_nombres = ["Correa","Litos","lejo","Tiago"]
print(min(lista_nombres))

nombre = "Raul"
print(min(nombre.lower()))

dic = {'c1':45,'c2':11}
print(min(dic))
print(min(dic.values()))

#actividad 1
lista_numeros = [44542247/2, 21310/5, 2134747*33, 44556475, 121676, 6654067, 353254, 123134, 55**12, 611**5]
valor_maximo = max(lista_numeros)

#actividad 2
lista_numeros = [44542247/2, 21310/5, 2134747*33, 44556475, 121676, 6654067, 353254, 123134, 55**12, 611**5]
valor_maximo = max(lista_numeros)

#actividad 3
diccionario_edades = {"Carlos":55, "María":42, "Mabel":78, "José":44, "Lucas":24, "Rocío":35, "Sebastián":19, "Catalina":2,"Darío":49}
edad_minima = min(diccionario_edades.values())
ultimo_nombre = max(diccionario_edades.keys())
print(edad_minima)
print(ultimo_nombre)