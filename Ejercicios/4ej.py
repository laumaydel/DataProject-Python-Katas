# 4. Genera una función que calcule la diferencia entre los valores de dos listas. 
# Usa la función map()

def diferencia_listas(lista1, lista2):
    return list(map(lambda x, y: x - y, lista1, lista2))

res = diferencia_listas([10, 20, 30], [2, 5, 10])

print(f'El resultado de la diferencia es la siguiente lista: {res}')
