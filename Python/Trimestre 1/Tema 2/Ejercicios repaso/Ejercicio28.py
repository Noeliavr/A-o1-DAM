def notas_medias():
    notas = []
    for i in range(5):
        nota = float(input("Nota " + str(i+1) + ": "))
        notas.append(nota)
    media = sum(notas) / len(notas)
    if media >= 9:
        print("Sobresaliente")
    elif media >= 5:
        print("Aprobado")
    else:
        print("Suspenso")

notas_medias()
