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
    print("La guitarra esta sonando")
  
  def afinar(self):
    print("afinando la guitarra")

class Piano(Instrumento):
  def tocar(self):
    print("El piano esta sonando")

  def afinar(self):
    print("Afianando el piano")

    # Demostración de polimorfismo
instrumentos = [Guitarra(), Piano()]

print("=== Instrumentos ===")
for instrumento in instrumentos:
    instrumento.tocar()
    instrumento.afinar()
    print()

    