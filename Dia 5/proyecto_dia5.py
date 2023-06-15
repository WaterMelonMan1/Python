import random

# Lista de palabras
palabras = ['anime','videojuegos','programar','python','madre','peliculas']

# Función para elegir una palabra al azar
def elegir_palabra(palabras):
    return random.choice(palabras)

# Función para pedir al usuario que ingrese una letra
def pedir_letra():
    print(" ")
    letra = input("Ingresa una letra: ")
    while not letra.isalpha() or len(letra) != 1:
        letra = input("Ingresa una letra válida: ")
    return letra.lower()

# Función para chequear si la letra ingresada se encuentra en la palabra
def chequear_letra(letra, palabra_secreta, letras_adivinadas):
    if letra in letras_adivinadas:
        print(f"Ya has adivinado la letra {letra}. Intenta con otra.")
        return True
    elif letra in palabra_secreta:
        print(f"¡Bien hecho! La letra {letra} está en la palabra.")
        letras_adivinadas.append(letra)
        return True
    else:
        print(f"Lo siento, la letra {letra} no está en la palabra.")
        return False

# Función para imprimir el estado actual del juego
def imprimir_juego(palabra_secreta, letras_adivinadas):
    for letra in palabra_secreta:
        if letra in letras_adivinadas:
            print(letra, end=" ")
        else:
            print("_", end=" ")
    print()

# Función para verificar si el jugador ha ganado
def verificar_ganador(palabra_secreta, letras_adivinadas):
    for letra in palabra_secreta:
        if letra not in letras_adivinadas:
            return False
    return True

# Función principal del juego
def jugar_ahorcado():
    palabra_secreta = elegir_palabra(palabras)
    letras_adivinadas = []
    intentos = 6

    print("¡Bienvenido al juego del ahorcado!")
    print("Palabra secreta")
    print(" ")
    imprimir_juego(palabra_secreta, letras_adivinadas)

    while intentos > 0:
        letra = pedir_letra()
        acierto = chequear_letra(letra, palabra_secreta, letras_adivinadas)

        if not acierto:
            intentos -= 1
            print("Lo siento, has fallado. Te quedan", intentos, "intentos.")
            print(" ")
        else:
            print("¡Acertaste!")
            print(" ")

        imprimir_juego(palabra_secreta, letras_adivinadas)

        if verificar_ganador(palabra_secreta, letras_adivinadas):
            print("¡Felicidades! Has ganado.")
            return

    print("Lo siento, has perdido. La palabra era", palabra_secreta)

# Ejecutar el juego
jugar_ahorcado()