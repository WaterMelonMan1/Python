def contar_primos(n):
    count = 0
    
    for i in range(2, n+1):
        es_primo = True
        
        for j in range(2, i):
            if i % j == 0:
                es_primo = False
                break
        
        if es_primo:
            print(i)
            count += 1
    
    return count

contar_primos(20)