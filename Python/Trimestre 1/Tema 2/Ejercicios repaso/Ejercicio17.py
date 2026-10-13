def es_vocal(letra):
    return letra.lower() in "aeiou"

letra = input("Introduce una letra: ")
if es_vocal(letra):
    print("Es una vocal.")
else:
    print("No es una vocal.")