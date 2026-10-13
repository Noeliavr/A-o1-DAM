def calcular_descuento(precio, porcentaje):
    if porcentaje > 50:
        print("Descuento no permitido.")
        return precio
    descuento = precio * porcentaje / 100
    return precio - descuento

precio = float(input("Precio: "))
porcentaje = float(input("Porcentaje de descuento: "))
final = calcular_descuento(precio, porcentaje)
print("Precio final: " + str(final))
calcular_descuento()
