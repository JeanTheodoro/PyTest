def calcula_cedula(value, list_cedulas_teste_mesa):
    list_cedulas = [200,100,50,20,10,5,2,1]
    list = []
    retos = 0

    for i in range(0, len(list_cedulas)):
        list.append(value//list_cedulas[i])
        retos = value % list_cedulas[i]
        value = retos
        print(list[i])

    return compare_cedulas(list, list_cedulas_teste_mesa)    
    

def compare_cedulas(list, list_cedulas_teste_mesa):

    list_equals = True
    count = 0

    while count < len(list_cedulas_teste_mesa): 

        if list[count] != list_cedulas_teste_mesa[count]:
            list_equals = False
            break  
        count += 1


    return list_equals
    
