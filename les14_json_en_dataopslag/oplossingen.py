# ✅ Oplossingen – Les 14: JSON en Data-opslag

import json
import datetime

# 1. Dict naar JSON
persoon = {"naam": "Ozgur", "leeftijd": 30, "stad": "Amsterdam"}
print(json.dumps(persoon))

# 2. JSON-string naar dict
json_str = '{"naam": "Ozgur", "leeftijd": 30}'
data = json.loads(json_str)
print(data)

# 3. Schrijven naar bestand
with open("persoon.json", "w") as f:
    json.dump(persoon, f)

# 4. Lezen uit bestand
with open("persoon.json", "r") as f:
    gelezen = json.load(f)
print(gelezen)

# 5. Lijst schrijven
personen = [
    {"naam": "Ozgur", "leeftijd": 30},
    {"naam": "Emma", "leeftijd": 25},
    {"naam": "Lars", "leeftijd": 40}
]
with open("personen.json", "w") as f:
    json.dump(personen, f, indent=4)

# 6. Lijst lezen
with open("personen.json", "r") as f:
    mensen = json.load(f)
for p in mensen:
    print(p["naam"])

# 7. Mooi geformatteerd printen
print(json.dumps(mensen, indent=4))

# 8. Ongeldige JSON afvangen
try:
    with open("fout.json", "r") as f:
        json.load(f)
except json.JSONDecodeError:
    print("Ongeldige JSON-structuur!")

# 9. Geneste dict
student = {
    "naam": "Ozgur",
    "scores": [85, 90, 78],
    "actief": True
}
print(json.dumps(student, indent=4))

# 10. Datum toevoegen
data_met_datum = {
    "naam": "Ozgur",
    "datum": datetime.date.today().isoformat()
}
print(json.dumps(data_met_datum, indent=4))
