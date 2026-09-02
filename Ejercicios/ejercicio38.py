# 38. Genera un programa que nos diga si es de noche, de día o tarde según la hora proporcionada por el usuario

def momento_del_dia(hora):
    if not (0 <= hora <= 23):
        return "Hora no válida. Debe estar entre 0 y 23."
    if 1 <= hora < 6:
            return "Es de día (mañana)."
    if 6 <= hora < 12:
        return "Es de día (mañana)."
    elif 12 <= hora < 20:
        return "Es de tarde."
    else:
        return "Es de noche."


# Ejemplo:
print(momento_del_dia(10))  
print(momento_del_dia(17))  
print(momento_del_dia(22)) 