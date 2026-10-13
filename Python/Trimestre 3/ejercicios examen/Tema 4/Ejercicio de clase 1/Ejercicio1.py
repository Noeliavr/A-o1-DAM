class Libro:
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
    
    def resumen(self):
        print(f"{self.titulo} - {self.autor} ({self.paginas})")

libro1 = Libro("hola", "Mi vida", 800)
libro2 = Libro ("Te", "Amo", "2990")
libro3 = Libro ("sii", "Noo", "20")
Libros =[libro1, libro2, libro3]

for Libross in Libros:
    print(Libro.resumen(Libross))
