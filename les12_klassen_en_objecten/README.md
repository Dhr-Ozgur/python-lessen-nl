# 🧱 Les 12 – Klassen en Objecten (OOP)

Welkom bij les 12 van de **Python Lessenreeks**!  
In deze les leer je de basis van **objectgeoriënteerd programmeren (OOP)**:  
je leert hoe je **klassen** en **objecten** maakt en gebruikt.

---

## 🎯 Leerdoelen
- Een klasse definiëren met `class`  
- Objecten maken (instanties van een klasse)  
- De constructor `__init__()` gebruiken  
- Methoden binnen een klasse schrijven  
- Erfenis (inheritance) toepassen  

---

## 💻 Voorbeelden

### Voorbeeld 1 – Eenvoudige klasse
```python
class Persoon:
    pass

p1 = Persoon()
print(p1)
```

### Voorbeeld 2 – Klasse met attributen
```python
class Persoon:
    def __init__(self, naam, leeftijd):
        self.naam = naam
        self.leeftijd = leeftijd

p1 = Persoon("Ozgur", 30)
print(p1.naam, p1.leeftijd)
```

### Voorbeeld 3 – Methode toevoegen
```python
class Persoon:
    def __init__(self, naam):
        self.naam = naam
    
    def groet(self):
        print("Hallo, ik ben", self.naam)

p1 = Persoon("Emma")
p1.groet()
```

### Voorbeeld 4 – Meerdere objecten
```python
p1 = Persoon("Ozgur")
p2 = Persoon("Lena")
p1.groet()
p2.groet()
```

### Voorbeeld 5 – Object wijzigen
```python
p1.leeftijd = 31
print("Nieuwe leeftijd:", p1.leeftijd)
```

### Voorbeeld 6 – Klasse met standaardwaarde
```python
class Auto:
    def __init__(self, merk="Onbekend"):
        self.merk = merk

auto = Auto()
print(auto.merk)
```

### Voorbeeld 7 – __str__ methode
```python
class Dier:
    def __init__(self, naam, soort):
        self.naam = naam
        self.soort = soort
    
    def __str__(self):
        return f"{self.naam} is een {self.soort}"

print(Dier("Minoes", "kat"))
```

### Voorbeeld 8 – Erfenis (inheritance)
```python
class Dier:
    def geluid(self):
        print("Onbekend geluid")

class Hond(Dier):
    def geluid(self):
        print("Woef!")

h = Hond()
h.geluid()
```

### Voorbeeld 9 – super() gebruiken
```python
class Dier:
    def __init__(self, soort):
        self.soort = soort

class Hond(Dier):
    def __init__(self, naam, soort):
        super().__init__(soort)
        self.naam = naam

h = Hond("Rex", "hond")
print(h.soort, h.naam)
```

### Voorbeeld 10 – Lijst van objecten
```python
dieren = [Dier("Minoes", "kat"), Dier("Bello", "hond")]
for d in dieren:
    print(d)
```

---

## 🧠 Uitleg
- **Class** = sjabloon voor objecten  
- **Object** = een specifieke instantie van een klasse  
- **self** verwijst naar het huidige object  
- **`__init__`** = constructor (wordt automatisch aangeroepen bij aanmaak)  
- **Inheritance** = een klasse overnemen en uitbreiden  

---

## 🧩 Opdrachten
Zie `opdrachten.md` voor 10 oefeningen over klassen en objecten.

---

## ✅ Oplossingen
Bekijk `oplossingen.py` voor de uitgewerkte antwoorden.
