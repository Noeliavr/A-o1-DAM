producto = input()
precio = input()
cantidad = input()
descuento = input()
total = float(precio) * int(cantidad)
desc = total * float(descuento) / 100
final = total - desc
print(str(total) + "€")
print(str(desc) + "€")
print(str(final) + "€")