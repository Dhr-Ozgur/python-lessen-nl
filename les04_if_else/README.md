# ⚖️ Les 4 – If-Else Structuren

Welkom bij les 4 van de **Python Lessenreeks**!  
In deze les leer je hoe een programma beslissingen kan nemen met **if**, **elif** en **else**.

---

## 🎯 Leerdoelen
- De structuur van `if` begrijpen  
- `elif` en `else` gebruiken  
- Vergelijkingsoperatoren leren (`==`, `!=`, `>`, `<`, `>=`, `<=`)  
- Logische operatoren (`and`, `or`, `not`)  
- Verschillende condities combineren  

---

## 💻 Voorbeelden

### Voorbeeld 1 – Eenvoudige if
```python
leeftijd = 18
if leeftijd >= 18:
    print("Je bent volwassen.")
```

### Voorbeeld 2 – If-else
```python
leeftijd = 16
if leeftijd >= 18:
    print("Volwassene")
else:
    print("Minderjarig")
```

### Voorbeeld 3 – If-elif-else
```python
score = 85
if score >= 90:
    print("Uitstekend")
elif score >= 75:
    print("Goed")
else:
    print("Voldoende of lager")
```

### Voorbeeld 4 – Gelijkheid controleren
```python
naam = "Ozgur"
if naam == "Ozgur":
    print("Welkom terug!")
```

### Voorbeeld 5 – Meerdere condities
```python
leeftijd = 25
student = True
if leeftijd < 30 and student:
    print("Jonge student!")
```

### Voorbeeld 6 – OR gebruiken
```python
dag = "zaterdag"
if dag == "zaterdag" or dag == "zondag":
    print("Het is weekend!")
```

### Voorbeeld 7 – NOT gebruiken
```python
regent = False
if not regent:
    print("Het is droog buiten ☀️")
```

### Voorbeeld 8 – Geneste if
```python
leeftijd = 20
if leeftijd >= 18:
    print("Volwassene")
    if leeftijd < 21:
        print("Maar nog geen 21!")
```

### Voorbeeld 9 – F-strings met voorwaarden
```python
naam = "Emma"
leeftijd = 17
print(f"{naam} is {'volwassen' if leeftijd >= 18 else 'minderjarig'}.")
```

### Voorbeeld 10 – Complex voorbeeld
```python
punt = 78
geslaagd = punt >= 55
if geslaagd:
    print("Gefeliciteerd, je bent geslaagd!")
else:
    print("Helaas, probeer opnieuw.")
```

---

## 🧠 Uitleg
Een **if-else structuur** laat je programma beslissingen nemen.  
De voorwaarde tussen haakjes moet **True** of **False** zijn.  
Gebruik `and`, `or`, en `not` om meerdere condities te combineren.  
Gebruik inspringing (4 spaties) om codeblokken te markeren.  

---

## 🧩 Opdrachten
Zie `opdrachten.md` voor 10 oefeningen van makkelijk tot moeilijk.

---

## ✅ Oplossingen
De uitwerkingen vind je in `oplossingen.py`.
