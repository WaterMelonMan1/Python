precios_cafe = [('capuchino',1.5),('expreso',2.2),('moka',1.9)]

def cafe_caro(lista_precios):
    precio_mayor = 0
    cafe_caro = ''
    
    for cafe,precio in lista_precios:
        if precio > precio_mayor:
            precio_mayor = precio
            cafe_caro = cafe
        else:
            pass
    return (cafe_caro,precio_mayor)

cafe,precio = cafe_caro(precios_cafe)
print(f"El {cafe} es el cafe mas caro con un valor de {precio}")