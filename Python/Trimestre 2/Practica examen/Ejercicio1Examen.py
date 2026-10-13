diccionario = ["increible", "milagro", "impactante"]
texto = input("Introduce un texto: ").lower()
palabras = texto.split()
palabras_prohibidas = {}
for palabra in palabras:
    if palabra in diccionario:
        palabras_prohibidas[palabra] = palabras_prohibidas.get(palabra, 0) + 1
if palabras_prohibidas:
    print("Palabras prohibidas encontradas:")
    for palabra, veces in palabras_prohibidas.items():
        print(f"- {palabra}: {veces} vez/veces")
else:
    print("No se encontraron palabras prohibidas.")                                         