def maximo(a, b):
    return a if a >= b else b

a = float(input("Primer número: "))
b = float(input("Segundo número: "))
print(f"El número mayor es {maximo(a, b)}")