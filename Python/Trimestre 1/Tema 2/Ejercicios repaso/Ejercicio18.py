def suma_hasta(n):
    suma = 0
    for i in range(1, n + 1):
        suma += i
    return suma

n = int(input("Introduce un número positivo: "))
print(f"La suma de los números hasta {n} es {suma_hasta(n)}.")
