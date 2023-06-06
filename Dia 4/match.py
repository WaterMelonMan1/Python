seria = "N-02"

match seria:
    case "N-01":
        print("samsung")
    case "N-02":
        print("Nokia")
    case "N-03":
        print("Xiaomi")
    case _:
        print("No hay producto con este codigo")

cliente = {'nombre':'Tiago',
           'Edad': 21,
           'Ocupacion':'Entrenador pokemon'}

pelicula = {'titulo':'spider man',
            'ficha_tecnica':{'protagonista':'peter parker',
                             'director':'tarantino'}}

elementos = [cliente, pelicula, 'libro']

for e in elementos:
    match e:
        case {'nombre': nombre,
              'Edad': Edad,
              'Ocupacion': Ocupacion}:
            print("Es un cliente")
            print(nombre,Edad,Ocupacion)
        case {'titulo': titulo,
              'ficha_tecnica':{'protagonista':protagonista,
                               'director':director}}:
            print("Es una pelicula")
            print(titulo,protagonista,director)
        case _:
            print("No se que es esto")