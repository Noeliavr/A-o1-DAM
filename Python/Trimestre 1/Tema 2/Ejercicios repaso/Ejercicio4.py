def operar(a, b, operacion):
    if operacion == "+":
        return a + b
    elif operacion == "-":
        return a - b
    elif operacion == "*":
        return a * b
    elif operacion == "/":
        if b != 0:
            return a / b
        else:
            return "Error: División por cero"
    else:
        return "Operación no válida"

resultado = operar(5, 3, "/")
print(resultado) 
