# 9. Crea una función que convierta una variable en una cadena de texto y enmascare todos los caracteres con el
# carácter '#', excepto los últimos cuatro.

def incognito(numero):
    texto = str(numero)
    if len(texto) <= 4:
        return texto

    ocultos = "#" * (len(texto)-4) #menos los 4 últimos dígitos
    visibles = texto[-4:] #los cuatro últimos
    res = ocultos + visibles
    print(res)

ejemplo = "1234567890123456"

incognito(ejemplo)