# 7. Genera una función que convierta una lista de tuplas a una lista de strings. Usa la función map()

def convertir_tuplas_string(lista_tupla):
    return(list(map(lambda t: str(t), lista_tupla))) #List para gerenara el resultado en una lista
                                                     #Función lambda: Toma cada tupla t y la convierte a tipo "str" 

ejemplo = [("Melocotón",2),("Sandía",3.5),("Aguacate",4)]
print(convertir_tuplas_string(ejemplo))