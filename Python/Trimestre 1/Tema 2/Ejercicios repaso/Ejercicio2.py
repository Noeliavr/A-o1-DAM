def es_par(numero):
    return numero % 2 == 0

n = int(input("Introduce un número: "))
if es_par(n):
    print("El número es par.")
else:
    print("El número es impar.")