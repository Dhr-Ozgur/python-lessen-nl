# ✅ Oplossingen – Les 16: CSV-bestanden

import csv

# 1. CSV aanmaken
with open("personen.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Naam", "Leeftijd", "Stad"])
    writer.writerow(["Ozgur", 30, "Amsterdam"])
    writer.writerow(["Emma", 25, "Rotterdam"])

# 2. Lezen en printen
with open("personen.csv", "r") as f:
    reader = csv.reader(f)
    for rij in reader:
        print(rij)

# 3. DictReader
with open("personen.csv", "r") as f:
    reader = csv.DictReader(f)
    for rij in reader:
        print(rij["Naam"])

# 4. Rij toevoegen
with open("personen.csv", "a", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Lars", 40, "Utrecht"])

# 5. Rijen tellen
with open("personen.csv", "r") as f:
    reader = csv.reader(f)
    print("Aantal rijen:", len(list(reader)))

# 6. DictWriter
velden = ["Naam", "Leeftijd", "Stad"]
with open("nieuw_bestand.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=velden)
    writer.writeheader()
    writer.writerow({"Naam": "Sara", "Leeftijd": 29, "Stad": "Eindhoven"})

# 7. Data als lijst
with open("personen.csv", "r") as f:
    reader = csv.DictReader(f)
    data = list(reader)
print(data)

# 8. Filteren
for persoon in data:
    if int(persoon["Leeftijd"]) > 30:
        print(persoon["Naam"], "is ouder dan 30")

# 9. Foutafhandeling
try:
    with open("fout.csv", "r") as f:
        reader = csv.reader(f)
        print(list(reader))
except FileNotFoundError:
    print("CSV-bestand niet gevonden!")

# 10. Kopie maken
with open("personen.csv", "r") as bron, open("backup.csv", "w", newline="") as doel:
    for regel in bron:
        doel.write(regel)
print("Backup succesvol aangemaakt.")
