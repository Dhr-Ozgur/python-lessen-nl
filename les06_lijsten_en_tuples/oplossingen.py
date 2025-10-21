# ✅ Oplossingen – Les 6: Lijsten en Tuples

# 1. Lijst van dieren
dieren = ["kat", "hond", "vis"]
print(dieren)

# 2. Eerste en laatste item
print("Eerste dier:", dieren[0])
print("Laatste dier:", dieren[-1])

# 3. Toevoegen
dieren.append("vogel")
print(dieren)

# 4. Verwijderen
dieren.remove("hond")
print(dieren)

# 5. Itereren
for dier in dieren:
    print("Ik heb een", dier)

# 6. Som en gemiddelde
getallen = [5, 10, 15, 20]
print("Som:", sum(getallen))
print("Gemiddelde:", sum(getallen)/len(getallen))

# 7. Min en max
print("Kleinste:", min(getallen))
print("Grootste:", max(getallen))

# 8. Tuple dagen
dagen = ("maandag", "dinsdag", "woensdag", "donderdag", "vrijdag")
for dag in dagen:
    print("Vandaag is", dag)

# 9. Tuple kleuren
kleuren = ("rood", "groen", "blauw")
for kleur in kleuren:
    print("Mijn favoriete kleur is", kleur)

# 10. Lijst vs tuple
lijst = [1, 2, 3]
tuple_data = (1, 2, 3)
lijst.append(4)
print("Lijst:", lijst)
print("Tuple:", tuple_data)
