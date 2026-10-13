def es_palindromo(palabra):
    palabra = palabra.lower()
    return palabra == palabra[::-1]

texto = input("Introduce una palabra: ")
if es_palindromo(texto):
    print(f"'{texto}' es un palíndromo ✅")
else:
    print(f"'{texto}' no es un palíndromo ❌")