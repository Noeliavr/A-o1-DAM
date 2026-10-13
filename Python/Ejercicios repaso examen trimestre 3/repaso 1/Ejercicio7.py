import json
import csv

precios ={}

with open ("videojuegos.csv", "r") as f:
    reader = csv.DictReader(f)
    for fila in reader:
        titulo = fila["titulo"]
        precio = float(fila["precio"])

        precios[titulo] = precio

ventasTotales = {}

with open("ventas.csv", "r") as f:
    ventas = csv.DictReader(f)
    for fila in ventas:
        producto = fila["producto"]
        unidades = int(fila["unidades_vendidas"])

        if producto in ventasTotales:
            ventasTotales[producto] += unidades
        else:
            ventasTotales[producto] = unidades
            
ingresosTotales = {}

total = 0

for precio, unidades in ventasTotales.items():

    precio = precios[producto]
    ingreso = precio * unidades

    ingresosTotales[producto] = ingreso
    total += ingreso

ProductoMasVendido = max(ventasTotales, key=ventasTotales.get)

with open("informe.txt", "w") as f:

    f.write("=== INFORME DE VENTAS ===\n\n")

    f.write(f"Producto más vendido: {ProductoMasVendido}\n\n")

    f.write("Ingresos por producto:\n")

    for producto, ingreso in ingresosTotales.items():
        f.write(f"- {producto}: {ingreso} euros\n")

    f.write(f"\nTotal global de ingresos: {total} euros\n")

print("Informe generado correctamente.")