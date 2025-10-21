# Voorbeelden – Les 7: Dictionaries

# 1. Dictionary maken
persoon = {"naam": "Ozgur", "leeftijd": 30, "stad": "Amsterdam"}
print(persoon)

# 2. Waarde ophalen
print(persoon["naam"])

# 3. Nieuwe key toevoegen
persoon["hobby"] = "programmeren"
print(persoon)

# 4. Waarde wijzigen
persoon["stad"] = "Rotterdam"
print(persoon)

# 5. Key verwijderen
del persoon["leeftijd"]
print(persoon)

# 6. Itereren over keys
for sleutel in persoon:
    print("Sleutel:", sleutel)

# 7. Itereren over values
for waarde in persoon.values():
    print("Waarde:", waarde)

# 8. Itereren over items
for sleutel, waarde in persoon.items():
    print(sleutel, "=", waarde)

# 9. Check of key bestaat
if "naam" in persoon:
    print("Naam bestaat in de dictionary.")

# 10. Geneste dictionary
studenten = {
    "s1": {"naam": "Emma", "leeftijd": 22},
    "s2": {"naam": "Ozgur", "leeftijd": 30}
}
print(studenten["s1"]["naam"])
