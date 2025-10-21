# ⚙️ Les 8 – Functies (Functions in Python)

Welkom bij les 8 van de **Python Lessenreeks**!  
In deze les leer je hoe je **functies** kunt maken en gebruiken.  
Functies helpen je om code te hergebruiken, overzichtelijk te houden en foutloos te programmeren.

---

## 🎯 Leerdoelen
- Functies definiëren met `def`  
- Functies aanroepen  
- Parameters en argumenten gebruiken  
- Waarden teruggeven met `return`  
- Lokale vs. globale variabelen begrijpen  

---

## 💻 Voorbeelden

### Voorbeeld 1 – Eenvoudige functie
```python
def groet():
    print("Hallo!")
groet()
```

### Voorbeeld 2 – Functie met parameter
```python
def groet_naam(naam):
    print("Hallo", naam)
groet_naam("Ozgur")
```

### Voorbeeld 3 – Twee parameters
```python
def tel_op(a, b):
    print("Som is:", a + b)
tel_op(5, 3)
```

### Voorbeeld 4 – Return-waarde
```python
def vermenigvuldig(a, b):
    return a * b

resultaat = vermenigvuldig(4, 5)
print("Resultaat:", resultaat)
```

### Voorbeeld 5 – Default waarde
```python
def begroeting(naam="vriend"):
    print("Hallo", naam)
begroeting()
begroeting("Emma")
```

### Voorbeeld 6 – Functie met berekening
```python
def gemiddelde(a, b, c):
    return (a + b + c) / 3
print("Gemiddelde:", gemiddelde(5, 8, 10))
```

### Voorbeeld 7 – Boolean return
```python
def is_volwassen(leeftijd):
    return leeftijd >= 18
print(is_volwassen(20))
```

### Voorbeeld 8 – Functie in een functie
```python
def kwadraat(x):
    return x * x

def som_van_kwadraten(a, b):
    return kwadraat(a) + kwadraat(b)

print(som_van_kwadraten(2, 3))
```

### Voorbeeld 9 – Functie met lijst
```python
def totaal(getallen):
    return sum(getallen)
print(totaal([2, 4, 6, 8]))
```

### Voorbeeld 10 – Complex voorbeeld
```python
def profiel(naam, leeftijd, stad):
    print(f"Naam: {naam}, Leeftijd: {leeftijd}, Stad: {stad}")

profiel("Ozgur", 30, "Amsterdam")
```

---

## 🧠 Uitleg
Een **functie** is een blok code dat pas wordt uitgevoerd als je het **aanroept**.  
Gebruik `def naam():` om een functie te maken.  
Met `return` kun je een waarde teruggeven.  
Voeg **parameters** toe tussen haakjes om invoer te gebruiken.

---

## 🧩 Opdrachten
Zie `opdrachten.md` voor 10 oefeningen over functies.

---

## ✅ Oplossingen
Bekijk `oplossingen.py` voor de uitgewerkte antwoorden.
