set1 = set(lista1)
set2 = set(lista2)

print(set1)
print(set2)


comunes = set1 & set2
print("Comunes:", comunes)



solo_lista1 = set1 - set2
print("Solo en lista1:", solo_lista1)



union = set1 | set2
print("Unión:", union)



cantidad = len(union)
print("Cantidad de números únicos:", cantidad)
