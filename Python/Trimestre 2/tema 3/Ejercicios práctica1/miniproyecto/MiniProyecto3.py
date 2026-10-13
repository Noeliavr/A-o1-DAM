riesgo = {
    "increíble": 5,
    "impactante": 3,
    "milagro": 8
}
titular = input("Introduce un titular de la noticia: ")

palabras = titular.lower().split()

print("Palabras en minúscula y dividida: ", palabras)

putnuacion_total = 0
palabras_detectadas ={}

for palabra in palabras:
    if palabra in riesgo:
        puntuacion_total += riesgo[palabra]
        palabras_detectadas[palabra] = riesgo[palabra]

print ("puntuación acumulada: ", puntuacion_total)
print ("palabras sospechosas detectadas: ", palabras_detectadas)

if puntuacion_total >= 8:
    print("Conclusión: Contenido sospechoso")
elif puntuacion_total > 0:
    print("Conclusión: Puede ser sensacionalista")
else:
    print("Conclusión: Parece confiable")

# Reto opcional
if palabras_detectadas:
    print("\nPalabras sospechosas encontradas:")

    # Ordenar por nivel de riesgo (de mayor a menor)
    ordenadas = sorted(palabras_detectadas.items(), key=lambda x: x[1], reverse=True)