# 10. Escribe una función que reciba una lista de números y calcule su promedio. Si la lista está vacía, lanza una
# excepción personalizada y maneja el error adecuadamente

class ListaVacia(Exception):
    pass #Lo hago así ya uq epone en el enuncuado "excepción personalizada", si no lo haría con un if que verifique si no está vacía len == 0

def promedio(lista):
    if not lista:
        raise ListaVacia("La lista está vacía")

    return sum(lista)/len(lista)

# Ejemplo
listaejemplo1 = [1,2,3,4,5,6,7,8,9]
listaejemplo2 = []

print(promedio(listaejemplo1))
print(promedio(listaejemplo2))
