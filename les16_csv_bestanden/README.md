# 📊 Les 16 – Bestandsverwerking met CSV (Comma-Separated Values)

Welkom bij les 16 van de **Python Lessenreeks**!  
In deze les leer je werken met **CSV-bestanden**: tekstbestanden waarin gegevens in tabelvorm zijn opgeslagen, gescheiden door komma’s.  
We gebruiken hiervoor de ingebouwde Python-module `csv`.

---

## 🎯 Leerdoelen
- CSV-bestanden openen en lezen  
- Gegevens schrijven naar CSV  
- Kopteksten (headers) gebruiken  
- De functies `csv.reader`, `csv.writer`, `csv.DictReader`, `csv.DictWriter` begrijpen  
- Werken met lijsten en dictionaries in CSV-formaten  

---

## 💻 Voorbeelden

### Voorbeeld 1 – Een CSV-bestand lezen
```python
import csv
with open("gegevens.csv", "r") as f:
    reader = csv.reader(f)
    for rij in reader:
        print(rij)
```

### Voorbeeld 2 – CSV-bestand met header
```python
with open("gegevens.csv", "r") as f:
    reader = csv.DictReader(f)
    for rij in reader:
        print(rij["Naam"], "-", rij["Leeftijd"])
```

### Voorbeeld 3 – CSV-bestand schrijven
```python
with open("nieuw.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Naam", "Leeftijd", "Stad"])
    writer.writerow(["Ozgur", 30, "Amsterdam"])
    writer.writerow(["Emma", 25, "Rotterdam"])
```

### Voorbeeld 4 – CSV-bestand schrijven met DictWriter
```python
velden = ["Naam", "Leeftijd", "Stad"]
with open("mensen.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=velden)
    writer.writeheader()
    writer.writerow({"Naam": "Lars", "Leeftijd": 40, "Stad": "Utrecht"})
```

### Voorbeeld 5 – Lezen van DictWriter-bestand
```python
with open("mensen.csv", "r") as f:
    reader = csv.DictReader(f)
    for persoon in reader:
        print(persoon)
```

### Voorbeeld 6 – Aantal rijen tellen
```python
with open("mensen.csv", "r") as f:
    reader = csv.reader(f)
    print("Aantal rijen:", len(list(reader)))
```

### Voorbeeld 7 – Rij toevoegen (append)
```python
with open("mensen.csv", "a", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Sara", 29, "Eindhoven"])
```

### Voorbeeld 8 – CSV naar lijst converteren
```python
with open("mensen.csv", "r") as f:
    reader = csv.DictReader(f)
    data = list(reader)
print(data)
```

### Voorbeeld 9 – Filteren van data
```python
with open("mensen.csv", "r") as f:
    reader = csv.DictReader(f)
    for r in reader:
        if int(r["Leeftijd"]) > 30:
            print(r["Naam"], "is ouder dan 30")
```

### Voorbeeld 10 – CSV inlezen met foutafhandeling
```python
try:
    with open("fout.csv", "r") as f:
        reader = csv.reader(f)
        for rij in reader:
            print(rij)
except FileNotFoundError:
    print("CSV-bestand niet gevonden!")
```

---

## 🧠 Uitleg
- **`csv.reader()`** → leest CSV-gegevens als lijsten  
- **`csv.writer()`** → schrijft lijsten naar CSV  
- **`csv.DictReader()`** → leest CSV als dictionaries  
- **`csv.DictWriter()`** → schrijft CSV met kolomnamen  
- Gebruik `newline=""` om lege regels te voorkomen bij schrijven.  

---

## 🧩 Opdrachten
Zie `opdrachten.md` voor 10 oefeningen met CSV-bestanden.

---

## ✅ Oplossingen
Bekijk `oplossingen.py` voor de uitgewerkte antwoorden.
