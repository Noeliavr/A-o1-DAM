def contar_notas():
    notas = []
    while True:
        try:
            nota = float(input("Ingrese una nota entre 0 y 10 (o -1 para terminar): "))
            if nota == -1:
                break
            if 0 <= nota <= 10:
                notas.append(nota)
            else:
                print("Nota inválida. Intente de nuevo.")
        except ValueError:
            print("Entrada inválida. Por favor ingrese un número.")

    aprobadas = sum(1 for n in notas if n >= 6)
    desaprobadas = sum(1 for n in notas if n < 6)

    print(f"Cantidad de notas aprobadas:", aprobadas)
    print(f"Cantidad de notas desaprobadas:", desaprobadas)
contar_notas()
