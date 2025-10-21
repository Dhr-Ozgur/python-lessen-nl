# ✅ Oplossingen – Les 4: If-Else Structuren

# 1. Leeftijd
leeftijd = int(input("Hoe oud ben je? "))
if leeftijd >= 18:
    print("Je bent volwassen.")
else:
    print("Je bent minderjarig.")

# 2. Cijfer
cijfer = int(input("Wat is je cijfer? "))
if cijfer >= 55:
    print("Voldoende!")
else:
    print("Onvoldoende.")

# 3. Naam
naam = input("Wat is je naam? ")
if naam == "Ozgur":
    print("Welkom terug, Ozgur!")
else:
    print("Hallo", naam)

# 4. Dag
dag = input("Welke dag is het? ").lower()
if dag == "zaterdag" or dag == "zondag":
    print("Weekend! 🎉")
else:
    print("Werkdag 😅")

# 5. Studentstatus
antwoord = input("Ben je student? (ja/nee): ").lower()
if antwoord == "ja":
    print("Succes met studeren!")
else:
    print("Fijn weekend!")

# 6. Vergelijk getallen
a = int(input("Eerste getal: "))
b = int(input("Tweede getal: "))
if a > b:
    print(a, "is groter dan", b)
elif a < b:
    print(a, "is kleiner dan", b)
else:
    print("Beide zijn gelijk.")

# 7. And/Or
leeftijd = int(input("Leeftijd: "))
student = input("Ben je student? (ja/nee): ").lower() == "ja"
if leeftijd < 30 and student:
    print("Jonge student!")
elif leeftijd >= 30 and not student:
    print("Ervaren volwassene!")

# 8. Geneste if
leeftijd = int(input("Hoe oud ben je? "))
if leeftijd < 12:
    print("Kind")
elif leeftijd < 18:
    print("Tiener")
else:
    if leeftijd < 65:
        print("Volwassene")
    else:
        print("Senior")

# 9. Inline if
punt = int(input("Cijfer: "))
print(f"Je bent {'geslaagd' if punt >= 55 else 'niet geslaagd'}.")

# 10. Scoreprogramma
score = int(input("Voer je score in: "))
if score >= 90:
    print("Uitstekend!")
elif score >= 75:
    print("Goed!")
elif score >= 55:
    print("Voldoende.")
else:
    print("Onvoldoende.")
