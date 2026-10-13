class Empleado:
    empresa = "TechCorp"
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario
    def __str__(self):
        return f"Nombre: {self.nombre}, Salario: {self.salario}, Empresa: {self.empresa}"
    
class Gerente(Empleado):
    def __init__(self, departamento, nombre, salario):
        self.departamento = departamento
        super().__init__(nombre, salario)
    def aumentar_salario(self, porcentaje, salario):
        self.salario = salario*(porcentaje/100)
        return f"Nombre: {self.nombre}, Salario: {self.salario}, Departamento {self.departamento}, Empresa: {Empleado.empresa} "
