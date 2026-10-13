import csv

datos_ventas = [
    ["mes", "producto", "unidades_vendidas"],
    ["Enero", "Celeste", 5],
    ["Enero", "Portal 2", 10],
    ["Febrero", "Hades", 20],
    ["Febrero", "Celeste", 8],
    ["Marzo", "Stardew Valley", 15]
]

with open("ventas.csv", "w", newline="") as f:
    escritor = csv.writer(f)
    escritor.writerows(datos_ventas)

ventas_por_mes = {}

with open("ventas.csv", "r") as f:
    reader = csv.DictReader(f)

    for fila in reader:
        mes = fila["mes"]
        unidades = int(fila["unidades_vendidas"])

        ventas_por_mes[mes] = ventas_por_mes.get(mes, 0) + unidades

mes_mas_ventas = max(ventas_por_mes, key=ventas_por_mes.get)

ranking = sorted(
    ventas_por_mes.items(),
    key=lambda x: x[1],
    reverse=True
)

print("Mes con más ventas:", mes_mas_ventas)
print("Unidades vendidas:", ventas_por_mes[mes_mas_ventas])

print("\nRanking descendente de meses:")
for mes, unidades in ranking:
    print(mes, "-", unidades)