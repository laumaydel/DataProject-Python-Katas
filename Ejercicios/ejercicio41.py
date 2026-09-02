# 41. En este ejercicio, se te pedirá que escribas un programa en Python que utilice condicionales para determinar el
# monto final de una compra en una tienda en línea, después de aplicar un descuento. El programa debe hacer lo
# siguiente:

def calcular_compra():
    precio_original = float(input("Precio original del artículo (€): "))
    tiene_cupon = input("¿Tienes un cupón de descuento? (sí/no): ").strip().lower() #Normalizar para comparar a minusculas
    descuento = 0.0 #Indicar que el descuento inicialmente es cero

    if tiene_cupon in ["sí", "si", "s"]: #Poner las tres alternativas que pude escribir cuando se le pregunta
        valor_cupon = float(input("Ingresa el valor del cupón (€): "))
        if valor_cupon > 0:
            descuento = valor_cupon
        else:
            print("El valor del cupón debe ser mayor a cero")

    precio_final = max(0.0, precio_original - descuento) #Poner un límite pq no puede ser un precio negativo
    print(f"Precio original: {precio_original:}€")
    print(f"Descuento aplicado: {descuento:}€")
    print(f"Precio final: {precio_final:}€")


calcular_compra()