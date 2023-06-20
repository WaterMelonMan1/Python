#actividad 1
def abrir_leer(nombre_archivo):
    archivo = open(nombre_archivo, "r")
    contenido = archivo.read()
    archivo.close()
    return contenido

#actividad 2
def sobrescribir(nombre_archivo):
    archivo = open(nombre_archivo, "w")
    archivo.write("contenido eliminado")
    archivo.close()

sobrescribir("ejemplo.txt")

#actividad 3
#con with
def registro_error(nombre_archivo):
    with open(nombre_archivo, "a") as archivo:
        archivo.write("se ha registrado un error de ejecución")
#sin with
def registro_error(nombre_archivo):
    archivo = open(nombre_archivo, "a")
    archivo.write("se ha registrado un error de ejecución")
    archivo.close()