def mostrar_multiplos(numero, limite):
    for i in range(numero, limite + 1, numero):
        print(i, end=" ")

n = int(input("Número base: "))
lim = int(input("Límite: "))
mostrar_multiplos(n, lim)