# 13. Genera una función la cual, para un conjunto de caracteres, devuelva una lista de tuplas con cada letra en
# mayúsculas y minúsculas. Las letras no pueden estar repetidas .Usa la función map()

def tuplasMm(caracteres):
    #Con set() eliminamos duplicados, pero primero hay que pasar todo a minuscula para unificar
    unicos = set(map(lambda x: x.lower(), caracteres))
    res = (list(map(lambda x: (x.upper(), x.lower()),unicos)))
    print(res)

#lista de ejmplos 

ejemplo= ["A","a","b","c","D","L","a"]
tuplasMm(ejemplo)