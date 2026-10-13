import csv
with open ("videojuegos.csv", "r") as f:
  reader=csv.DirecReader(f)
with open ("inventario.txt", "w") as f:
  f.write