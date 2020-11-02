from sum import sum
from numero_perfeito import nro_perfeito
from fibonacci import fibonacci
from calcular_cedulas import calcula_cedula

list = [0,1,1,2,3,5]
value_salary = 1588

## A lista lis_notas_salary representa a quantidade de notas na sequência 200,100,50,20,10,5,2,1
list_notas_salary = [7,1,1,1,1,1,1,1]


def test_sum():
    assert sum(5,3) == 8

def test_nro_perfeito():
    assert nro_perfeito (28) == 28

def test_fibonacci():
    assert fibonacci(list) == True

def test_calcular_cedulas():
    assert calcula_cedula(value_salary, list_notas_salary) == True