# Set con los gustos del usuario
gustos_usuario = {"Acción", "Sci-Fi"}

# Lista de películas (titulo, set de géneros)
peliculas = [
    ("Matrix", {"Sci-Fi"}),
    ("Titanic", {"Romance"}),
    ("Avatar", {"Acción", "Sci-Fi"})
]

# Recomendación de películas
print("Recomendaciones:")

for titulo, generos in peliculas:
    # Intersección entre gustos del usuario y géneros de la película
    if gustos_usuario & generos != set():
        print("Te puede gustar:", titulo)
