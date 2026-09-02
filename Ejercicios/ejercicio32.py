# 32. Crea una función que tome un nombre completo y una lista de empleados, busque el nombre completo en la lista y
# devuelve el puesto del empleado si está en la lista, de lo contrario, devuelve un mensaje indicando que la persona
# no trabaja aquí.

empleados = [
    {"nombre": "Laura Mayorga", "puesto": "Data Analyst"},
    {"nombre": "Carlos Gómez", "puesto": "Python Developer"},
    {"nombre": "Ana Martínez", "puesto": "Project Manager"},
    {"nombre": "Juan Jiménez", "puesto": "Business"}]


def buscar_empleado(nombre_completo,empleados):
    nombre_normalizado = nombre_completo.strip().title()

    for emp in empleados:
        if emp["nombre"].strip().title() == nombre_normalizado:
            return f"El puesto de {emp['nombre']} es: {emp['puesto']}"
        return f"No se ha encontrado a la persona"


# Ejemplo
print(buscar_empleado("Laura Mayorga", empleados))
