texto = input("Escribe un texto aquí: ")
textodividido=texto.split()
print(textodividido)
lista = []
contarPalabras= {}
palabras_misteriosas = ["increíble", "milagro", "impactante"]

for palabra in textodividido:

  if palabra in palabras_misteriosas:

    if palabra in contarPalabras:
      contarPalabras[palabra] += 1

    else:
      contarPalabras[palabra] = 1


if contarPalabras:
  print("Hemos encontrado palabra/s prohibida/s...")
  for palabra, cantidad in contarPalabras.items():
    print(f"{palabra}: {cantidad}")
else:
  print("No hay ninguna palabra prohibida!!")