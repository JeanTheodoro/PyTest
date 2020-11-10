from sum import sum
from numero_perfeito import nro_perfeito
from fibonacci import fibonacci
from calcular_cedulas import calcula_cedula
from series import series

list = [0,1,1,2,3,5]
value_salary = 1588

## A lista lis_notas_salary representa a quantidade de notas na sequência 200,100,50,20,10,5,2,1
list_notas_salary = [7,1,1,1,1,1,1,1]


## A Lista de teste para o exercicio series.py
list_series = [1, 9, 2, 8, 3, 7, 4, 6, 5, 5, 6, 4, 7, 3, 8, 2, 9, 1]

def test_sum():
    assert sum(5,3) == 8

def test_nro_perfeito():
    assert nro_perfeito (28) == 28

def test_fibonacci():
    assert fibonacci(list) == True

def test_calcular_cedulas():
    assert calcula_cedula(value_salary, list_notas_salary) == True

def test_serie():
    assert series (list_series) == True    