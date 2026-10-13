def cajero():
    saldo = 1000
    while True:
        print("1. Consultar saldo ")
        print("2. Ingresar dinero ")
        print("3. Retirar dinero ")
        print ("4. Salir")
        opcion = input("Elige una opcion: ")
        if opcion == "1":
            print ("Tu saldo actual es:"+ str(saldo))
        elif opcion == "2":
            ingreso = float(input("¿Cuanto quieres ingresar? "))
            saldo += ingreso
            print ("Tu saldo actual es:"+ str(saldo))
        elif opcion == "3":
            retirar = float(input("¿Cuánto quieres retirar? "))
            if retirar > saldo:
                print ("Lo que quieres retirar tiene q ser menos que tu saldo")
            else:
                saldo -= retirar
                print ("Tu saldo actual es:"+ str(saldo))
        elif opcion == "4":
            print ("Saliendo... Hasta luegoo :)")
            break
        else:
            print ("Error, ese número no es válido")

cajero()