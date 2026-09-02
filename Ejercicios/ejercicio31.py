# 31. Crea una función que solicite al usuario ingresar una lista de nombres y luego solicite un nombre para buscar en
# esa lista. Si el nombre está en la lista, se imprime un mensaje indicando que fue encontrado, de lo contrario, se
# lanza una excepción.

class NombreNoEncontradoError(Exception):
    pass

def buscar_nombre():
    entrada = input("Ingresa una lista de nombres separadas por comas: ")
    nombres = [n.strip().title() for n in entrada.split(",")] #Convertir a minuscula y quitar los espacios extras

    nombre_buscar = input("Ingresa el nombre a buscar").strip().title()

    try:
        if nombre_buscar not in nombres:
            raise NombreNoEncontradoError(f'El nombre {nombre_buscar} no se encuentra en la lista')
        print(f'El nombre {nombre_buscar} fue encontrado en la lista')
    except NombreNoEncontradoError as e:
        print(f"Error: {e}")



buscar_nombre()