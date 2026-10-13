import json

datos_contactos = [
  { "nombre": "Ana", "telefono": "600111222", "favorito": True },
  { "nombre": "Luis", "telefono": "600333444", "favorito": False },
  { "nombre": "Marta", "telefono": "600555666", "favorito": True },
  { "nombre": "Alberto", "telefono": "600777888", "favorito": True }
]

with open ("contactos.json", "w") as f:
    json.dump(datos_contactos, f)

with open ("contactos.json", "r") as f:
    datos_contactos = json.load(f)
    for d in datos_contactos:
        if d["favorito"] == True:
            print (d)