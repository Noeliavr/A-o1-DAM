def area_rectangulo(base, altura):
    return base * altura

b = float(input("Introduce la base: "))
h = float(input("Introduce la altura: "))
print(f"El área del rectángulo es {area_rectangulo(b, h)}")