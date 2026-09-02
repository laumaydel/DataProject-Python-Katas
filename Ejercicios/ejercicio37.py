# 37. Crea una función llamada procesar_texto que procesa un texto según la opción especificada: contar_palabras ,
# reemplazar_palabras , eliminar_palabra . Estas opciones son otras funciones que tenemos que definir primero 
# y llamar dentro de la función procesar_texto 

# Contar palabras
def contar_palabras(texto):
    palabras = texto.lower().split() #En minúscula para unificar
    return {p: palabras.count(p) for p in set(palabras)}

# Función para reemplazar palabras
def reemplazar_palabras(texto, palabra_origen, palabra_nueva):
    return texto.replace(palabra_origen, palabra_nueva)

# Función para eliminar palabra
def eliminar_palabra(texto, palabra):
    # Reemplazamos la palabra por una cadena vacía y limpiamos espacios dobles
    return texto.replace(palabra, "").replace("  ", " ").strip()

# Función principal
def procesar_texto(texto, opcion, *args):
    if opcion == "contar":
        return contar_palabras(texto)
    elif opcion == "reemplazar":
        return reemplazar_palabras(texto, args[0], args[1])
    elif opcion == "eliminar":
        return eliminar_palabra(texto, args[0])
    else:
        raise ValueError(
            f"Opción '{opcion}' no válida. Usa 'contar', 'reemplazar' o 'eliminar'."
        )


## Ejemplos

ejemplo = "python es genial y python es facil"

#Ejemplo 1 
print("Contar:", procesar_texto(ejemplo, "contar"))

#Ejemplo 2
print("Reemplazar:",procesar_texto(ejemplo, "reemplazar", "python", "JavaScript"))

#Ejemplo 3
print("Eliminar:", procesar_texto(ejemplo, "eliminar", "genial"))