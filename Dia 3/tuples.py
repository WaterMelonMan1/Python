mi_tuple = (1,2,(10,20),4)
print(mi_tuple[1])
print(mi_tuple[2][1])
mi_tuple = list(mi_tuple)# se pasa de tuple a lista
mi_tuple = tuple(mi_tuple)#Se pasa de lista a tuple
print(type(mi_tuple))

t = (1,2,3)
x,y,z = t
print(x,y,z)

tu = (1,2,3,1)
print(tu.count(1))
print(tu.index(2))

#actividad 1
mi_tupla = (1, 2, 3, 2, 3, 1, 3, 2, 3, 3, 3, 1, 3, 2, 2, 1, 3, 2)
print(mi_tupla.count(2))

#actividad 2
mi_tupla = (1, 2, 3, 2, 3, 1, 3, 2)
mi_lista = list(mi_tupla)

#actividad 3
mi_tupla = (1,2,3,4)
a,b,c,d = mi_tupla