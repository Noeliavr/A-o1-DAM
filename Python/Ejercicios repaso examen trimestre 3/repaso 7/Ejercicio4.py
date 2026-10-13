
import json

config_inicial = {
  "tema": "oscuro",
  "idioma": "en",
  "autoguardado": True,
  "tamano_fuente": 14
  }

with open ("config_app.json", "w") as f:
    json.dump(config_inicial, f)

nuevaConfig_inicial =[]

with open("config_app.json", "r") as f:
    nuevaConfig_inicial = json.load(f)

    nuevaConfig_inicial ["idioma"] = "es"

with open ("config_app.json", "w") as f:
    json.dump (nuevaConfig_inicial, f)

    print(nuevaConfig_inicial)
