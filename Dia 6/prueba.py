import os

def contar_archivos(path):
    contador = 0
    for root, dirs, files in os.walk(path):
        contador += len(files)
    return contador

def limpiar_pantalla():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def mostrar_menu():
    limpiar_pantalla()
    print("Bienvenido al programa de recetas")
    print("La ruta de acceso a la carpeta de recetas es:", os.path.join(os.getcwd(), "Dia 6", "Recetas"))
    print("Hay un total de", contar_archivos(os.path.join("Dia 6", "Recetas")), "recetas en la carpeta")

    print("Opciones:")
    print("1. Leer una receta")
    print("2. Crear una receta")
    print("3. Crear una nueva categoría")
    print("4. Eliminar una receta")
    print("5. Eliminar una categoría")
    print("6. Salir")

def leer_receta():
    limpiar_pantalla()
    ruta_recetas = os.path.join(os.getcwd(), "Dia 6", "Recetas")
    categorias = obtener_categorias(ruta_recetas)
    print("Categorías existentes:")
    for categoria in categorias:
        print(categoria)
    categoria_elegida = input("Ingrese el nombre de la categoría de la receta que desea leer: ")
    categoria_ruta = os.path.join(ruta_recetas, categoria_elegida)
    recetas = obtener_recetas(categoria_ruta)
    print("Recetas existentes en la categoría", categoria_elegida + ":")
    for receta in recetas:
        print(receta)
    receta_elegida = input("Ingrese el nombre de la receta que desea leer: ")
    ruta_receta = f"{categoria_ruta}/{receta_elegida}"
    try:
        with open(ruta_receta, "r") as archivo:
            contenido = archivo.read()
            print(contenido)
    except FileNotFoundError:
        print("La receta que desea leer no existe.")

def obtener_categorias(ruta_recetas):
    categorias = []
    for nombre in os.listdir(ruta_recetas):
        ruta = os.path.join(ruta_recetas, nombre)
        if os.path.isdir(ruta):
            categorias.append(nombre)
    return categorias

def obtener_recetas(ruta_categoria):
    recetas = []
    for nombre in os.listdir(ruta_categoria):
        ruta = os.path.join(ruta_categoria, nombre)
        if os.path.isfile(ruta) and nombre.endswith(".txt"):
            recetas.append(nombre)
    return recetas

def crear_receta():
    limpiar_pantalla()
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

def crear_categoria():
    limpiar_pantalla()
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

def eliminar_receta():
    limpiar_pantalla()
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
    filename = os.path.join(categoria_ruta, receta_nombre + ".txt")
    if os.path.exists(filename):
        os.remove(filename)
        print("La receta se ha eliminado exitosamente")
    else:
        print("La receta no existe")

def eliminar_categoria():
    limpiar_pantalla()
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

while True:
    mostrar_menu()

    opcion = input("Elija una opción: ")
    if opcion == "1":
        leer_receta()
    elif opcion == "2":
        crear_receta()
    elif opcion == "3":
        crear_categoria()
    elif opcion == "4":
        eliminar_receta()
    elif opcion == "5":
        eliminar_categoria()
    elif opcion == "6":
        print("Gracias por usar el programa")
        break
    else:
        print("Opción inválida")

    input("Presione cualquier tecla para continuar...")