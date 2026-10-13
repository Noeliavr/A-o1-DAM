class Empleado:
  empresa = "TechCorp"
  def __init__(self, nombre, salario):
    self.nombre = nombre
    self.salario = salario
  def __str__(self):
    return f"Nombre: {self.nombre}, Salario: {self.salario}, Empresa: {self.empresa}, departamento: {Gerente.departamento}"

class Gerente(Empleado):
  def __init__ (self,nombre, salario, departamento):
    super().__init__(nombre, salario)
    self.departamento = departamento
  def aumentar_salario(self, porcentaje):
    self.salario += self.salario * (porcentaje / 100)
    return f"Nombre: {self.nombre}, Salario: {self.salario}, Departamento {self.departamento}, Empresa: {Empleado.empresa}"
  
  #Crear objetos
empleado1 = Empleado("Ana", 2000)
empleado2 = Empleado("Luis", 2500)

gerente1 = Gerente("Carlos", 4000, "IT")
gerente2 = Gerente("Marta", 4500, "Marketing")

# Mostrar información
print(empleado1)
print(empleado2)
print(gerente1)
print(gerente2)

# Aumentar salario de un gerente
gerente1.aumentar_salario(10)

print("\nDespués del aumento:")
print(gerente1)
  
