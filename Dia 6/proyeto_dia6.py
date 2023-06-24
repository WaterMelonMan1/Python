#librerias 
import pathlib
import os
#Funcion del menu principal del programa
def menu_principal():
    os.system('cls')
    print("Bienvenido al Libro de recetas !LO QUE NO MATA ENGORDA¡")
    print("La ruta de acceso a la carpeta de recetas es:", os.path.join(os.getcwd(), "Dia 6", "Recetas"))
    #Mostrar cuantas recetas hay dentro de la carpeta
    cantidad_recetas(os.path.join("Dia 6", "Recetas"))

    print("Elige alguna de las siguientes acciones para hacer con el recetario")

    print("Opciones:")
    print("1. Leer una receta")
    print("2. Crear una receta")
    print("3. Crear una nueva categoría")
    print("4. Eliminar una receta")
    print("5. Eliminar una categoría")
    print("6. Salir")
#Funcion para contar la cantidad de recetas en la carpeta receras    
def cantidad_recetas(path):
    contador = 0
    for root, dirs, files in os.walk(path):
        contador += len(files)
    return print(f"Hay un total de {contador} recetas en el recetario")
#funcion para leer la receta de la categoria seleccionada
def opcion1():
    os.system('cls')
    #se da una ruta de carpeta
    ruta_recetas = os.path.join(os.getcwd(), "Dia 6", "Recetas")
    # se usa la funcion para obetener una lista de las categorias
    categorias = obtener_categorias(ruta_recetas)
    print("Categorías existentes:")
    #se hace un iterador que muestre las categorias
    for categoria in categorias:
        print(categoria)
    #se pregunta que categoria desea acceder para añadirlo a la direccion 
    categoria_elegida = input("Ingrese el nombre de la categoría de la receta que desea leer: ")
    categoria_ruta = os.path.join(ruta_recetas, categoria_elegida)
    #se extraen als recetas de la categoria seleecionada
    recetas = obtener_recetas(categoria_ruta)
    print("Recetas existentes en la categoría", categoria_elegida + ":")
    #Se muestran las recetas de la categoria
    for receta in recetas:
        print(receta)
    receta_elegida = input("Ingrese el nombre de la receta que desea leer: ")
    ruta_receta = f"{categoria_ruta}/{receta_elegida}"
    #se crea una variable la cual tiene la direccion de la carpeta mas 
    #los nombres de los archivos que s epidieron antes para mostrar la receta pedida
    #Un ciclo el cual revisara que la receta si se encuentre en la carpeta
    try:
        with open(ruta_receta, "r") as archivo:
            contenido = archivo.read()
            print(contenido)
    except FileNotFoundError:
        print("La receta que desea leer no existe.")

#funcion para crear receta        
def opcion2():
    os.system('cls')
    ruta_recetas = os.path.join(os.getcwd(), "Dia 6", "Recetas")
    categorias = obtener_categorias(ruta_recetas)
    print("Categorías existentes:")
    for categoria in categorias:
        print(categoria)
    categoria_elegida = input("Ingrese el nombre de la categoría en la que desea crear la receta: ")
    categoria_ruta = os.path.join(ruta_recetas, categoria_elegida)
    recetas = obtener_recetas(categoria_ruta)
    print("Recetas existentes en la categoría", categoria_elegida + ":")
    for receta in recetas:
        print(receta)
    receta_nombre = input("Escriba el nombre de la nueva receta: ")
    contenido = input("Escriba el contenido de la nueva receta: ")

    # Crear el archivo en la carpeta correspondiente
    filename = os.path.join(categoria_ruta, receta_nombre + ".txt")
    with open(filename, "w") as f:
        f.write(contenido)

    print("La receta se ha creado exitosamente")
#funcion para crear nuevas categorias
def opcion3():
    os.system('cls')
    ruta_recetas = os.path.join(os.getcwd(), "Dia 6", "Recetas")
    categorias = obtener_categorias(ruta_recetas)
    print("Categorías existentes:")
    for categoria in categorias:
        print(categoria)
    categoria_nombre = input("Escriba el nombre de la nueva categoría: ")

    # Crear la carpeta en la carpeta "Recetas"
    path = os.path.join(ruta_recetas, categoria_nombre)
    os.makedirs(path, exist_ok=True)

    print("La categoría se ha creado exitosamente")
#eliminar una receta
def opcion4():
    os.system('cls')
    ruta_recetas = os.path.join(os.getcwd(), "Dia 6", "Recetas")
    categorias = obtener_categorias(ruta_recetas)
    print("Categorías existentes:")
    for categoria in categorias:
        print(categoria)
    categoria_elegida = input("Ingrese el nombre de la categoría en la que desea eliminar una receta: ")
    categoria_ruta = os.path.join(ruta_recetas, categoria_elegida)
    recetas = obtener_recetas(categoria_ruta)
    print("Recetas existentes en la categoría", categoria_elegida + ":")
    for receta in recetas:
        print(receta)
    receta_nombre = input("Escriba el nombre de la receta que desea eliminar: ")
    filename = os.path.join(categoria_ruta, receta_nombre)
    if os.path.exists(filename):
        os.remove(filename)
        print("La receta se ha eliminado exitosamente")
    else:
        print("La receta no existe")
#eliminar una categoria
def opcion5():
    os.system('cls')
    ruta_recetas = os.path.join(os.getcwd(), "Dia 6", "Recetas")
    categorias = obtener_categorias(ruta_recetas)
    print("Categorías existentes:")
    for categoria in categorias:
        print(categoria)
    categoria_nombre = input("Escriba el nombre de la categoría que desea eliminar: ")
    path = os.path.join(ruta_recetas, categoria_nombre)
    if os.path.exists(path):
        os.rmdir(path)
        print("La categoría se ha eliminado exitosamente")
    else:
        print("La categoría no existe")



#funcion para extraer las categorias de la carpeta recetas
def obtener_categorias(ruta_recetas):
    categorias = []
    for nombre in os.listdir(ruta_recetas):
        ruta = os.path.join(ruta_recetas, nombre)
        if os.path.isdir(ruta):
            categorias.append(nombre)
    return categorias
#funcion para extraer las recetas de la carpeta que se seleccione
def obtener_recetas(ruta_categoria):
    recetas = []
    for nombre in os.listdir(ruta_categoria):
        ruta = os.path.join(ruta_categoria, nombre)
        if os.path.isfile(ruta) and nombre.endswith(".txt"):
            recetas.append(nombre)
    return recetas    

#ciclo que mantiene abierto el menu rpincipal mientras no se presoine el boton 6
while True:
    menu_principal()

    opcion = input("Elija una opcion: ")
    
    if opcion == "1":
        opcion1()
    elif opcion == "2":
        opcion2()
    elif opcion == "3":
        opcion3()
    elif opcion == "4":
        opcion4()
    elif opcion == "5":
        opcion5()
    elif opcion == "6":
        print("Gracias por usar el programa")
        break
    else:
        print("Opción inválida")

    input("Presione cualquier tecla para continuar...")

