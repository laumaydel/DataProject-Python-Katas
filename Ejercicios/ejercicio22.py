# 22. Dada una lista numérica, obtén el producto total de los valores de dicha lista.Usa la función reduce() .
from functools import reduce

def producto_total(numeros): 
    res = reduce(lambda acc, x: acc * x, numeros)
    print(res)

listaejemplo = [2,3,5,6,1]

producto_total(listaejemplo)
    