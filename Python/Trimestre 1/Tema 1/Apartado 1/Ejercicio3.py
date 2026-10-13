palabra = input("Dime una palabra: ")

primeros_tres = palabra[:3]

posicion = len(palabra) - 3

ultimos_tres = palabra[posicion:]

resultado = primeros_tres + ultimos_tres

print(resultado)
