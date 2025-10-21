# ✅ Oplossingen – Les 7: Dictionaries

# 1. Dictionary maken
persoon = {"naam": "Ozgur", "leeftijd": 30, "stad": "Amsterdam"}
print(persoon)

# 2. Naam printen
print("Naam:", persoon["naam"])

# 3. Hobby toevoegen
persoon["hobby"] = "programmeren"
print(persoon)

# 4. Stad wijzigen
persoon["stad"] = "Rotterdam"
print(persoon)

# 5. Leeftijd verwijderen
del persoon["leeftijd"]
print(persoon)

# 6. Sleutels printen
for sleutel in persoon:
    print("Sleutel:", sleutel)

# 7. Waarden printen
for waarde in persoon.values():
    print("Waarde:", waarde)

# 8. Items printen
for sleutel, waarde in persoon.items():
    print(f"{sleutel} = {waarde}")

# 9. Check key
if "naam" in persoon:
    print("Naam bestaat in de dictionary.")

# 10. Geneste dictionary
studenten = {
    "s1": {"naam": "Emma", "leeftijd": 22},
    "s2": {"naam": "Ozgur", "leeftijd": 30}
}
print("Student 1:", studenten["s1"]["naam"], "-", studenten["s1"]["leeftijd"])
print("Student 2:", studenten["s2"]["naam"], "-", studenten["s2"]["leeftijd"])
