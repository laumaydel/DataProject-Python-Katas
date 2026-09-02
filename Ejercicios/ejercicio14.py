#14. Crea una función que retorne las palabras de una lista de palabras que comience con una letra en especifico. 
# Usa lafunción filter()

def palabras_por_inicial(lista_palabras, letra):
    #Pasar a minuscula para poder comparar
    letra = letra.lower()
    return list(
        filter(lambda p: p.lower().startswith(letra), lista_palabras)) #primero se pasa a mnuscula para poder unificar

listaejemplo = ["Manzana", "Plátano", "Maracuyá","Mango"]
print(palabras_por_inicial(listaejemplo,"M"))
