# ✅ Oplossingen – Les 5: Lussen

# 1. Hallo wereld 5x
for i in range(5):
    print("Hallo wereld!")

# 2. Getallen 1 t/m 10
for i in range(1, 11):
    print(i)

# 3. Karakters van 'Python'
for letter in "Python":
    print(letter)

# 4. Som 1 t/m 100
som = 0
for i in range(1, 101):
    som += i
print("Som =", som)

# 5. While-loop tellen
teller = 0
while teller <= 5:
    print("Teller is", teller)
    teller += 1

# 6. Break
for i in range(10):
    if i == 6:
        break
    print(i)

# 7. Continue
for i in range(10):
    if i == 4:
        continue
    print("Nummer:", i)

# 8. Invoer tot 'stop'
woord = ""
while woord != "stop":
    woord = input("Typ iets (of 'stop' om te stoppen): ")
    print("Je typte:", woord)

# 9. Vermenigvuldigingstabel
for i in range(1, 6):
    for j in range(1, 6):
        print(i, "x", j, "=", i * j)
    print("---")

# 10. Even getallen 1–20
for i in range(1, 21):
    if i % 2 == 0:
        print(i)
