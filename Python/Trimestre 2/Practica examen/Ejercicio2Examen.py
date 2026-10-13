Estudiante1 ={
    "Nombre": input("Escribe tu nombre: "),
    "Edad": int(input("Escribe tu edad: ")),
    "Nota": float(input("Escribe tu nota: "))
}
Estudiante2 ={
    "Nombre": input("Escribe tu nombre:  "),
    "Edad": int(input("Escribe tu edad:  ")),
    "Nota": float(input("Escribe tu nota:  "))
}
Estudiante3 ={
    "Nombre": input("Escribe tu nombre: "),
    "Edad": int(input("Escribe tu edad: ")),
    "Nota": float(input("Escribe tu nota: "))
}
lista = [Estudiante1, Estudiante2, Estudiante3]
print("Lista de estudiantes: ")
for estudiante in lista:
    print(estudiante)

suma = 0
for estudiante in lista:
    suma += estudiante ["Nota"]
promedio = suma / len(lista)
print("Este es el promedio: ", promedio)
