
Estudiante1= {
  "nombre " : input ("Escribe tu nombre: "),
  "Edad " : int(input("Escribe tu edad")),
  "Nota " : float(input("Escribe tu nota"))
}

Estudiante2= {
  "nombre " : input ("Escribe tu nombre: "),
  "Edad " : int(input("Escribe tu edad")),
  "Nota " : float(input("Escribe tu nota"))
}

Estudiante3= {
  "nombre " : input ("Escribe tu nombre: "),
  "Edad " : int(input("Escribe tu edad")),
  "Nota " : float(input("Escribe tu nota"))
}

Estudiantes = [Estudiante1, Estudiante2, Estudiante3]

print ("Lista de estudiantes: ")
for estudiante in Estudiantes:
  print(estudiante)

suma = 0
for estudiante in Estudiantes:
  suma += estudiante ["nota"]

  promedio = suma / len(Estudiantes)

  print ("Promedio de las tres notas: ", promedio)
  