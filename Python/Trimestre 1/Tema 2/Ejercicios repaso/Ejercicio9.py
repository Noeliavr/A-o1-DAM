def media(lista):
    if len(lista) == 0:
        return 0
    return sum(lista) / len(lista)

numeros = [float(x) for x in input("Introduce números separados por espacio: ").split()]
print(f"La media es {media(numeros)}")