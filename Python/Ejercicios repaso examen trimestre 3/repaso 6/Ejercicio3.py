import csv
datos_ventas = [
   ["mes", "producto", "unidades_vendidas"],
   ["Enero", "Celeste", 5],
   ["Enero", "Portal 2", 10],
   ["Febrero", "Hades", 20],
   ["Febrero", "Celeste", 8],
   ["Marzo", "Stardew Valley", 15]
]

with open ("ventas.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(datos_ventas)


ventasmes ={}


with open ("ventas.csv", "r") as f:
    reader = csv.DictReader(f)
    for fila in reader:
        mes = fila["mes"]
        unidades = int(fila["unidades_vendidas"])

        if mes in ventasmes:
            ventasmes[mes] += unidades
        else:
            ventasmes[mes] = unidades

            