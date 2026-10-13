class Coche:
  ruedas = 4
  def __init__(self, marca, modelo):
    self.marca = marca
    self.modelo = modelo
  def mostrar_info(self):
    print (f"Marca: {self.marca} Modelo {self.modelo} Ruedas {self.ruedas}")
    
# Crear objetos
coche1 = Coche("Toyota", "Corolla")
coche2 = Coche("Ford", "Focus")

# Mostrar información
coche1.mostrar_info()
coche2.mostrar_info()

#Cambiar numero de ruedas
Coche.ruedas = 6

#Mostrar cambios
coche1.mostrar_info()
coche2.mostrar_info()