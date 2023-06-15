#se debe tener un txt para este proceso
mi_archivo = open('Dia 6/texto.txt')

#Se lee e imprime lo que tiene el archivo
#print(mi_archivo.read())

#leer solo una linea
#print(mi_archivo.readline())

#primera_linea = mi_archivo.readline()
#print(primera_linea.rstrip())#Quita el salto de linea

#primera_linea = mi_archivo.readline()
#print(primera_linea.upper())#Se puede usar modificadores de string normales

#primera_linea = mi_archivo.readline()
#print(primera_linea)

#for l in mi_archivo:
#    print(f"Aqui dice: {l}")

todas = mi_archivo.readlines()
print(todas)

todas = todas.pop()
print(todas)

#se cierra el archivo
mi_archivo.close()

#actividad 1
mi_archivo = open('texto.txt')
print(mi_archivo.read())

#actividad 2
mi_archivo = open('texto.txt')
print(mi_archivo.readline())

#actividad 3
mi_archivo = open('texto.txt')
linea2 = mi_archivo.readlines()[1]
print(linea2)