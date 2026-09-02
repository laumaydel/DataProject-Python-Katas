# 5. Ecribe una función que tome una lista de números como parámetro y un valor opcional 
# nota_aprobado, que por defecto es 5. La función debe calcular la media de los números en la lista y 
# determinar si la media es mayor o igual que nota aprobado. Si es así, el estado será "aprobado",
#  de lo contrario, será "suspenso". La función debe devolver una tupla que contenga la media y el estado.

def evaluacion(calificaciones, nota_aprobado = 5):
    media = round(sum(calificaciones)/len(calificaciones),3)
    if media >= nota_aprobado:
        estado = "aprobado"
        print(f'La media es de {media}, teniendo por tanto el curso {estado}')
    else: 
        estado = "suspenso"
    print(f'La media es de {media}, teniendo por tanto el curso {estado}')
    return(media,estado)


    
calificaciones1 = [3.4,7.8,9,10,4.75,8.3,1.4]
evaluacion(calificaciones1) #Ejemplo aprobado

calificaciones2 = [2.3,3.1,4.5,6.7,5.01,3.75]
evaluacion(calificaciones2) # Ejemplo suspenso
