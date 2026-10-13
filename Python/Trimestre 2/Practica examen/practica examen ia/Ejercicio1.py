texto = input("Escribe un texto: ")
textodividido = texto.split()
lista =[]
contarPalabras ={}
palabras_clave =["python", "lista", "diccionario"]

for palabra in textodividido:

  if palabra in palabras_clave:

    if palabra in contarPalabras:
      contarPalabras[palabra] += 1

    else:
      contarPalabras[palabra] = 1


if contarPalabras:
  print("Hemos encontrado palabra prohibida...")
  for palabra, cantidad in contarPalabras.items():
    print(f"{palabra}: {cantidad}")
else:
  print("No hay ninguna palabra prohibida!!")tt5n