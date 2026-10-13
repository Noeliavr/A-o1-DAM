# Lista original
colores_usados = ["rojo", "azul", "rojo", "verde", "azul", "amarillo"]

# Convertimos la lista en set (elimina duplicados)
colores_distintos = set(colores_usados)

print("Colores distintos:", colores_distintos)

# 1. Mostrar cuántos colores diferentes se han usado
print("Cantidad de colores distintos:", len(colores_distintos))

# 2. Añadir el color "negro"
colores_distintos.add("negro")
print("Después de añadir negro:", colores_distintos)

# 3. Intentar añadir "rojo" (no se repetirá)
colores_distintos.add("rojo")
print("Después de intentar añadir rojo:", colores_distintos)

# 4. Preguntar un color al usuario y comprobar si está en el set
color_usuario = input("Introduce un color: ")

if color_usuario in colores_distintos:
    print("El color está en colores_distintos.")
else:
    print("El color NO está en colores_distintos.")
