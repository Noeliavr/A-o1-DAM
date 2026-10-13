class Cuenta:
	def __init__(self, titular, saldo):
		self.titular = titular      # público
		self._saldo = saldo        # protegido
		self.__clave = "1234"      # privado

	def mostrar(self):
		print(f"Titular: {self.titular}, Saldo: {self._saldo}")

	def nuevaclave(self, nueva_clave):
		self.__clave= nueva_clave
	
c = Cuenta("Luis", 1000)
print(c.titular)    # OK
print(c._saldo)     # OK, pero no recomendado
print(c.nuevaclave("12345"))# Acceso posible, pero no recomendado
print(c._Cuenta__clave) 


