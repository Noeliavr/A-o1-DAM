class CuentaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def ingresar(self, cantidad):
        self.cantidad = cantidad
        self.saldo += cantidad
        print (f"Ingreso con exito. Saldo: {self.saldo} euros")

    def retirar (self, cantidad):
        if cantidad<self.saldo:
            self.saldo-=cantidad
            print (f"Retirada con exito. Saldo {self.saldo} euros")
        else:
            print("error")

cuenta1= CuentaBancaria ("Bebeeeeeeeeee", 40000)
cuenta1.retirar(200)
cuenta1.ingresar(2000)
print(f"Nuevo Saldo {cuenta1.saldo} de {cuenta1.titular}")