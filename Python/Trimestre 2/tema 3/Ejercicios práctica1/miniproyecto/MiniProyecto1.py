posts = [
  {"user": "Ana", "likes":10},
  {"user": "Juan", "likes":55},
  {"user": "Ana", "likes":30}
]
print(len(posts))
#Recorrer todos los posts e imprimir cada uno en el siguiente formato: usuario: ana - likes: 10
for post in posts:
  print("usuario: ", post["user"], "- likes: ", post["likes"])
  #Contar los likes totales que tiene Ana.
  likesAna = 0  # ← aquí inicializas el contador

for post in posts:
    if post["user"] == "Ana":
        likesAna += post["likes"]



print("Total de likes de ana:", likesAna)

posts = [
    {"user": "ana", "likes": 10},
    {"user": "juan", "likes": 55},
    {"user": "ana", "likes": 30}
]

resumen = {}

for post in posts:
    usuario = post["user"]
    likes = post["likes"]
    
    if usuario not in resumen:
        resumen[usuario] = 0
    
    resumen[usuario] += likes

print("Resumen de likes por usuario:")
print("------------------------------")

for usuario in resumen:
    print(f"{usuario}: {resumen[usuario]} likes")