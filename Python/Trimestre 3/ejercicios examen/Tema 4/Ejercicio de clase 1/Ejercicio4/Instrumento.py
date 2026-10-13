from abc import ABC, abstractmethod
class Instrumento(ABC):
  @abstractmethod
  def tocar(self):
    pass

  @abstractmethod
  def afinar(self):
    pass
class Guitarra(Instrumento):
  def tocar(self):
    print("La guitarra se toca asi")
  def afinar(self):
    print("La guitarra se afina asi")

class Piano(Instrumento):
  def tocar(self):
    print("El piano se toca asi")
  def afinar(self):
    print("El piano se afina asi")

Instrumento = [Guitarra(), Piano()]

print("=== Instrumentos ===")
for instrumentos in Instrumento:
    instrumentos.tocar()
    instrumentos.afinar()
    print()