# 20. Para una lista con elementos tipo integer y string obtén una nueva lista sólo con los valores int. 
# Usa la función filter()

def obtener_enteros(lista_mixta):
    return list(filter(lambda x: type(x) is int, lista_mixta)) #Crear un elemento list con solo los que sean int 

listaejemplo = ["Hola", 20, True, 50, -20,"Laura"]

print(obtener_enteros(listaejemplo))

