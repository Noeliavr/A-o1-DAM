def verificar_edad():
    try:
        edad = int(input("Por favor, ingrese su edad: "))
        if edad < 0:
            print("La edad no puede ser negativa.")
        elif edad < 18:
            print("Eres menor de edad.")
        else:
            print("Eres mayor de edad.")
    except ValueError:
        print("Entrada inválida. Por favor, ingrese un número entero para la edad.")
verificar_edad()
