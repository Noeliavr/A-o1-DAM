resolucion = input()
x = resolucion.find('x')
ancho = resolucion[:x]
alto = resolucion[x+1:]
pixeles = int(ancho) * int(alto)
ratio = round(float(ancho) / float(alto), 2)
# Usamos una lista y multiplicación booleana para elegir el texto
tipos = ["Cuadrado", "Estándar", "Panorámico"]
# True es 1, False es 0. Solo uno será 1.
formato = tipos[(ratio > 1.5) * 2 + (ratio >= 1.2 and ratio <= 1.5) * 1]
print("Ancho:", ancho)
print("Alto:", alto)
print("Píxeles:", pixeles)
print("Ratio:", ratio)
print("Formato:", formato)