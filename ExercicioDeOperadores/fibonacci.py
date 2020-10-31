def fibonacci(list):
    
    nro_back = 0
    nro_next = 1
    qdn_item = len(list)
    list_fibonacci = []
    list_fibonacci.append(nro_back)
    list_fibonacci.append(nro_next)

    for i in range(1, (qdn_item - 1)):
        fibonacci = nro_back + nro_next
        nro_back = nro_next
        nro_next = i
        list_fibonacci.append(fibonacci)

    return compare_list(list, list_fibonacci, qdn_item) 

def compare_list(list, list_fibonacci, qdn_item):
    count = 0
    list_equals = True

    while count < qdn_item :

        if list[count] != list_fibonacci[count]:
            list_equals = False
            break
        count += 1
    
    return list_equals
         

    

