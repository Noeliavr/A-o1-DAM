def control_temperatura():
    temperaturas = []
    while True:
        temp = input("Temperatura (stop para terminar): ")
        if temp == "stop":
            break
        temperaturas.append(float(temp))
    if temperaturas:
        max_temp = max(temperaturas)
        min_temp = min(temperaturas)
        media = sum(temperaturas) / len(temperaturas)
        print("Máxima: " + str(max_temp))
        print("Mínima: " + str(min_temp))
        print("Media: " + str(media))

control_temperatura()
