# ✅ Oplossingen – Les 12: Klassen en Objecten

# 1. Lege klasse
class Persoon:
    pass
p1 = Persoon()
print(p1)

# 2. Attributen
class Persoon:
    def __init__(self, naam, leeftijd):
        self.naam = naam
        self.leeftijd = leeftijd
p1 = Persoon("Ozgur", 30)
print(p1.naam, p1.leeftijd)

# 3. Methode groet()
class Persoon:
    def __init__(self, naam):
        self.naam = naam
    def groet(self):
        print("Hallo, ik ben", self.naam)
p1 = Persoon("Emma")
p1.groet()

# 4. Twee objecten
p2 = Persoon("Lena")
p2.groet()

# 5. Attribuut wijzigen
p1.leeftijd = 31
print("Nieuwe leeftijd:", p1.leeftijd)

# 6. Auto klasse
class Auto:
    def __init__(self, merk, model, bouwjaar):
        self.merk = merk
        self.model = model
        self.bouwjaar = bouwjaar

# 7. __str__ gebruiken
    def __str__(self):
        return f"{self.merk} {self.model} ({self.bouwjaar})"
auto = Auto("Tesla", "Model 3", 2023)
print(auto)

# 8. Erfenis
class Dier:
    def geluid(self):
        print("Onbekend geluid")
class Hond(Dier):
    def geluid(self):
        print("Woef!")
h = Hond()
h.geluid()

# 9. super() constructor
class Dier:
    def __init__(self, soort):
        self.soort = soort
class Hond(Dier):
    def __init__(self, naam, soort):
        super().__init__(soort)
        self.naam = naam
h = Hond("Bello", "hond")
print(h.naam, h.soort)

# 10. Lijst van objecten
personen = [
    Persoon("Ozgur"),
    Persoon("Emma"),
    Persoon("Lena")
]
for p in personen:
    p.groet()
