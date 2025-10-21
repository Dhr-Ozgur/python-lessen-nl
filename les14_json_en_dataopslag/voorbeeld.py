# Voorbeelden – Les 14: JSON en Data-opslag

import json

# 1. Dict naar JSON-string
persoon = {"naam": "Ozgur", "leeftijd": 30, "stad": "Amsterdam"}
print(json.dumps(persoon))

# 2. JSON-string naar dict
json_str = '{"naam": "Ozgur", "leeftijd": 30}'
data = json.loads(json_str)
print(data["naam"])

# 3. Schrijven naar JSON-bestand
with open("data.json", "w") as f:
    json.dump(persoon, f)

# 4. Lezen uit JSON-bestand
with open("data.json", "r") as f:
    data = json.load(f)
print(data)

# 5. Mooie indeling
print(json.dumps(data, indent=4))

# 6. Lijst van dictionaries
personen = [
    {"naam": "Ozgur", "leeftijd": 30},
    {"naam": "Emma", "leeftijd": 25}
]
with open("personen.json", "w") as f:
    json.dump(personen, f, indent=2)

# 7. Itereren
with open("personen.json", "r") as f:
    mensen = json.load(f)
for p in mensen:
    print(p["naam"], "-", p["leeftijd"])

# 8. Foutafhandeling
try:
    with open("fout.json", "r") as f:
        data = json.load(f)
except json.JSONDecodeError:
    print("Ongeldige JSON!")

# 9. Conversie test
d = {"x": 5, "y": 10}
s = json.dumps(d)
print(json.loads(s))

# 10. Geneste JSON
complex_data = {
    "gebruiker": {
        "naam": "Ozgur",
        "interesses": ["Python", "AI", "Muziek"],
        "actief": True
    }
}
print(json.dumps(complex_data, indent=4))
