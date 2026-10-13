def contar_vocales(texto):
    texto = texto.lower()
    contador = 0
    for letra in texto:
        if letra in "aeiou":
            contador += 1
    return contador

frase = input("Introduce un texto: ")
print(f"El texto contiene {contar_vocales(frase)} vocales.")