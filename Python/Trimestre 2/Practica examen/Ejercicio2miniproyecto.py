gustos_usuario = {"Acción", "Sci-Fi"}

peliculas = [
    ("Matrix", {"Sci-Fi"}),
    ("Titanic", {"Romance"}),
    ("Avatar", {"Acción", "Sci-Fi"})
]

recomendaciones =[]

for titulos, generos in peliculas:
    if gustos_usuario & generos != set():
        recomendaciones.append(titulos)

for titulos in sorted(recomendaciones):
    print("Te podría gustar las siguientes peliculas: ", titulos)