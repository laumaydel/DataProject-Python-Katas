# 9. Escribe una función que tome una lista de nombres de mascotas como parámetro y devuelva una nueva lista
# excluyendo ciertas mascotas prohibidas en España. La lista de mascotas a excluir es 
# ["Mapache", "Tigre","Serpiente Pitón", "Cocodrilo", "Oso"].Usa la función filter()

def filtrar_mascotas(lista):
    prohibidas = ["Mapache", "Tigre","Serpiente Pitón", "Cocodrilo", "Oso"]
    resultado = filter(lambda m: m.strip().title() not in prohibidas, lista)
    return list(resultado)

#Ejemplo 
mis_mascotas = ["Perro", "Gato", "Tigre", "Loro", "Mapache", "Tortuga"]

print(filtrar_mascotas(mis_mascotas)) #Solo devuelve aquellas que están permitidas