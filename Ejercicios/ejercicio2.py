# 2. Dada una lista de números, obtén una nueva lista con el doble de cada valor. 
# Usa la función map()

def doble(lista):
    return list(map(lambda x: x*2, lista)) # Usar lambda para simplificar

listaejemplo = (1,2,3,4,5,6,7,8,9)
print(doble(listaejemplo))