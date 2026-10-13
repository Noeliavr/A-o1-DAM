def cajero():
  saldo = 1000
  while True:
    print("\nBienvenido al cajero automático")
    print("1. Consultar saldo")
    print("2. Retirar dinero")
    print("3. Depositar dinero")
    print("4. Salir")
    
    opcion = input("Seleccione una opción (1-4): ")
    
    if opcion == '1':
      print(f"Su saldo actual es: {saldo} unidades monetarias")
    
    elif opcion == '2':
      cantidad = float(input("Ingrese la cantidad a retirar: "))
      if cantidad > saldo:
        print("Fondos insuficientes.")
      else:
        saldo -= cantidad
        print(f"Ha retirado {cantidad} unidades monetarias. Su nuevo saldo es: {saldo}")
    
    elif opcion == '3':
      cantidad = float(input("Ingrese la cantidad a depositar: "))
      saldo += cantidad
      print(f"Ha depositado {cantidad} unidades monetarias. Su nuevo saldo es: {saldo}")
    
    elif opcion == '4':
      print("Gracias por usar el cajero automático. ¡Hasta luego!")
      break
    
    else:
      print("Opción no válida. Por favor, intente de nuevo.")
      