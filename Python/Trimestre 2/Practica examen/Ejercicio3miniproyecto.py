riesgo = {
    "increíble": 5,
    "impactante": 3,
    "milagro": 8
}

titular = input("Escribe el titular de la noticia: ")
titularMinuscula = titular.lower()
titularDividido= titular.split()
print(titularMinuscula)
print(titularDividido)
lista =[]
contador = 0

for palabra in titularDividido:
    if palabra in riesgo:
        contador += riesgo[palabra]
        lista.append((palabra, riesgo[palabra]))


if contador == 0:
    textofinal = ("Contenido no sospechoso")
elif contador <6:
    textofinal =("Contenido poco sospechoso")
else:
    textofinal=("Contenido muy sospechoso")
print("riesgo: ", contador," - ",textofinal)