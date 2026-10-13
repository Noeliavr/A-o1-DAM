numero =[4, 2, 5, 1, 3]
print(numero)
numero.insert(0,0)
print(numero)
numero.sort()
print(numero)
medio = (len(numero) //2)-1
del numero[medio]
print(numero)