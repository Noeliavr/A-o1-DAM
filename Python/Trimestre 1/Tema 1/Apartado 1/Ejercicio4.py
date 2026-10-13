frase = input("Introduce una frase: ")

inicio = int(input("Introduce la posición de inicio: "))

longitud = int(input("Introduce la longitud del substring: "))

substring = frase[inicio:inicio+longitud]

print("El substring es: ", substring)