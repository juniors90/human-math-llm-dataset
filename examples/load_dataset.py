import json
from pathlib import Path

# ruta a este archivo
base_path = Path(__file__).resolve().parent

# ../data/train.jsonl
data_path = base_path.parent / "data" / "train.jsonl"

data = []
with open(data_path, "r", encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        if line:  # ignora líneas vacías
            data.append(json.loads(line))

print("Cantidad de ejemplos:", len(data))
print("\nPrimer problema:\n", data[0]["problem"])
print("\nPrimera solución:\n", data[0]["solution"])
print("\n-----------------------------------------------")
print("\nPrimer problema:\n", data[11]["problem"])
print("\nPrimera solución:\n", data[11]["solution"])
