def cero_continuo(*args):
    ceros_repetidos = False
    for i in range(len(args)-1):
        if args[i] == 0 and args[i + 1] == 0:
            ceros_repetidos = True
            break
    return ceros_repetidos

print(cero_continuo(1,1,1,5,0,0))