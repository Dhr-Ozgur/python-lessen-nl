# Voorbeelden – Les 3: Invoer en Uitvoer

# 1. Naam vragen
naam = input("Wat is je naam? ")
print("Hallo", naam)

# 2. Leeftijd vragen
leeftijd = input("Hoe oud ben je? ")
print("Je bent", leeftijd, "jaar oud.")

# 3. Getallen optellen
a = int(input("Voer een getal in: "))
b = int(input("Voer nog een getal in: "))
print("De som is:", a + b)

# 4. Woonplaats
stad = input("Waar woon je? ")
print("Je woont in", stad, "🌆")

# 5. Meerdere gegevens
naam = input("Wat is je naam? ")
leeftijd = input("Hoe oud ben je? ")
print("Hallo", naam + ", je bent", leeftijd, "jaar oud.")

# 6. Lengte berekenen
lengte = float(input("Wat is je lengte in meters? "))
print("Je lengte is", lengte, "m.")

# 7. Verdubbeling
getal = int(input("Voer een getal in: "))
print("Het dubbele is:", getal * 2)

# 8. Boolean input
antwoord = input("Ben je student? (ja/nee): ")
is_student = antwoord.lower() == "ja"
print("Studentstatus:", is_student)

# 9. Begroeting met f-string
naam = input("Wat is je naam? ")
print(f"Welkom bij de cursus, {naam}! 🎓")

# 10. Compleet programma
naam = input("Naam: ")
leeftijd = int(input("Leeftijd: "))
stad = input("Woonplaats: ")
print(f"{naam}, {leeftijd} jaar, woont in {stad}.")
