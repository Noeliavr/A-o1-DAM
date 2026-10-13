import json
import csv

with open ("contactos.json", "r") as f:
    reader= json.load(f)

    with open("contactos.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(reader)


    with open("contactos.csv", "r") as f:
        reader = csv.reader(f)
        for fila in reader:
            print(fila)