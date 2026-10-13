def tipo_numero(n):
    if n > 0:
        return "positivo"
    elif n < 0:
        return "negativo"
    else:
        return "cero"

num = float(input("Introduce un número: "))
print(f"El número es {tipo_numero(num)}.")