# 12. Genera una función que al recibir una frase devuelva una lista con la longitud de cada palabra. 
# Usa la función map()

def logitud_palabras(frase):
    palabras = frase.split() #Split sirve para dividir cadena de texto en lista más pequeña
    return list(map(len,palabras)) #Poner list ya que queremos que nos devuelva una lista

fraseejemplo= "Hola, buenas tardes me llamo Laura"
print(logitud_palabras(fraseejemplo))
