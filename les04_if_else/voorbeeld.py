# Voorbeelden – Les 4: If-Else Structuren

# 1. Eenvoudige if
leeftijd = 18
if leeftijd >= 18:
    print("Je bent volwassen.")

# 2. If-else
leeftijd = 16
if leeftijd >= 18:
    print("Volwassene")
else:
    print("Minderjarig")

# 3. If-elif-else
score = 85
if score >= 90:
    print("Uitstekend")
elif score >= 75:
    print("Goed")
else:
    print("Voldoende of lager")

# 4. Gelijkheid
naam = "Ozgur"
if naam == "Ozgur":
    print("Welkom terug!")

# 5. Meerdere condities
leeftijd = 25
student = True
if leeftijd < 30 and student:
    print("Jonge student!")

# 6. OR
dag = "zaterdag"
if dag == "zaterdag" or dag == "zondag":
    print("Het is weekend!")

# 7. NOT
regent = False
if not regent:
    print("Het is droog buiten ☀️")

# 8. Geneste if
leeftijd = 20
if leeftijd >= 18:
    print("Volwassene")
    if leeftijd < 21:
        print("Maar nog geen 21!")

# 9. F-string inline if
naam = "Emma"
leeftijd = 17
print(f"{naam} is {'volwassen' if leeftijd >= 18 else 'minderjarig'}.")

# 10. Complex voorbeeld
punt = 78
geslaagd = punt >= 55
if geslaagd:
    print("Gefeliciteerd, je bent geslaagd!")
else:
    print("Helaas, probeer opnieuw.")
