# 15. Crea una función lambda que sume 3 a cada número de una lista dada

sumar_tres = lambda lista: list(map(lambda x: x + 3, lista))

listaejemplo = [1,2,3,4,5,6,7]
print(sumar_tres(listaejemplo))