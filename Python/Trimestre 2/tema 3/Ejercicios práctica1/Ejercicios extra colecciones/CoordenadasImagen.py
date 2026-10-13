punto = (120, 200)

print("Punto en la imagen:", punto)
x, y = punto
print(x)
print(y)
l = list(punto)
print(l)
l[0] = 300
print(l)
punto = tuple(l)
print("Esta es la tupla modificada: ", punto)