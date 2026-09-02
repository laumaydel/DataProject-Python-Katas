# 3. Escribe una función que tome una lista de palabras y una palabra objetivo como parámetros. 
# La función debe devolver una lista con todas las palabras de la lista original que contengan la 
# palabra objetivo.

def buscar(lista,palabra_objetivo):
    return [palabra for palabra in lista if palabra_objetivo in palabra]


# Ejemplo
frutas = ["manzana", "sandía", "pera", "melocotón", "plátano"]

res1 = buscar(frutas,"ana")
print(f'Contiene ana el resultado1?: {res1}') #La salida es una lista solo con manzana ya que contiene "ana"

# Ejemplo de una cadena que no está en la lista, por ejemplo kiwi
res2 = buscar(frutas,"kiwi")
print(f'Contiene kiwi: {res2}') #Objeto vacío --> lista vacía pq ninguno lo cumple
