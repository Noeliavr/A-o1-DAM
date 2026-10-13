import csv

with open ("videojuegos.csv", "r") as f:
    reader = csv.DictReader(f)
    total=0
    with open("informe.txt","w") as f:
        for t in reader:
            f.write(f' {t["titulo"]} - {t["genero"]} - {t["stock"]} unidades\n')
            total = total +int(t["stock"])
        f.write(f"Total unidades: {total}")