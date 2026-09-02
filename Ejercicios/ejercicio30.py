# 30. Crea una función que determine si dos palabras son anagramas, es decir, si están formadas por las mismas letras
# pero en diferente orden.

def es_anagrama(palabra1, palabra2):
    # Limpiamos espacios y convertimos a minúsculas para poder comparar
    p1 = palabra1.replace(" ", "").lower()
    p2 = palabra2.replace(" ", "").lower()

    # Si al ordenar alfabéticamente sus letras son idénticas, son anagramas
    return sorted(p1) == sorted(p2)


# Ejemplo:
print(es_anagrama("Roma", "Amor")) 
print(es_anagrama("Hola", "Mundo"))  