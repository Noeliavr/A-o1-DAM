def contar_palabras():
    contador = 0
    while True:
        palabra = input("Dime una palabra, cuando no me quieras decir más escribe FIN: ")
        if palabra == "fin":
            break
        contador += 1
        print("Total de palabras: "+ str(contador))
contar_palabras()