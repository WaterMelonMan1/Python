nombres = ['Lejo','Tiago','Litos','Correa']
edades = [20,21,19,22]
trabajo = ['Estudia','Rascarse las bolas','Practicas','Tostao']
combinados = list(zip(nombres,edades,trabajo))


for nombre,edad,laburo in combinados:
    print(f"{nombre} tiene {edad} años y se dedica a {laburo}")


#actividades 1 
capitales = ["Berlín", "Tokio", "París", "Helsinki", "Ottawa", "Canberra"]
paises = ["Alemania", "Japón", "Francia", "Finlandia", "Canadá", "Australia"]
combinado_paises = list(zip(capitales,paises))
for capital,pais in combinado_paises:
    print(f"La capital de {pais} es {capital}")

#actividad 2
marcas = ["Nike","Adidas","New Balance","Hugo jefe"]
productos = ["Retro4","Super Stars","Tennis normal","Gorritas"]
mi_zip = zip(marcas,productos)

#actividad 3
español = ["uno","dos","tres","cuatro","cinco"]
portugues = ["um","dois","três","quatro","cinco"]
ingles = ["one","two","three","four","five"]
numeros = list(zip(español,portugues,ingles))

print(numeros)