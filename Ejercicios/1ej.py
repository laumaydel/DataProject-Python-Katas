# 1. Escribe una función que reciba una cadena de texto como parámetro y 
# devuelva un diccionario con las frecuencias de cada letra en la cadena. 
# Los espacios no deben ser considerados.

def frecuencia_letras(cadena):
    cadena = cadena.replace(" ", "").lower() #Para despreciar los espacios, cambiamos y los eliminamos con replace
    return {letra: cadena.count(letra) for letra in set(cadena)}

cadena1 = "Hola, mi nombre es Laura"

print(frecuencia_letras(cadena1))
