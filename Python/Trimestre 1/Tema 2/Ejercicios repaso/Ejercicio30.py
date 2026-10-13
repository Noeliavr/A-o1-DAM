def adivina_color():
    colores = ['rojo', 'azul', 'verde', 'amarillo', 'naranja']
    color_secreto = 'verde'
    intentos = 3
    print("Adivina el color secreto. Tienes 3 intentos.")
    while intentos > 0:
        intento = input("Introduce un color: ").lower()
        if intento == color_secreto:
            print("¡Felicidades! Has adivinado el color secreto.")
            return
        else:
            intentos -= 1
            print(f"Color incorrecto. Te quedan {intentos} intentos.")
    print(f"Lo siento, has agotado tus intentos. El color secreto era '{color_secreto}'.")
adivina_color()
