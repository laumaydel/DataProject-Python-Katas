# 24. Calcula la diferencia total en los valores de una lista. Usa la función reduce() .
from functools import reduce

def diferencia_total (lista):
    res = reduce(lambda acc,x: acc - x,lista)
    print(res)

listaejemplo = [2,3,5,6,1]
diferencia_total(listaejemplo)
