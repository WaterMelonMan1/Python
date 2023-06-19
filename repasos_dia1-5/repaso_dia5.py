import random

palabras = ['auto','perro','gato','monte','everest','remolque']

#se genera la palabra aleatoria
def elegir_palabra(palabras):
    return random.choice(palabras)

# pedir por teclado una tecla al usuario
def pedir_letra():
    # se coloca un print para generar un espacio y que se vea mejor
    print(" ")
    #Se crea la variable en la que se guardara la letra po teclado 
    letra = input("Ingresa una letra: ")
    #Se hace una verificacion de que la letra 
    #ingreasada si sea alfabetica y solo sea 1
    while not letra.isalpha() or len(letra) != 1:
        #en caso de que no sea alfabetica o mas de una letra
        #Se repetira perguntando por la letra
        print("Recuerda que es solo una letra alfabetica")
        letra = input("Ingresa una letra valida")
    # en caso de que la letra cumpla el requisito 
    # se guardara la letra ingresada
    return letra.lower()#wn miniscula para que siempre se guarde y concida

#Chequear si la letra ingresada se encuentra en la palabra
def chequear_letra(letra,palabra_secreta,letras_adivinadas):
    #condicional si la letra escrita acerto, ya habia sido acertada o fallo
    #la letra ya habia sido acertada con enterioridad
    if letra in letras_adivinadas:
        print(f"Ya has adivinado la letra {letra}. Intenta con otra")
        #devuelve un boolenamo de eleccion si o no 
        #si es true no resta los intentos
        return True
    elif letra in palabra_secreta:
        print(f"¡Bien hecho! La letra {letra} está en la palabra.")
        #al acertar la palabra se meten en la lista letras adivinadas
        #Para asi tener un conteo de cuales ya fueron adivinadas
        letras_adivinadas.append(letra)
        return True
    else:
        print(f"Lo siento, la letra {letra} no está en la palabra.")
        #Al no acertar con letra se retorna falso 
        #lo cual provoca que se le reste un intento
        return False
    
#Imprimir estado de la partida
def imprimir_juego(palabra_secreta,letras_adivinadas):
    #Se crea un ciclo que recorre toda la palabra secreta
    #Comparando la letra ingresada para ver si esta en algun lugar
    for letra in palabra_secreta:
        #Si la letra se enceuntra en la palabra la imprimira
        #Con end cancelamos el salto de linea para que
        # }imprima lo demas en una sola linea
        if letra in letras_adivinadas:
            print(letra, end=" ")
        #En caso de que no se encuentre la letra dejara el espacio
        #Y seguira en la misma linea con el end
        else:
            print("_",end=" ")
    print()

# se verifica si el jugador gano o perdio la partida
def verificar_ganador(palabra_secreta,letras_adivinadas):
    # se crea un ciclo que revise si las 
    # letras adivinadas ya completan la palabra secreta 
    for letra in palabra_secreta:
        # se revisa que las letras esten bien
        # con una sola que no este ya se da por perdida la partida
        if letra not in letras_adivinadas:
            return False
    # en caso de que todas las letras esten bien 
    # se dara como ganada la partida
    return True

# Funcion principal del juego el cual une las demas
def jugar_ahorcado():
    # se estableven variables para alojar los datos necesarios
    palabra_secreta = elegir_palabra(palabras)
    letras_adivinadas = []
    intentos = 6

    print("¡Bienvenido al juego del ahorcado!")
    print("Palabra secreta")
    print(" ")
    #se muestra el juego por comando llamando la funcion correspondiente
    #Al no haber letra aun se imprimiran _ en cada letra de la palabra
    imprimir_juego(palabra_secreta,letras_adivinadas)
    # se hace un ciclo el cual se detendra al llegar los intentos a 0
    while intentos > 0:
        letra = pedir_letra()
        acierto = chequear_letra(letra,palabra_secreta,letras_adivinadas)

        # se hace una condicion la cial si retorna true es que la letra
        # si se encuentra en la palabra y se mostrara que acerto y no se
        # restara los intentos
        # pero si da falso lo contrario no acierta y se le resta un intento
        if not acierto:
            intentos -= 1
            print("Lo siento, has fallado. Te quedan", intentos, "intentos.")
            print(" ")
        else:
            print("¡Acertaste!")
            print(" ")
        
        #se imprimir el juego actualizado con lo adivinado
        imprimir_juego(palabra_secreta,letras_adivinadas)
        
        #se llama la fucion que solo retirna verdadero o falso
        # para ver si la persona gano o no
        if verificar_ganador(palabra_secreta,letras_adivinadas):
            print("¡Felicidades! Has ganado.")
            #aqui se usa el return ya que aqui acabaria el juego
            return
    # si no acerto en adivinar la palabra
    print("Lo siento, has perdido. La palabra era", palabra_secreta)

# Ejecutar el juego
jugar_ahorcado()
    

