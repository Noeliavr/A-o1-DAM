# Lista inicial
lista_compra = ["pan", "leche", "huevos", "manzanas"]

print("Lista inicial:", lista_compra)

# 1. Añadir "agua" al principio
lista_compra.insert(0, "agua")

# Añadir "café" al final
lista_compra.append("café")

print("Después de añadir productos:", lista_compra)

# 2. Mostrar el número total de productos
print("Total de productos:", len(lista_compra))

# 3. Borrar "huevos"
lista_compra.remove("huevos")

print("Después de borrar huevos:", lista_compra)

# 4. Ordenar alfabéticamente
lista_compra.sort()

print("Lista ordenada alfabéticamente:", lista_compra)
