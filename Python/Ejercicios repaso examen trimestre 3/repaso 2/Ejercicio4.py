import json
config_inicial = {
  "tema": "oscuro",
  "idioma": "en",
  "autoguardado": True,
  "tamano_fuente": 14
  }

with open ("configinicial.json", "w") as f:
    json.dump(config_inicial, f)

configNueva = {}

with open ("configinicial.json", "r") as f:
    configNueva =json.load(f)
    configNueva["idioma"] = "es"

with open ("configinicial.json", "w") as f:
    json.dump(configNueva, f)