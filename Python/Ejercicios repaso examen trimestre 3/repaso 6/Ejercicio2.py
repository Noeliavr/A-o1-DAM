import csv

with open ("videojuegos.csv", "r") as f:
    reader = csv.DictReader(f)
    totalunidades = 0
    with open("informe.txt", "w") as f:
        for i in reader:
            f.write(f' {i["titulo"]} - {i["genero"]} - {i["stock"]} unidades\n')
            totalunidades = totalunidades + int(i["stock"])
        f.write(f"total unidades {totalunidades}\n")