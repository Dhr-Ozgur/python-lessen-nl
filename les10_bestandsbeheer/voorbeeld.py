# Voorbeelden – Les 10: Bestandsbeheer

# 1. Bestand lezen
bestand = open("voorbeeld.txt", "r")
inhoud = bestand.read()
print(inhoud)
bestand.close()

# 2. Met 'with' lezen
with open("voorbeeld.txt", "r") as f:
    print(f.read())

# 3. Eén regel lezen
with open("voorbeeld.txt", "r") as f:
    print(f.readline())

# 4. Regels als lijst
with open("voorbeeld.txt", "r") as f:
    regels = f.readlines()
print(regels)

# 5. Schrijven naar bestand
with open("nieuw.txt", "w") as f:
    f.write("Hallo wereld!\n")
    f.write("Dit is een test.")

# 6. Toevoegen aan bestaand bestand
with open("nieuw.txt", "a") as f:
    f.write("\nNog een regel.")

# 7. Lijst schrijven
regels = ["Regel 1\n", "Regel 2\n", "Regel 3\n"]
with open("lijst.txt", "w") as f:
    f.writelines(regels)

# 8. Regels tellen
with open("lijst.txt", "r") as f:
    inhoud = f.readlines()
print("Aantal regels:", len(inhoud))

# 9. Bestand niet gevonden
try:
    with open("fout.txt", "r") as f:
        print(f.read())
except FileNotFoundError:
    print("Bestand niet gevonden!")

# 10. Bewerken en herschrijven
with open("data.txt", "w") as f:
    f.write("Python is leuk!\n")
with open("data.txt", "r+") as f:
    tekst = f.read()
    f.write("\nJa, echt waar!")
