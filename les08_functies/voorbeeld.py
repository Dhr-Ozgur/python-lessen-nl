# Voorbeelden – Les 8: Functies

# 1. Eenvoudige functie
def groet():
    print("Hallo!")
groet()

# 2. Functie met parameter
def groet_naam(naam):
    print("Hallo", naam)
groet_naam("Ozgur")

# 3. Twee parameters
def tel_op(a, b):
    print("Som is:", a + b)
tel_op(5, 3)

# 4. Return-waarde
def vermenigvuldig(a, b):
    return a * b
print("Resultaat:", vermenigvuldig(4, 5))

# 5. Default parameter
def begroeting(naam="vriend"):
    print("Hallo", naam)
begroeting()
begroeting("Emma")

# 6. Gemiddelde functie
def gemiddelde(a, b, c):
    return (a + b + c) / 3
print("Gemiddelde:", gemiddelde(5, 8, 10))

# 7. Boolean functie
def is_volwassen(leeftijd):
    return leeftijd >= 18
print(is_volwassen(20))

# 8. Functie in functie
def kwadraat(x):
    return x * x
def som_van_kwadraten(a, b):
    return kwadraat(a) + kwadraat(b)
print(som_van_kwadraten(2, 3))

# 9. Functie met lijst
def totaal(getallen):
    return sum(getallen)
print(totaal([2, 4, 6, 8]))

# 10. Complex voorbeeld
def profiel(naam, leeftijd, stad):
    print(f"Naam: {naam}, Leeftijd: {leeftijd}, Stad: {stad}")
profiel("Ozgur", 30, "Amsterdam")
