import json
import csv

with open ("contactos.json", "r") as f:
    datos_contacto = json.load(f)

    
    with open("contactos.csv", "w") as f:
        campos = ["nombre", "telefono", "favorito"]
        writer = csv.DictWriter (f, fieldnames=campos)
        writer.writeheader()
        writer.writerows(datos_contacto)

    with open ("contactos.csv", "r") as f:
        reader = csv.DictReader(f)

        lista = list(reader)

        total = len(lista)

        print(f"El total de filas es: {total}")