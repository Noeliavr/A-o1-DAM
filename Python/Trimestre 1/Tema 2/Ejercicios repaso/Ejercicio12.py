def repetir_texto(texto, veces):
    for _ in range(veces):
        print(texto)

t = input("Texto: ")
n = int(input("Veces: "))
repetir_texto(t, n)