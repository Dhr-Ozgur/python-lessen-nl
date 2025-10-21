# Voorbeelden – Les 16: CSV-bestanden

import csv

# 1. CSV lezen
with open("gegevens.csv", "r") as f:
    reader = csv.reader(f)
    for rij in reader:
        print(rij)

# 2. CSV met header
with open("gegevens.csv", "r") as f:
    reader = csv.DictReader(f)
    for rij in reader:
        print(rij["Naam"], "-", rij["Leeftijd"])

# 3. Schrijven naar CSV
with open("nieuw.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Naam", "Leeftijd", "Stad"])
    writer.writerow(["Ozgur", 30, "Amsterdam"])
    writer.writerow(["Emma", 25, "Rotterdam"])

# 4. DictWriter
velden = ["Naam", "Leeftijd", "Stad"]
with open("mensen.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=velden)
    writer.writeheader()
    writer.writerow({"Naam": "Lars", "Leeftijd": 40, "Stad": "Utrecht"})

# 5. DictReader
with open("mensen.csv", "r") as f:
    reader = csv.DictReader(f)
    for persoon in reader:
        print(persoon)

# 6. Aantal rijen tellen
with open("mensen.csv", "r") as f:
    reader = csv.reader(f)
    print("Aantal rijen:", len(list(reader)))

# 7. Rij toevoegen
with open("mensen.csv", "a", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Sara", 29, "Eindhoven"])

# 8. CSV naar lijst
with open("mensen.csv", "r") as f:
    reader = csv.DictReader(f)
    data = list(reader)
print(data)

# 9. Filteren
with open("mensen.csv", "r") as f:
    reader = csv.DictReader(f)
    for r in reader:
        if int(r["Leeftijd"]) > 30:
            print(r["Naam"], "is ouder dan 30")

# 10. Foutafhandeling
try:
    with open("fout.csv", "r") as f:
        reader = csv.reader(f)
        for rij in reader:
            print(rij)
except FileNotFoundError:
    print("Bestand niet gevonden!")
