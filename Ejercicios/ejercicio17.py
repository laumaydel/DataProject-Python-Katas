# 17. Crea una función que tome una lista de dígitos y devuelva el número correspondiente. Por ejemplo, [5,7,2]
# corresponde al número quinientos setenta y dos (572). Usa la función reduce()

from functools import reduce

def conversion_digitos(lista_numeros):
    return reduce(lambda acc, d: acc * 10 + d, lista_numeros)

ejemplo = [6,8,9,6]
print(conversion_digitos(ejemplo))
    