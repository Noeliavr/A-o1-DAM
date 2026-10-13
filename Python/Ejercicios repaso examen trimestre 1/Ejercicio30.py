def adivina_color():
    color = "verde"
    intentos = 3
    while intentos > 0:
        adivinar = input ("Adivina el color: ")
        if adivinar == color:
            print("Enhorabuena, has adivinado el color")
            return
        else:
            print ("Intentalo de nuevo")
            intentos -=1
    print ("Has agotado los intentos, perdon pero no adivinaste, el color es: "+ color)
adivina_color()