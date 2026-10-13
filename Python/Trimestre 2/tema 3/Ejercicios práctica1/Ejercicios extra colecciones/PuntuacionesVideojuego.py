puntuaciones = [1200, 800, 950, 1500]

print("Puntuaciones originales:", puntuaciones)

puntuacion = int(input("Dime tu nueva puntuación: "))
puntuaciones.append(puntuacion)
print(puntuaciones)
puntuaciones.sort(reverse = True)
print(puntuaciones)
media = sum(puntuaciones) / len(puntuaciones)
print(media)