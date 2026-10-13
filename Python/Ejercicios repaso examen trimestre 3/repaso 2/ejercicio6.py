import csv
import json

with open ("contactos.json", "r") as f:
    datos_contacto = json.dump(f)

    with open ("contactos.csv", "w", newline="") as f:
        campos=["nombre", "telefono", "favorito"]
        writer = csv.DictWriter(f, fieldnames=campos)
        writer.writeheader()
        writer.writerows(datos_contacto)
    
    with open ("contactos.csv", "r") as f:
        reader = csv.DictReader(f)
        fila = list(reader)


        total = len(fila)

        print(f"total filas: {total}")