# 11. Escribe un programa que pida al usuario que introduzca su edad. Si el usuario ingresa un valor no numérico o un
# valor fuera del rango esperado (por ejemplo, menor que 0 o mayor que 120), maneja las excepciones
# adecuadamente.

def verificar_edad():
        try: 
            edad = int(input("¿Cuantos años tiene?: "))
            if edad < 0  or edad > 120: 
                raise ValueError(print("La edad debe estar comprendida entre 0 y 120 años"))

        except: 
              ValueError
        else: 
         print(f'Edad registrada correctamemnte: {edad} años')

verificar_edad()