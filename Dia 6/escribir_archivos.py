#archivo = open('Dia 6/texto.txt', 'r') solo para leer el texto
archivo = open('Dia 6/texto.txt', 'w')
archivo.write('hola\n')
archivo.write('mundo')

archivo1 = open('Dia 6/texto1.txt', 'w')
archivo1.write('soy el segundo txt')

archivo2 = open('Dia 6/texto2.txt', 'w')
#Se puede cambiar la w por a en caso 
#tal de que se quiera ir a poner las cosas desde lo ultimo
lista = ['hola','como','estas','?']
for p in lista:
    archivo2.writelines(p + '\n')
archivo2.write('bienvenido')


archivo.close()
archivo1.close()
archivo2.close()

#actividad 1
archivo = open('mi_archivo.txt', 'w')
archivo.write('Nuevo texto')
archivo = open('mi_archivo.txt', 'r')
print(archivo.read())
archivo.close()

#actividad 2
archivo = open('mi_archivo.txt', 'a')
archivo.write('Nuevo inicio de sesión')
archivo.close()
archivo = open('mi_archivo.txt', 'r')
print(archivo.read())
archivo.close()

#actividad 3
registro_ultima_sesion = ["Federico", "20/12/2021", "08:17:32 hs", "Sin errores de carga"]
archivo = open('registro.txt', 'a')
linea = "\t".join(registro_ultima_sesion) + "\n"
archivo.writelines([linea])
archivo.close()

archivo = open('registro.txt', 'r')
contenido = archivo.read()
print(contenido)
archivo.close()