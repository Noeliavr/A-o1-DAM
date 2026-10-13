# Lista de publicaciones
posts = [
    {"user": "ana", "likes": 10},
    {"user": "juan", "likes": 55},
    {"user": "ana", "likes": 30}
]

# 1. Mostrar cuántos posts hay en total
print("Total de posts:", len(posts))
print()

# 2. Recorrer e imprimir cada post
print("Listado de publicaciones:")
for post in posts:
    print(f"usuario: {post['user']} - likes: {post['likes']}")

print()

# 3. Contar likes totales por usuario
likes_por_usuario = {}

for post in posts:
    usuario = post["user"]
    likes = post["likes"]

    # Si el usuario no existe aún, se inicializa
    if usuario not in likes_por_usuario:
        likes_por_usuario[usuario] = 0

    # Se suman los likes
    likes_por_usuario[usuario] += likes

# 4. Mostrar resumen
print("Resumen de likes por usuario:")
print("------------------------------")

for usuario, total_likes in likes_por_usuario.items():
    print(f"{usuario}: {total_likes} likes")

print()

# ================================
# RETO OPCIONAL
# ================================

usuario_mas_popular = ""
max_likes = 0

for usuario, total_likes in likes_por_usuario.items():
    if total_likes > max_likes:
        max_likes = total_likes
        usuario_mas_popular = usuario

print("Usuario más popular:", usuario_mas_popular, "con", max_likes, "likes totales")
print("=" * 50)

