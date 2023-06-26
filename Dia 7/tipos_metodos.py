class pajaro:
    #Metodos de instancia
    alas = True
    def __init__(self, mi_color, mi_especie):
        self.color = mi_color
        self.especie = mi_especie

    def piar(self):
        print(f"El {self.especie} hace ¡Pio,Pio!")

    def volar(self,altura):
        print(f"El {self.especie} vuela a {altura} metros de altura")

    def pintar_negro(self):
        self.color = 'negro'
        print(f"Ahora el {self.especie} es {self.color}")

    #metodos de clase
    @classmethod
    def poner_huevos(cls,cantidad):
        print(f"Puso {cantidad} huevos")
        cls.alas = False
        print(pajaro.alas)

    #metodos estaticos
    @staticmethod
    def mirar():
        print("El pajaro mira")
        

''' Metodos de instancia
aguila = pajaro('Amarillo','Aguila')
aguila.piar()
aguila.volar(15)
aguila.pintar_negro()
aguila.alas = False
print(aguila.alas)'''

pajaro.poner_huevos(3)
pajaro.mirar()

#actividad 1
class Mascota:
    @staticmethod
    def respirar():
        print("Inhalar... Exhalar")        
Mascota.respirar()

#actividad 2
class Mascota:
    @staticmethod
    def respirar():
        print("Inhalar... Exhalar")
        
Mascota.respirar()

#actividad 3
class Personaje:
    def __init__(self, cantidad_flechas):
        self.cantidad_flechas = cantidad_flechas

    def lanzar_flecha(self):
        self.cantidad_flechas -= 1

personaje1 = Personaje(10)
print(personaje1.cantidad_flechas) 

personaje1.lanzar_flecha()
print(personaje1.cantidad_flechas) 
