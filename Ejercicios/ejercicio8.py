# 8. Escribe un programa que pida al usuario dos números e intente dividirlos. Si el usuario ingresa un valor no numérico
# o intenta dividir por cero, maneja esas excepciones de manera adecuada. Asegúrate de mostrar un mensaje
# indicando si la división fue exitosa o no.

def division():
    try:
        num1 = float(input("Escriba el primer número:")) # float para numeros reales
        num2 = float(input("Escriba el egundo número:"))
        res =num1/num2

    except ValueError:
        print("Los valores deben ser numéricos, no caracteres")

    except ZeroDivisionError:
        print("No se puede dividir entre cero")

    else: 
        print(f'El resultado de la division es{res}')


division() #Hacer ejempplos de que todos funcionan