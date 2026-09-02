# 34. Crea la clase Arbol , define un árbol genérico con un tronco y ramas como atributos. Los métodos disponibles son:
# crecer_tronco , nueva_rama , crecer_ramas , quitar_rama e info_arbol . El objetivo es implementar estos métodos para
# manipular la estructura del árbol.

class Arbol:
    def __init__(self):
        self.tronco = 1    #Inicializar 1 tronco 
        self.ramas = [] #Tenemos 0 ramas al inicio, lisrta vacía

    def crecer_tronco(self): #Aumentar la longitud del tronco
        self.tronco += 1

    def nueva_rama(self):
        self.ramas.append(1)  # Agregar una nueva rama de longitud 1

    def crecer_ramas(self):
        self.ramas = [r + 1 for r in self.ramas]  #Aumentar en 1 la longitud de todas las ramas existentes


    def quitar_rama(self, posicion):
        if 0 <= posicion < len(self.ramas):
            self.ramas.pop(posicion)   # Eliminar la rama en una posición específica

        else:
            print(f"Error: La posición {posicion} de la rama no existe.")

    def info_arbol(self):
        return {"longitud_tronco": self.tronco,
                "numero_ramas": len(self.ramas),
                "longitudes_ramas": self.ramas}


#EJEMPLOS
# 1. Crear un árbol
mi_arbol = Arbol()

# 2. Hacer crecer el tronco del árbol una unidad
mi_arbol.crecer_tronco()

# 3. Añadir una nueva rama al árbol
mi_arbol.nueva_rama()

# 4. Hacer crecer todas las ramas del árbol una unidad
mi_arbol.crecer_ramas()

# 5. Añadir dos nuevas ramas al árbol
mi_arbol.nueva_rama()
mi_arbol.nueva_rama()

# 6. Retirar la rama situada en la posición 2 (tercera rama)
mi_arbol.quitar_rama(2)

# 7. Obtener información sobre el árbol
print("Estado final del árbol:", mi_arbol.info_arbol())