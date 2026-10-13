def contar_notas():
    notasSuspensas = 0
    notasAprobadas = 0
    while True:
        nota = float(input("Introduceme tus notas, cuando no tengas mas introduce un número negativo. "))
        if nota < 0:
            print("Has acabado :p")
            break
        elif nota >=5:
            notasAprobadas += 1
        else:
            notasSuspensas += 1
    print("Aprobados: " + str(notasAprobadas))
    print("Suspensos: " + str(notasSuspensas))
contar_notas()
