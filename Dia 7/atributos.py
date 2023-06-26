class pajaro:
    def __init__(self, mi_color, mi_especie):
        self.color = mi_color
        self.especie = mi_especie

mi_pajaro = pajaro('Negro','Papagallo')
print(mi_pajaro.especie,mi_pajaro.color)

#actividad 1
class Casa:
    def __init__(self, color, cantidad_pisos):
        self.color = color
        self.cantidad_pisos = cantidad_pisos

casa_blanca = Casa("blanco", 4)
print(casa_blanca.color, casa_blanca.cantidad_pisos)
#actividad 2
class Cubo:
    caras = 6
    def __init__(self, color):
        self.color = color

cubo_rojo = Cubo("rojo")
print(cubo_rojo.color, cubo_rojo.caras)
#actividad 3
class Personaje:
    real = False
    def __init__(self,especie,magico,edad):
        self.especie = especie
        self.magico = magico
        self.edad = edad
harry_potter = Personaje("Humano",True,17)
print(harry_potter.edad,harry_potter.especie,harry_potter.magico)