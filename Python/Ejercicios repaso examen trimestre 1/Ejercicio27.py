def control_temperatura():
    temperaturas = []
    while True:
        temperatura = input("Dime temperaturas, cuando quieras parar dime STOP: ")
        if temperatura == "stop":
            break
        temperaturas.append(float(temperatura))
        if temperaturas:
            maxima = max(temperaturas)
            minima = min(temperaturas)
            media = sum(temperaturas) / len(temperaturas)
            print("Máximo: " + str(maxima))
            print ("Mínimo:" + str(minima))
            print ("Media: "+ str(media))
control_temperatura()