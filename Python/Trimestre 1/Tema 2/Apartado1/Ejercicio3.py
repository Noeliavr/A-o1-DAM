
num1 = int(input("Introduce el primer número: "))
num2 = int(input("Introduce el segundo número: "))
suma=range(num1,num2 +1)
print("La suma de los números entre", num1, "y", num2, "es", sum(suma))

if sum(suma)%2==0:
  print("La suma es par")
else:
  print("La suma es impar")