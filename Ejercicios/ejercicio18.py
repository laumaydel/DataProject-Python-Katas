# 18. Escribe un programa en Python que cree una lista de diccionarios que contenga información de estudiantes
# (nombre, edad, calificación) y use la función filter para extraer a los estudiantes con una calificación mayor o 
# igual a 90. Usa la función filter()

estudiantes = [
    {"nombre": "Ana", "edad": 20, "calificacion": 85},
    {"nombre": "Luis", "edad": 22, "calificacion": 85},
    {"nombre": "Carlos", "edad": 19, "calificacion": 90},
    {"nombre": "Guille", "edad": 21, "calificacion": 97}]

def estudiante_excelente (lista):
    return list(filter(lambda est: est["calificacion"] >= 90, lista)) #coger el atributo calificacion y filtrar por ese

print(estudiante_excelente(estudiantes))