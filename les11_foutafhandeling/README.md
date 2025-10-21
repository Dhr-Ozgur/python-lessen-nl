# ⚠️ Les 11 – Foutafhandeling (Exceptions & try/except)

Welkom bij les 11 van de **Python Lessenreeks**!  
In deze les leer je hoe je fouten in je code kunt opvangen en voorkomen dat je programma crasht.  
We gebruiken hiervoor de sleutelwoorden `try`, `except`, `else` en `finally`.

---

## 🎯 Leerdoelen
- Het verschil tussen fouttypes begrijpen  
- Fouten voorkomen met `try/except`  
- De `else`- en `finally`-blokken gebruiken  
- Eigen foutmeldingen maken met `raise`  
- Meerdere excepties combineren  

---

## 💻 Voorbeelden

### Voorbeeld 1 – Eenvoudige fout
```python
print(10 / 0)  # ZeroDivisionError
```

### Voorbeeld 2 – try/except
```python
try:
    print(10 / 0)
except ZeroDivisionError:
    print("Delen door nul is niet toegestaan!")
```

### Voorbeeld 3 – Meerdere excepties
```python
try:
    getal = int("abc")
except ValueError:
    print("Ongeldige invoer!")
except Exception as e:
    print("Onbekende fout:", e)
```

### Voorbeeld 4 – else-blok
```python
try:
    getal = int(input("Voer een getal in: "))
except ValueError:
    print("Dat is geen getal!")
else:
    print("Je voerde in:", getal)
```

### Voorbeeld 5 – finally-blok
```python
try:
    bestand = open("data.txt", "r")
except FileNotFoundError:
    print("Bestand niet gevonden!")
finally:
    print("Probeer voltooid.")
```

### Voorbeeld 6 – Eigen exceptie
```python
try:
    leeftijd = int(input("Leeftijd: "))
    if leeftijd < 0:
        raise ValueError("Leeftijd kan niet negatief zijn!")
except ValueError as e:
    print("Fout:", e)
```

### Voorbeeld 7 – Combinatie van fouten
```python
try:
    x = int(input("Eerste getal: "))
    y = int(input("Tweede getal: "))
    print("Resultaat:", x / y)
except ZeroDivisionError:
    print("Je kunt niet door nul delen!")
except ValueError:
    print("Alleen cijfers zijn toegestaan.")
```

### Voorbeeld 8 – try in functie
```python
def deel(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Kan niet delen door nul!"
print(deel(10, 0))
```

### Voorbeeld 9 – foutmelding printen
```python
try:
    a = int("abc")
except Exception as e:
    print("Foutmelding:", e)
```

### Voorbeeld 10 – Eigen functie met raise
```python
def controleer_getal(x):
    if x < 0:
        raise ValueError("Negatieve getallen niet toegestaan!")
    else:
        print("Getal is geldig:", x)

try:
    controleer_getal(-5)
except ValueError as e:
    print("Fout:", e)
```

---

## 🧠 Uitleg
- **try:** code die mogelijk fout kan geven  
- **except:** code die wordt uitgevoerd bij een fout  
- **else:** code die wordt uitgevoerd als er géén fout is  
- **finally:** code die altijd wordt uitgevoerd  
- Gebruik **`raise`** om zelf een fout te veroorzaken.  

---

## 🧩 Opdrachten
Zie `opdrachten.md` voor 10 oefeningen met foutafhandeling.

---

## ✅ Oplossingen
Bekijk `oplossingen.py` voor de uitgewerkte antwoorden.
