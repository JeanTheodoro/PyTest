def nro_perfeito(nro):
    nro_perfeito = 0
    
    for i in range(1,nro):
        if nro % i == 0 :
            nro_perfeito += i
    return nro_perfeito
    
