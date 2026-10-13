texto = input("Escribe un texto aquí: ")
textodividido = texto.split()
lista = []
palabras_unicas = set (lista)
print("Palabras únicas: ", palabras_unicas)

cantidad = (len(lista), lista[0], lista [-1])

print("Cantidad de palabras:", cantidad[0])
print("Primera palabra:", cantidad[1])
print("Última palabra:", cantidad[2])