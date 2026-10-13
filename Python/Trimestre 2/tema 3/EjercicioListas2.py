# Lista inicial de puntuaciones
puntuaciones = [1200, 800, 950, 1500]

print("Puntuaciones originales:", puntuaciones)

# 1. Pedir nueva puntuación al usuario y añadirla
nueva_puntuacion = int(input("Introduce la puntuación de la nueva partida: "))
puntuaciones.append(nueva_puntuacion)

print("Lista actualizada:", puntuaciones)

# 2. Ordenar de mayor a menor
puntuaciones.sort(reverse=True)

print("Puntuaciones ordenadas (mayor a menor):", puntuaciones)

# 3. Mostrar puntuación más alta y más baja
maxima = max(puntuaciones)
minima = min(puntuaciones)

print("Puntuación más alta:", maxima)
print("Puntuación más baja:", minima)

# 4. Calcular la media
media = sum(puntuaciones) / len(puntuaciones)

print("Media de puntuaciones:", media)
