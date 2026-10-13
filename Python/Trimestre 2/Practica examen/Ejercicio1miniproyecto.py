posts = [
{"user": "ana", "likes":10},
{"user": "juan", "likes": 55},
{"user": "ana", "likes": 30}
]
total_posts = (len(posts))
print ("Total posts: ",total_posts)
for post in posts:
    print(f"usuario: {post['user']} - likes: {post['likes']}")


likesAna = 0

for post in posts:
    if post["user"] == "ana":
        likesAna += post["likes"]
print ("Total de likes de Ana es: ", likesAna)

likesJuan = 0
for post in posts:
    if post["user"]== "juan":
        likesJuan +=post ["likes"]


print ("Resumen de likes por usuario: ")
print("------------------------------")
print("Ana: ",likesAna," likes")
print("Juan: ",likesJuan," likes")