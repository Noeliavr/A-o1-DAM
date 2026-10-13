def verificar_edad():
    while True:
        edad = int(input("Introduce tu edad: "))
        if edad < 0:
            print("Error, debes meter un numero positivo")
        elif edad < 18:
            print("Eres menor de edad")
        elif edad < 64:
            print("Adulto")
        else:
            print ("Jubilado")
        continuar = input("Desea continuar S/N: ")
        if continuar == "N":
            print("Hasta luegoooo")
            break
verificar_edad()