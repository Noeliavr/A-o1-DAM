def obtener_punto():
    return (3.5, 4.2, "Punto A")

x, y, nombre = obtener_punto()

print(x)
print(y)
print(nombre)

tupla = obtener_punto()

x = 5
tupla[0] = x


tupla = obtener_punto()

lista = list(tupla)   # convertir a lista
lista.append("Nuevo valor")  # agregar cuarto elemento

tupla = tuple(lista)  # volver a convertir a tupla

print(tupla)


mi_tupla = (1, 2, 1, 3, 1)

# posición del primer 1
posicion = mi_tupla.index(1)

# cuántos 1 hay
cantidad = mi_tupla.count(1)

print("Posición del primer 1:", posicion)
print("Cantidad de veces que aparece 1:", cantidad)
