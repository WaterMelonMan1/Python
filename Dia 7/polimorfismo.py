class vaca: 

    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        print(self.nombre + " Dice muuu")

class oveja:

    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        print(self.nombre + " Dice Beee")

vaca1 = vaca("Lola")
oveja1 = oveja("Nube")

def animal_habla(animal):
    animal.hablar()

animal_habla(vaca1)
animal_habla(oveja1)

#actividad 1
palabra = "polimorfismo"
lista = ["Clases", "POO", "Polimorfismo"]
tupla = (1, 2, 3, 80)

for objeto in [palabra,lista,tupla]:
    print(len(objeto))

#actividad 2
class Mago():
    def atacar(self):
        print("Ataque mágico")

class Arquero():
    def atacar(self):
        print("Lanzamiento de flecha")

class Samurai():
    def atacar(self):
        print("Ataque con katana")

sabio = Mago()
tirador = Arquero()
luchaddor = Samurai()
personajes = [tirador,sabio,luchaddor]
for personaje in personajes:
    personaje.atacar()

#actividad 3
class Mago():
    def defender(self):
        print("Escudo mágico")

class Arquero():
    def defender(self):
        print("Esconderse")

class Samurai():
    def defender(self):
        print("Bloqueo")

def personaje_defender(personaje):
    personaje.defender()
