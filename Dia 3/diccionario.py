diccionario = {'c1':'valor1','c2':'valor2'}
print(diccionario)

clave1 = diccionario['c2']
print(clave1)

cliente = {'nombre':'Alejo','Apellido':'Ospina','edad':20,'talla':'L'}
consulta = (cliente['talla'])
print(consulta)
print(cliente['nombre'])

dic = {'c1':55,'c2':[10,20,30],'c3':{'s1':100,'s2':200}}
print(dic['c1'])
print(dic['c2'])
print(dic['c2'][1])
print(dic['c3'])
print(dic['c3']['s2'])

#actividad 0
dic = {'c1':['a','b','c','d'],'c2':['d','e','f']}
print(dic['c2'][1].upper())


dics = {1:'a',2:'b'}
print(dics)
dics[3] = 'c'
print(dics)
dics[2] = 'B'
print(dics)

print(dics.keys())
print(dics.values())
print(dics.items())


#actividad 1
mi_dic = {'nombre':'Karen','apellido':'Jurgens','edad':35,'ocupacion':'Periodista'}


#actividad 2
mi_dict = {"valores_1":{"v1":3,"v2":6},"puntos":{"points1":9,"points2":[10,300,15]}}
print(mi_dict["puntos"]["points2"][1])

#actividad 3
mi_dic = {"nombre":"Karen", "apellido":"Jurgens", "edad":35, "ocupacion":"Periodista"}
mi_dic["pais"] = "Colombia"
mi_dic["edad"] = 36
mi_dic["ocupacion"] = "Editora"