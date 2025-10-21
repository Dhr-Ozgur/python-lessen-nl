# 📖 Les 7 – Dictionaries (Woordenboeken)

Welkom bij les 7 van de **Python Lessenreeks**!  
In deze les leer je werken met **dictionaries** – verzamelingen van sleutel–waardeparen (key–value pairs).  

---

## 🎯 Leerdoelen
- Dictionaries maken en gebruiken  
- Waarden opzoeken via sleutels  
- Items toevoegen en verwijderen  
- Itereren over keys, values en items  
- Geneste dictionaries gebruiken  

---

## 💻 Voorbeelden

### Voorbeeld 1 – Een dictionary maken
```python
persoon = {"naam": "Ozgur", "leeftijd": 30, "stad": "Amsterdam"}
print(persoon)
```

### Voorbeeld 2 – Een waarde ophalen
```python
print(persoon["naam"])
```

### Voorbeeld 3 – Een nieuwe key toevoegen
```python
persoon["hobby"] = "programmeren"
print(persoon)
```

### Voorbeeld 4 – Een waarde wijzigen
```python
persoon["stad"] = "Rotterdam"
print(persoon)
```

### Voorbeeld 5 – Een key verwijderen
```python
del persoon["leeftijd"]
print(persoon)
```

### Voorbeeld 6 – Itereren over keys
```python
for sleutel in persoon:
    print("Sleutel:", sleutel)
```

### Voorbeeld 7 – Itereren over values
```python
for waarde in persoon.values():
    print("Waarde:", waarde)
```

### Voorbeeld 8 – Itereren over items
```python
for sleutel, waarde in persoon.items():
    print(sleutel, "=", waarde)
```

### Voorbeeld 9 – Checken of key bestaat
```python
if "naam" in persoon:
    print("Naam bestaat in de dictionary.")
```

### Voorbeeld 10 – Geneste dictionary
```python
studenten = {
    "s1": {"naam": "Emma", "leeftijd": 22},
    "s2": {"naam": "Ozgur", "leeftijd": 30}
}
print(studenten["s1"]["naam"])
```

---

## 🧠 Uitleg
Een **dictionary** in Python is een verzameling van sleutel–waardeparen.  
Je gebruikt `{}` om ze te definiëren.  
Je kunt waarden opzoeken via hun sleutel (`dict["key"]`) en ze aanpassen.  
Met `.items()`, `.keys()` en `.values()` kun je gemakkelijk over dictionaries itereren.

---

## 🧩 Opdrachten
Zie `opdrachten.md` voor 10 oefeningen over dictionaries.

---

## ✅ Oplossingen
Bekijk `oplossingen.py` voor de uitwerkingen.
