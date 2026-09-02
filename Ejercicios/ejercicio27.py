# 27. Crea una función que calcule el promedio de una lista de números

#Idem que el ejercicio 10

def promedio(lista):
    if not lista:
        return 0
    return sum(lista)/len(lista)

# Ejemplo
listaejemplo1 = [1,2,3,4,5,6,7,8,9]
print(promedio(listaejemplo1))