def contar_caracteres(texto):
    letras = 0
    numeros = 0
    espacios = 0
    for char in texto:
        if char.isalpha():
            letras += 1
        elif char.isdigit():
            numeros += 1
        elif char == " ":
            espacios += 1
    print("Letras: " + str(letras))
    print("Números: " + str(numeros))
    print("Espacios: " + str(espacios))

texto = input("Texto: ")
contar_caracteres(texto)
