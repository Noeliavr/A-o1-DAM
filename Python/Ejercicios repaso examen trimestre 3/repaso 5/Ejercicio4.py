import json

config_inicial = {
  "tema": "oscuro",
  "idioma": "en",
  "autoguardado": True,
  "tamano_fuente": 14
  }

with open("config.json", "w") as f:
    json.dump(config_inicial, f)

nuevaconfig = {}
with open("config.json", "r") as f:
    nuevaconfig = json.load(f)

    nuevaconfig["idioma"] = "es"

with open("config.json", "w") as f:
    json.dump(nuevaconfig, f)
