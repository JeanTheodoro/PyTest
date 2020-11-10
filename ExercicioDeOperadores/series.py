def series(lista_serie):
    number_min = 1
    number_max = 9
    cout = 0
    list = []

    while cout < 10:
        list.append(number_min + cout)
        list.append(number_max - cout)
        cout = cout + 1
    
    return verficar_lista_iguais(list, lista_serie)

def verficar_lista_iguais(list, lista_serie):

    for c, v in enumerate (lista_serie):

        if list[c] != v :
           return False 
        
        return True
