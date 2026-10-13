import sqlite3
conn = sqlite3.connect("biblioteca.db")
cursor =conn.cursor()
cursor.execute("""
create table if not exist libros(
              id integer primary key autoincrement,
              unique titulo text,
              unique autor text,
              anio integer
              )

""")
conn.commit()
libros_nuevos = [
    ("El Quijote", "Cervantes", 1605),
    ("Cien años de soledad", "García Márquez", 1967),
    ("La sombra del viento", "Zafón", 2001),
]
for libro in libros_nuevos:
  try:
    cursor.execute(
      "insert into libros (titulo, autor, anio) values (?, ?, ?)", (libro)
    )
  except sqlite3.OperationalError:
    f"El libro no existe devido al UNIQUE"
    conn.commit()
conn.close()