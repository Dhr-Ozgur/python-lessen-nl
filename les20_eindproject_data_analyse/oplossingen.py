# ✅ Oplossingen – Les 20: Eindproject Mini Data Analyse

import csv
import json
import matplotlib.pyplot as plt

# 1. CSV aanmaken (optioneel)
with open("studenten.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Naam", "Leeftijd", "Score"])
    writer.writerow(["Ozgur", 30, 85])
    writer.writerow(["Emma", 25, 90])
    writer.writerow(["Lars", 40, 78])
    writer.writerow(["Sara", 29, 95])
    writer.writerow(["Tom", 33, 88])

# 2. CSV lezen
studenten = []
with open("studenten.csv", "r") as f:
    reader = csv.DictReader(f)
    for rij in reader:
        studenten.append(rij)

# 3. Naar JSON schrijven
with open("studenten.json", "w") as f:
    json.dump(studenten, f, indent=4)

# 4. Analyse
scores = [int(s["Score"]) for s in studenten]
gemiddelde = sum(scores) / len(scores)
max_score = max(scores)
min_score = min(scores)
ouder_dan_30 = [s for s in studenten if int(s["Leeftijd"]) > 30]
print("Gemiddelde score:", gemiddelde)
print("Hoogste score:", max_score)
print("Laagste score:", min_score)
print("Studenten ouder dan 30:", len(ouder_dan_30))

# 5. Staafdiagram
namen = [s["Naam"] for s in studenten]
plt.bar(namen, scores, color="skyblue")
plt.title("Scores per student")
plt.ylabel("Score")
plt.show()

# 6. Cirkeldiagram
plt.pie(scores, labels=namen, autopct="%1.1f%%")
plt.title("Scoreverdeling")
plt.show()

# 7. Resultaat opslaan
resultaat = {
    "gemiddelde": gemiddelde,
    "hoogste": max_score,
    "laagste": min_score,
    "studenten_ouder_dan_30": len(ouder_dan_30)
}
with open("analyse_resultaat.json", "w") as f:
    json.dump(resultaat, f, indent=4)

print("Eindanalyse opgeslagen in analyse_resultaat.json ✅")
