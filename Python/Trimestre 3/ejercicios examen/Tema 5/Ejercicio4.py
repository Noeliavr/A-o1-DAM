import json

config_inicial = {
    "tema": "oscuro",
    "idioma": "en",
    "autoguardado": True,
    "tamano_fuente": 14
}

with open("config_app.json", "w") as archivo:
    json.dump(config_inicial, archivo)

with open("config_app.json", "r") as archivo:
    config = json.load(archivo)

config["idioma"] = "es"

with open("config_app.json", "w") as archivo:
    json.dump(config, archivo)

print("Configuración actualizada:")
print(config) 