# 40. Escribe una función que tome dos parámetros: figura (una cadena que puede ser "rectangulo" , "circulo" o
# "triangulo" ) y datos (una tupla con los datos necesarios para calcular el área de la figura)

import math

def calcular_area(figura, datos):
    figura = figura.lower() #pasar a minuscula para busar y unificar
    if figura == "rectangulo":
        base, altura = datos
        return base * altura

    elif figura == "triangulo":
        base, altura = datos
        return (base * altura) / 2

    elif figura == "circulo":
        radio = datos[0]
        return math.pi * (radio**2) # ** Se usa para poder elevar, con el 2 detras es al cuadrado

    else:
        raise ValueError(f"Figura '{figura}' no reconocida. Usa 'rectangulo', 'triangulo' o 'circulo'.")


# Ejemplos con las tres figuras: 
print("Rectángulo (5, 4):", calcular_area("rectangulo", (5, 4)))  
print("Triángulo (6, 3):", calcular_area("triangulo", (6, 3)))  
print("Círculo (r=3):", round(calcular_area("circulo", (3,)), 2))  