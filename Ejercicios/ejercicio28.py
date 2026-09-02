# 28. Crea una función que busque y devuelva el primer elemento duplicado en una lista dada.

def primer_duplicado(lista):
    duplicados = set() #comienza siendo una lista vacía
    for elemento in lista:
        if elemento in duplicados:
            return elemento
        duplicados.add(elemento) #añadir a la lista inicial
    return None  # Si no hay duplicados


# Ejemplo:
print(primer_duplicado([1, 3, 5, 3, 2, 1]))  