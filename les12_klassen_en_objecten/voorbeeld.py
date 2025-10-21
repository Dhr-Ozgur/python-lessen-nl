# Voorbeelden – Les 12: Klassen en Objecten

# 1. Eenvoudige klasse
class Persoon:
    pass
p1 = Persoon()
print(p1)

# 2. Klasse met attributen
class Persoon:
    def __init__(self, naam, leeftijd):
        self.naam = naam
        self.leeftijd = leeftijd
p1 = Persoon("Ozgur", 30)
print(p1.naam, p1.leeftijd)

# 3. Methode
class Persoon:
    def __init__(self, naam):
        self.naam = naam
    def groet(self):
        print("Hallo, ik ben", self.naam)
p1 = Persoon("Emma")
p1.groet()

# 4. Meerdere objecten
p2 = Persoon("Lena")
p2.groet()

# 5. Object wijzigen
p1.leeftijd = 31
print("Nieuwe leeftijd:", p1.leeftijd)

# 6. Standaardwaarde
class Auto:
    def __init__(self, merk="Onbekend"):
        self.merk = merk
auto = Auto()
print(auto.merk)

# 7. __str__ methode
class Dier:
    def __init__(self, naam, soort):
        self.naam = naam
        self.soort = soort
    def __str__(self):
        return f"{self.naam} is een {self.soort}"
print(Dier("Minoes", "kat"))

# 8. Erfenis
class Dier:
    def geluid(self):
        print("Onbekend geluid")
class Hond(Dier):
    def geluid(self):
        print("Woef!")
h = Hond()
h.geluid()

# 9. super() gebruiken
class Dier:
    def __init__(self, soort):
        self.soort = soort
class Hond(Dier):
    def __init__(self, naam, soort):
        super().__init__(soort)
        self.naam = naam
h = Hond("Rex", "hond")
print(h.soort, h.naam)

# 10. Lijst van objecten
dieren = [Dier("kat"), Dier("hond")]
for d in dieren:
    print(d.soort)
