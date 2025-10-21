# Voorbeelden – Les 6: Lijsten en Tuples

# 1. Een lijst maken
dieren = ["kat", "hond", "vis"]
print(dieren)

# 2. Een item tonen
print(dieren[0])

# 3. Item toevoegen
dieren.append("vogel")
print(dieren)

# 4. Item verwijderen
dieren.remove("hond")
print(dieren)

# 5. Door lijst itereren
for dier in dieren:
    print("Ik heb een", dier)

# 6. Lijstlengte
getallen = [10, 20, 30, 40]
print("Aantal:", len(getallen))

# 7. Som en gemiddelde
print("Som:", sum(getallen))
print("Gemiddelde:", sum(getallen)/len(getallen))

# 8. Tuple gebruiken
dagen = ("maandag", "dinsdag", "woensdag")
print(dagen)

# 9. Tuple itereren
for dag in dagen:
    print("Vandaag is", dag)

# 10. Verschil list vs tuple
lijst = [1, 2, 3]
tuple_data = (1, 2, 3)
lijst.append(4)
print(lijst)
print(tuple_data)
