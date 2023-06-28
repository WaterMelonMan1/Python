class Animal: 
    def __init__(self,tipo, edad, color):
        self.tipo = tipo
        self.edad = edad
        self.color = color

    def nacer(self):
        print(f"El {self.tipo} ha nacido")

    def hablar(self):
        print(f"El {self.tipo} emite un sonido")

class Ave(Animal):

    def __init__(self, tipo, edad, color,altura):
        super().__init__(tipo, edad, color)
        self.altura = altura


    def hablar(self):
        print("Pio")

    def volar(self):
        print(f"El {self.tipo} vuela a {self.altura} m de altura")

aguila = Ave('Aguila',2,'negro',100)

#Otra
class padre:
    def hablar(self):
        print("Hola")

class madre:
    def reir(self):
        print("Ja ja")

    def hablar(self):
        print("Que tal?")

class hijo(padre, madre):
    pass

class nieto(hijo):
    pass

mi_nieto = nieto()
mi_nieto.hablar() 

#actividad 1
class Padre():
    def trabajar(self):
        print("Trabajando en el Hospital")

    def reir(self):
        print("Ja ja ja!")

class Madre():
    def trabajar(self):
        print("Trabajando en la Fiscalía")
        
class Hija(Madre,Padre):
    pass

#actividad 2
class Vertebrado:
    vertebrado = True

class Ave(Vertebrado):
    tiene_pico = True
    def poner_huevos(self):
        print("Poniendo huevos")

class Reptil(Vertebrado):
    venenoso = True

class Pez(Vertebrado):
    def nadar(self):
        print("Nadando")
    def poner_huevos(self):
        print("Poniendo huevos")

class Mamifero(Vertebrado):
    def caminar(self):
        print("Caminando")
    def amamantar(self):
        print("Amamantando crías")

class Ornitorrinco(Ave,Reptil,Pez,Mamifero):
    pass

#actividad 3
class Padre():
    color_ojos = "marrón"
    tipo_pelo = "rulos"
    altura = "media"
    voz = "grave"
    deporte_preferido = "tenis"
    def reir(self):
        return "Jajaja"
    def hobby(self):
        return "Pinto madera en mi tiempo libre"
    def caminar(self):
        return "Caminando con pasos largos y rápidos"
        
class Hijo(Padre):
    def hobby(self):
        return "Juego videojuegos en mi tiempo libre"