from sum import sum
from numero_perfeito import nro_perfeito
from fibonacci import fibonacci

list = [0,1,1,2,3,5]

def test_sum():
    assert sum(5,3) == 8

def test_nro_perfeito():
    assert nro_perfeito (28) == 28

def test_fibonacci():
    assert fibonacci(list) == True
