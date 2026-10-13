# 1. Set con los géneros preferidos del usuario
gustos_usuario = {"Acción", "Sci-Fi"}

# 2. Lista de tuplas (título, set de géneros)
peliculas = [
    ("Matrix", {"Sci-Fi"}),
    ("Titanic", {"Romance"}),
    ("Avatar", {"Acción", "Sci-Fi"})
]

# 3. Filtrar películas que tengan al menos un género en común
recomendaciones = []

for titulo, generos in peliculas:
    if gustos_usuario & generos != set():
        recomendaciones.append(titulo)

# Reto opcional: ordenar alfabéticamente
recomendaciones.sort()

# Mostrar resultados
for pelicula in recomendaciones:
    print(f"Te puede gustar: {pelicula}")
