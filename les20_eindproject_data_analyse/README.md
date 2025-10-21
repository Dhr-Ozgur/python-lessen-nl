# 🎓 Les 20 – Eindproject: Mini Data Analyse met Python (JSON, CSV & Visualisatie)

Welkom bij **de laatste les van de Python Lessenreeks**! 🐍  
In dit eindproject combineer je **alles wat je hebt geleerd** — van bestandsbeheer tot data-analyse en visualisatie.

We gaan een mini-analyse uitvoeren op fictieve studentenresultaten.  
De data komt uit een CSV-bestand en wordt omgezet naar JSON.  
Daarna maken we enkele grafieken met `matplotlib`.

---

## 🎯 Leerdoelen
- Data inlezen uit CSV-bestanden  
- Data converteren naar JSON  
- Eenvoudige analyses uitvoeren (gemiddelde, hoogste score, aantal studenten)  
- Resultaten visualiseren in grafieken  
- Eindresultaten opslaan  

---

## 📊 Dataset
CSV-bestand: `studenten.csv`

| Naam | Leeftijd | Score |
|------|-----------|--------|
| Ozgur | 30 | 85 |
| Emma | 25 | 90 |
| Lars | 40 | 78 |
| Sara | 29 | 95 |
| Tom | 33 | 88 |

---

## 💻 Voorbeeldcode
```python
import csv
import json
import matplotlib.pyplot as plt

# 1. CSV lezen
studenten = []
with open("studenten.csv", "r") as f:
    reader = csv.DictReader(f)
    for rij in reader:
        studenten.append(rij)

# 2. Omzetten naar JSON
with open("studenten.json", "w") as f:
    json.dump(studenten, f, indent=4)

# 3. Analyse
scores = [int(s["Score"]) for s in studenten]
gemiddelde = sum(scores) / len(scores)
print("Gemiddelde score:", gemiddelde)

# 4. Visualisatie
namen = [s["Naam"] for s in studenten]
plt.bar(namen, scores, color="skyblue")
plt.title("Scores per student")
plt.ylabel("Score")
plt.show()
```

---

## 🧠 Uitleg
- Combineert **CSV, JSON en Matplotlib**  
- Analyse: berekent gemiddelde en toont scores  
- Visualisatie: grafische weergave van data  
- Dit project is een mini-versie van echte data-analyse  

---

## 🧩 Opdrachten
Zie `opdrachten.md` voor 10 uitdagende projectopdrachten.

---

## ✅ Oplossingen
Bekijk `oplossingen.py` voor de uitgewerkte eindoplossing.
