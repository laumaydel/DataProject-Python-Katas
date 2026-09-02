# 19. Crea una función lambda que filtre los números impares de una lista dada.

filtrar_impares = lambda lista: list(filter(lambda x: x%2 != 0, lista)) 
#Para ver si son impares lo que hay que hacer es ver si el módulo es distinto de cero, entonces no es divisible exacto entre 2 --> impar


# Ejemplo
listaejemplo = [2,4,6,7,8,9,10,16,89]
print(filtrar_impares(listaejemplo))