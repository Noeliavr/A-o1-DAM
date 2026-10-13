def contar_palabras():
    contador = 0
    while True:
        palabra = input("Palabra (fin para terminar): ")
        if palabra == "fin":
            break
        contador += 1
    print("Total palabras: " + str(contador))

contar_palabras()
