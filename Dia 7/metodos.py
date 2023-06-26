class pajaro:
    alas = True
    def __init__(self, mi_color, mi_especie):
        self.color = mi_color
        self.especie = mi_especie

    def piar(self):
        print(f"El {self.especie} hace ¡Pio,Pio!")

    def volar(self,altura):
        print(f"El {self.especie} vuela a {altura} metros de altura")

aguila = pajaro('Amarillo','Aguila calva')
aguila.piar()
aguila.volar(15)

#actividad 1
class Perro:
    def ladrar(self):
        print("Guau!")

perro1 = Perro()
perro1.ladrar()

#actividad 2
class Mago:
    def lanzar_hechizo(self):
        print("¡Abracadabra!")

merlin = Mago()
merlin.lanzar_hechizo()

#actividad 3
class Alarma:
    def postergar(self,cantidad_minutos):
        print(f"La alarma ha sido pospuesta {cantidad_minutos} minutos")
        
reloj = Alarma()
reloj.postergar(12)