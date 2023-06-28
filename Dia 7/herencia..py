class Animal:

    def __init__(self, edad, color, animal):
        self.animal = animal
        self.edad = edad
        self.color = color

    def nacer(self):
        print(f"Nace el {self.animal}")
    def morir(self):
        print(f"Muere el {self.animal}")
    def respirar(self):
        print(f"El {self.animal} vive y respira")

class Pajaro(Animal):
    pass

class Perro(Animal):
    pass

ave = Pajaro(2, 'Amarillo', 'Aguila')
print(ave.animal, ave.color, ave.edad)
ave.nacer()

perro = Perro(2, 'Marron', 'Criollo')
print(perro.animal, perro.color, perro.edad)
perro.respirar()

#actividad 1
class Persona:
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad

class Alumno(Persona):
    pass
#actividad 2
class Mascota:
    def __init__(self,edad,nombre,cantidad_patas):
        self.edad = edad
        self.nombre = nombre
        self.cantidad_patas = cantidad_patas

class Perro(Mascota):
    pass
#actividad 3
class Vehiculo:
    def acelerar(self):
        pass

    def frenar(self):
        pass

class Automovil(Vehiculo):
    pass
