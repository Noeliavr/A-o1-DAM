import csv

datos_juegos = [
 ["titulo", "genero", "precio", "stock"],
 ["Celeste", "Plataformas", 19.99, 8],
 ["Hades", "Accion", 24.50, 0],
 ["Stardew Valley", "Simulacion", 14.99, 15],
 ["Portal 2", "Puzzle", 9.99, 6],
 ["Forza Horizon", "Carreras", 39.99, 3]
]


with open("videojuegos.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(datos_juegos)

with open ("videojuegos.csv", "r") as f:
    reader = csv.reader(f)
    for fila in reader:
        if fila[2] < "30":
            if fila[3] > "0":
                print (fila)