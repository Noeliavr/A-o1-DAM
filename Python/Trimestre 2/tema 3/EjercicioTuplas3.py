# Tupla original
punto = (120, 200)

print("Punto en la imagen:", punto)

# 1. Desempaquetar la tupla
x, y = punto
print("Coordenada X:", x)
print("Coordenada Y:", y)

# 2. Intentar modificar la tupla (provoca error)
# punto[0] = 300   # ← Descomenta esta línea para ver el error

# 3. Convertir la tupla en lista, modificar y volver a tupla
lista_punto = list(punto)
lista_punto[0] = 300
punto = tuple(lista_punto)

print("Punto modificado:", punto)
