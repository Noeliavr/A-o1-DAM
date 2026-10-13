def calcular_descuento(precio, porcentaje):

    if porcentaje > 50:
        print("Descuento no permitido")
    else:
        descuento = precio * porcentaje / 100
        return precio - descuento
precio = float(input("Dime el precio: "))
porcentaje = float(input("Dime el porcentaje del descuento: "))
precio_final = calcular_descuento(precio, porcentaje)
print("Precio final: "+ str(precio_final))
