# Diccionario de palabras sospechosas y su nivel de riesgo
riesgo = {
    "increíble": 5,
    "impactante": 3,
    "milagro": 8
}

# Pedir titular al usuario
titular = input("Introduce el titular de la noticia: ")

# Normalizar texto
palabras = titular.lower().split()

# Calcular puntuación total
puntuacion = 0

for palabra in palabras:
    if palabra in riesgo:
        puntuacion += riesgo[palabra]

# Mostrar resultado
if puntuacion >= 7:
    print("Riesgo:", puntuacion, "- Contenido sospechoso")
else:
    print("Riesgo:", puntuacion, "- Contenido con bajo riesgo")
