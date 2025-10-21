# 🗂️ Les 14 – JSON en Data-opslag

Welkom bij les 14 van de **Python Lessenreeks**!  
In deze les leer je werken met **JSON (JavaScript Object Notation)**, een veelgebruikt formaat voor het opslaan en uitwisselen van gegevens.  

---

## 🎯 Leerdoelen
- JSON-bestanden lezen en schrijven  
- Python-structuren (dict, list) omzetten naar JSON  
- JSON omzetten naar Python-objecten  
- `json.load()`, `json.dump()`, `json.loads()`, `json.dumps()` gebruiken  
- JSON gebruiken in combinatie met foutafhandeling  

---

## 💻 Voorbeelden

### Voorbeeld 1 – Dictionary naar JSON-string
```python
import json
persoon = {"naam": "Ozgur", "leeftijd": 30, "stad": "Amsterdam"}
json_data = json.dumps(persoon)
print(json_data)
```

### Voorbeeld 2 – JSON-string naar dict
```python
python_data = json.loads(json_data)
print(python_data["naam"])
```

### Voorbeeld 3 – JSON schrijven naar bestand
```python
with open("data.json", "w") as f:
    json.dump(persoon, f)
```

### Voorbeeld 4 – JSON lezen uit bestand
```python
with open("data.json", "r") as f:
    data = json.load(f)
print(data)
```

### Voorbeeld 5 – Mooie JSON (indent)
```python
print(json.dumps(persoon, indent=4))
```

### Voorbeeld 6 – Lijst van dictionaries
```python
personen = [
    {"naam": "Ozgur", "leeftijd": 30},
    {"naam": "Emma", "leeftijd": 25}
]
with open("personen.json", "w") as f:
    json.dump(personen, f, indent=2)
```

### Voorbeeld 7 – JSON lezen en itereren
```python
with open("personen.json", "r") as f:
    mensen = json.load(f)
for p in mensen:
    print(p["naam"], "-", p["leeftijd"])
```

### Voorbeeld 8 – JSON met try/except
```python
try:
    with open("fout.json", "r") as f:
        data = json.load(f)
except json.JSONDecodeError:
    print("Ongeldige JSON-structuur!")
```

### Voorbeeld 9 – Data converteren
```python
python_dict = {"a": 1, "b": 2}
json_str = json.dumps(python_dict)
nieuw_dict = json.loads(json_str)
print(nieuw_dict)
```

### Voorbeeld 10 – Complexe geneste JSON
```python
data = {
    "student": {
        "naam": "Ozgur",
        "scores": [85, 90, 78],
        "actief": True
    }
}
print(json.dumps(data, indent=4))
```

---

## 🧠 Uitleg
- **`json.dumps()`** → Python → JSON-string  
- **`json.loads()`** → JSON-string → Python  
- **`json.dump()`** → Python → JSON-bestand  
- **`json.load()`** → JSON-bestand → Python  
- JSON ondersteunt strings, nummers, lijsten, dictionaries, `true/false` en `null`.  

---

## 🧩 Opdrachten
Zie `opdrachten.md` voor 10 oefeningen met JSON en data-opslag.

---

## ✅ Oplossingen
Bekijk `oplossingen.py` voor de uitgewerkte antwoorden.
