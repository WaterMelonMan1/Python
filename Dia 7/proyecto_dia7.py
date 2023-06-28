import os

class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

class Cliente(Persona):
    def __init__(self, nombre, apellido,numero_cuenta,balance):
        super().__init__(nombre, apellido)
        self.numero_cuenta = numero_cuenta
        self.balance = balance


    def __str__(self):
        return f"{self.nombre} {self.apellido}\nN°Cuenta: {self.numero_cuenta}\nSaldo Total: {self.balance:,.3f}"
    
    def depositar(self):
        deposito = float(input("Cuanto desea depositar: "))
        self.balance = self.balance + deposito

    def retirar(self):
        retiro = float(input("Cuanto dese retirar: "))
        self.balance = self.balance - retiro
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
Usuario1 = Cliente(nombre,apellido,1,0)
def menu_principal():
    os.system('cls')
    print("Que quieres hacer.")
    print("1. Ver estado de la cuenta.")
    print("2. Depositar dinero.")
    print("3. Retirar Dinero")
    print("4. Salir de la App")

def opcion1():
    os.system('cls')
    print("Informacion e la cuenta:")
    print(Usuario1)

def opcion2():
    os.system('cls')
    Usuario1.depositar()

def opcion3():
    os.system('cls')
    Usuario1.retirar()

while True:
    menu_principal()
    opcion = input("Elija una opcion: ")
    if opcion == "1":
        opcion1()
        input("Presiona enter para continuar.....")
    elif opcion == "2":
        opcion2()
        input("Presiona enter para continuar.....")
    elif opcion == "3":
        opcion3()
        input("Presiona enter para continuar.....")
    else:
        break

print("GRacias por usar banco 13")



