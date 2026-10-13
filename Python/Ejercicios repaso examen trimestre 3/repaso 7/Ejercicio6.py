import json
import csv

with open ("contactos.json", "r") as f:
    datos_contacto = json.load(f)

    with open ("contactos.csv", "w", newline="") as f:
        campos = ["nombre", "telefono", "favorito"]
        writer = csv.DictWriter(f, fieldnames= campos)
        writer.writeheader()
        writer.writerows(datos_contacto)

    with open ("contactos.csv", "r") as f:
        reader = csv.reader(f)
        filas = list(reader)

        totalRegistros = len(filas) - 1

        print(f" El archivo contactos.csv tiene {totalRegistros} contactos.")