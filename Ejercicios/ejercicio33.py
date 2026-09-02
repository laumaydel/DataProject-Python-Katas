# 33. Crea una función lambda que sume elementos correspondientes de dos listas dadas.

sumar_listas = lambda l1, l2: list(map(lambda x, y: x + y, l1, l2))

lista1 = [1, 2, 3, 4]
lista2 = [10, 20, 30, 40]

print(sumar_listas(lista1,lista2))