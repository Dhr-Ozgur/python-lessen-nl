# ✅ Oplossingen – Les 8: Functies

# 1. groet()
def groet():
    print("Hallo wereld!")
groet()

# 2. groet_naam()
def groet_naam(naam):
    print("Hallo", naam)
groet_naam("Ozgur")

# 3. tel_op()
def tel_op(a, b):
    print("Som is:", a + b)
tel_op(10, 5)

# 4. vermenigvuldig()
def vermenigvuldig(a, b):
    return a * b
print(vermenigvuldig(3, 4))

# 5. begroeting()
def begroeting(naam="vriend"):
    print("Hallo", naam)
begroeting()
begroeting("Emma")

# 6. gemiddelde()
def gemiddelde(a, b, c):
    return (a + b + c) / 3
print("Gemiddelde:", gemiddelde(5, 10, 15))

# 7. is_even()
def is_even(getal):
    return getal % 2 == 0
print(is_even(4), is_even(5))

# 8. lengte_van_woord()
def lengte_van_woord(woord):
    print("Lengte van het woord is:", len(woord))
lengte_van_woord("Python")

# 9. som_lijst()
def som_lijst(getallen):
    return sum(getallen)
print("Som:", som_lijst([1, 2, 3, 4]))

# 10. profiel()
def profiel(naam, leeftijd, stad):
    print(f"Naam: {naam}")
    print(f"Leeftijd: {leeftijd}")
    print(f"Stad: {stad}")
profiel("Ozgur", 30, "Amsterdam")
