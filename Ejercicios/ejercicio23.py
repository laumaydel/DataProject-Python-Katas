# 23. Concatena una lista de palabras.Usa la función reduce() .

from functools import reduce
def texto_unido (lista):
    res = reduce(lambda acc,p: acc + p, lista)
    print(res)

palabras = ["Hola", " ", "me", " ", "llamo", " ", "Laura"]
texto_unido(palabras)