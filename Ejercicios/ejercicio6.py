# 6. Escribe una función que calcule el factorial de un número de manera recursiva.

def factorial(numero):
    if numero == 0 or numero == 1:  #Como el factorial de 0 y de 1 es = 1 hay que poner esto si no sería infinito
        return 1
    return numero * factorial(numero-1) # Manera recursiva ya que se usa la función dentro de ella msima

print(factorial(8))