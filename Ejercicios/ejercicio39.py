# 39. Escribe un programa que determine qué calificación en texto tiene un alumno en base a su calificación numérica.
# Las reglas de calificación son:
# - 0 - 69 insuficiente
# - 70 - 79 bien
# - 80 - 89 muy bien
# - 90 - 100 excelente


def obtener_calificacion(nota):
    if not (0<= nota <= 100):
        return "Nota fuera de rango"

    if nota <= 69: 
        return "insuficiente"
    elif nota <= 79:
        return "bien"
    elif nota <= 89:
        return "muy bien"
    else:
        return "excelente"

#Ejemplo
print(obtener_calificacion(93))