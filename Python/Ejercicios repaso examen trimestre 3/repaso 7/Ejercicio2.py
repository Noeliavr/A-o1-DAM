import csv
nuevo_videojuego = []

with open ("videojuegos.csv", "r") as f:
    reader = csv.DictReader(f)
    totalUnidades = 0
    with open("videojuegos.txt", "w") as f:
        for v in reader:
            f.write(f'{v["titulo"]} - {v["genero"]} - {v["stock"]} unidades\n')
            totalUnidades = totalUnidades + int(v["stock"])
        f.write(f" Total de Unidades: {totalUnidades}")