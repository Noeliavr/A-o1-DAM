import json

config_inicial = {
  "tema": "oscuro",
  "idioma": "en",
  "autoguardado": True,
  "tamano_fuente": 14
}

with open ("config_inicial.json", "w") as f:
    json.dump(config_inicial, f)

nueva_config_inicial =[]

with open ("config_inicial.json", "r") as f:
    nueva_config_inicial = json.load(f)
    nueva_config_inicial["idioma"] = "es"

with open("config_inicial.json", "w") as f:
    json.dump(nueva_config_inicial, f)