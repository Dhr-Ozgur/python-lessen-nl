# Voorbeelden – Les 5: Lussen

# 1. Simpele for-loop
for i in range(5):
    print("Hallo wereld!")

# 2. For-loop met teller
for i in range(1, 6):
    print("Nummer:", i)

# 3. Door tekst itereren
woord = "Python"
for letter in woord:
    print(letter)

# 4. Som berekenen
som = 0
for i in range(1, 6):
    som += i
print("Som =", som)

# 5. Lijst doorlopen
dieren = ["kat", "hond", "vis"]
for dier in dieren:
    print("Ik heb een", dier)

# 6. While-loop
teller = 0
while teller < 5:
    print("Teller is", teller)
    teller += 1

# 7. Break gebruiken
for i in range(10):
    if i == 5:
        break
    print(i)

# 8. Continue gebruiken
for i in range(6):
    if i == 3:
        continue
    print("Nummer:", i)

# 9. While met invoer
woord = ""
while woord != "stop":
    woord = input("Typ iets (of 'stop' om te stoppen): ")
    print("Je typte:", woord)

# 10. Geneste for-loop
for i in range(1, 4):
    for j in range(1, 4):
        print(i, "x", j, "=", i * j)
