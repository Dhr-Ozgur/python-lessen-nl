# ✅ Oplossingen – Les 10: Bestandsbeheer

# 1. Bestand schrijven
with open("test.txt", "w") as f:
    f.write("Dit is een testbestand.\n")

# 2. Bestand lezen
with open("test.txt", "r") as f:
    print(f.read())

# 3. Regel toevoegen
with open("test.txt", "a") as f:
    f.write("Nog een regel toegevoegd.\n")

# 4. Regels genummerd lezen
with open("test.txt", "r") as f:
    for i, regel in enumerate(f, start=1):
        print(i, regel.strip())

# 5. Aantal regels tellen
with open("test.txt", "r") as f:
    regels = f.readlines()
print("Aantal regels:", len(regels))

# 6. Lijst schrijven
regels = ["Eerste regel\n", "Tweede regel\n", "Derde regel\n"]
with open("lijst.txt", "w") as f:
    f.writelines(regels)

# 7. Woorden tellen per regel
with open("lijst.txt", "r") as f:
    for regel in f:
        print(len(regel.split()), "woorden:", regel.strip())

# 8. Try/except foutafhandeling
try:
    with open("onbestaand.txt", "r") as f:
        print(f.read())
except FileNotFoundError:
    print("Bestand niet gevonden!")

# 9. r+ lezen en schrijven
with open("test.txt", "r+") as f:
    inhoud = f.read()
    f.write("\nToegevoegde tekst via r+ mode.")

# 10. Bestand kopiëren
with open("test.txt", "r") as bron, open("kopie.txt", "w") as doel:
    for regel in bron:
        doel.write(regel)
print("Bestand succesvol gekopieerd!")
