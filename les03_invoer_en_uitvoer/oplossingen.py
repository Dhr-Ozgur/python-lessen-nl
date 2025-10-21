# ✅ Oplossingen – Les 3: Invoer en Uitvoer

# 1. Naam
naam = input("Wat is je naam? ")
print("Hallo", naam)

# 2. Leeftijd
leeftijd = input("Hoe oud ben je? ")
print("Je bent", leeftijd, "jaar oud.")

# 3. Som van twee getallen
a = int(input("Voer een getal in: "))
b = int(input("Voer nog een getal in: "))
print("De som is:", a + b)

# 4. Woonplaats
stad = input("Waar woon je? ")
print("Je woont in", stad, "🌆")

# 5. Naam en leeftijd
naam = input("Wat is je naam? ")
leeftijd = input("Hoe oud ben je? ")
print("Hallo", naam + ", je bent", leeftijd, "jaar oud.")

# 6. Lengte
lengte = float(input("Wat is je lengte in meters? "))
print("Je lengte is", lengte, "m.")

# 7. Verdubbeling en kwadraat
getal = int(input("Voer een getal in: "))
print("Het dubbele is:", getal * 2)
print("Het kwadraat is:", getal ** 2)

# 8. Boolean input
antwoord = input("Ben je student? (ja/nee): ")
is_student = antwoord.lower() == "ja"
print("Studentstatus:", is_student)

# 9. f-string begroeting
naam = input("Wat is je naam? ")
print(f"Welkom bij de cursus, {naam}! 🎓")

# 10. Profielprogramma
naam = input("Naam: ")
leeftijd = int(input("Leeftijd: "))
stad = input("Woonplaats: ")
hobby = input("Wat is je hobby? ")
print(f"--- PROFIEL ---")
print(f"Naam: {naam}")
print(f"Leeftijd: {leeftijd}")
print(f"Woonplaats: {stad}")
print(f"Hobby: {hobby}")
