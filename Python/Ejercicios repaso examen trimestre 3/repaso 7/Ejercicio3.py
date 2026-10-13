import csv
from collections import defaultdict


datos_ventas = [
   ["mes", "producto", "unidades_vendidas"],
   ["Enero", "Celeste", 5],
   ["Enero", "Portal 2", 10],
   ["Febrero", "Hades", 20],
   ["Febrero", "Celeste", 8],
   ["Marzo", "Stardew Valley", 15]
]

with open("ventas.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(datos_ventas)

ventasPorMes = {}

with open ("ventas.csv", "r") as f: 
    reader = csv.DictReader(f)
    for fila in reader:
        mes = fila["mes"]
        unidades = int(fila["unidades_vendidas"])
        
        if mes in ventasPorMes:
            ventasPorMes[mes] += unidades
        else:
            ventasPorMes[mes] = unidades

def obtener_unidades(item):

    return item[1]

items = list(ventasPorMes.items())
item1 = items[1] 

ranking = sorted(ventasPorMes.items(), key=obtener_unidades, reverse=True)


print("--- Ranking de Ventas Mensuales ---")
print(f"Mes con más ventas: {ranking[0][0]} ({ranking[0][1]} unidades)\n")
for mes, unidades in ranking:
    print(f"{mes}: {unidades} unidades")
