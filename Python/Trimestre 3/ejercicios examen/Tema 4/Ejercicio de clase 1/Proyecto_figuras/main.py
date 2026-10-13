from figuras.circulo import Circulo
from figuras.rectangulo import Rectangulo

circulo = Circulo(5)
rectangulo = Rectangulo(4, 3)

print("Circulo")
print(f"Area: {circulo.area():.2f}")
print(f"Perimetro: {circulo.perimetro():.2f}")

print("\nRectangulo")
print(f"Area: {rectangulo.area()}")
print(f"Perimetro: {rectangulo.perimetro()}")