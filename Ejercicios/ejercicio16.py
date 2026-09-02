# 16. Escribe una función que tome una cadena de texto y un número entero n como parámetros y devuelva una lista de
# todas las palabras que sean más largas que n. Usa la función filter()

def lon_palabras(cadena, n):
    palabras = cadena.split() #Guardar cada palabar de la cadena individulamente para poder contar sus caracteres
    return list(filter(lambda p: len(p)> n, palabras))

textoejemplo = "Hola muy buenas tardes, mi nombre es Laura Mayorgas, palabras especialemente largas"

print(lon_palabras(textoejemplo,7))