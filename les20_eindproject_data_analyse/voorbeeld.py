# Voorbeeld – Les 20: Mini Data Analyse Eindproject

import csv
import json
import matplotlib.pyplot as plt

# 1. Data lezen uit CSV
studenten = []
with open("studenten.csv", "r") as f:
    reader = csv.DictReader(f)
    for rij in reader:
        studenten.append(rij)

# 2. Opslaan als JSON
with open("studenten.json", "w") as f:
    json.dump(studenten, f, indent=4)

# 3. Eenvoudige analyse
scores = [int(s["Score"]) for s in studenten]
gemiddelde = sum(scores) / len(scores)
max_score = max(scores)
min_score = min(scores)
print("Gemiddelde:", gemiddelde)
print("Hoogste:", max_score)
print("Laagste:", min_score)

# 4. Visualisatie: staafdiagram
namen = [s["Naam"] for s in studenten]
plt.bar(namen, scores, color="green")
plt.title("Scores per student")
plt.ylabel("Score")
plt.show()

# 5. Cirkeldiagram
plt.pie(scores, labels=namen, autopct="%1.1f%%")
plt.title("Scoreverdeling per student")
plt.show()

# 6. Data opslaan in JSON met extra statistieken
resultaat = {
    "gemiddelde": gemiddelde,
    "hoogste": max_score,
    "laagste": min_score
}
with open("analyse_resultaat.json", "w") as f:
    json.dump(resultaat, f, indent=4)

print("Analyse voltooid en opgeslagen.")
