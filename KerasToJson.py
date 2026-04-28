import zipfile
import json

with zipfile.ZipFile("model.keras", "r") as z:
     z.extractall("modelo_extraido")

# print(config)