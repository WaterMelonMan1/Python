mi_set = set((1,2,3,4,5,1,1,2,2,3,3,4,4,(1,2,3)))
print(type(mi_set))
print(mi_set)
#otro_set = {1,2,3}
#print(type(otro_set))
#print(otro_set)
print(len(mi_set))
print(2 in mi_set)

s1 = {1,2,3}
s2 = {3,4,5}
s3 = s1.union(s2)
print(s3)

s1 = {1,2,3}
s1.add(4)
print(s1)

s1 = {1,2,3}
s1.remove(3)
print(s1)

s1 = {1,2,3}
s1.discard(2)
print(s1)

s1 = {1,2,3}
sorteo = s1.pop()
print(sorteo)

s1 = {1,2,3}
s1.clear()
print(s1)

#actividad 1
mi_set_1 = {1, 2, "tres", "cuatro"}
mi_set_2 = {"tres", 4, 5} 
mi_set_3 = mi_set_1.union(mi_set_2)

#actividad 2
sorteo = {"Camila", "Margarita", "Axel", "Jorge", "Miguel", "Mónica"}
sorteo.pop()

#actividad 3
sorteo = {"Camila", "Margarita", "Axel", "Jorge", "Miguel", "Mónica"}
sorteo.add("Damián")