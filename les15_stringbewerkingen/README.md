# ✂️ Les 15 – Geavanceerde Stringbewerkingen (Regex, Slicing & Formatting)

Welkom bij les 15 van de **Python Lessenreeks**!  
In deze les leer je **strings op verschillende manieren te bewerken en te analyseren** met slicing, functies en reguliere expressies (regex).

---

## 🎯 Leerdoelen
- Strings doorsnijden met slicing  
- Belangrijke stringmethoden gebruiken (`upper()`, `replace()`, `split()`, etc.)  
- Tekst formatteren met `f-strings` en `.format()`  
- Patronen zoeken met de module `re` (regex)  
- Substrings vinden, tellen en vervangen  

---

## 💻 Voorbeelden

### Voorbeeld 1 – Basis slicing
```python
tekst = "Python is geweldig"
print(tekst[0:6])   # 'Python'
print(tekst[-9:])   # 'geweldig'
```

### Voorbeeld 2 – upper(), lower()
```python
print(tekst.upper())
print(tekst.lower())
```

### Voorbeeld 3 – split() en join()
```python
woorden = tekst.split()
print(woorden)
print(" | ".join(woorden))
```

### Voorbeeld 4 – replace()
```python
print(tekst.replace("geweldig", "fantastisch"))
```

### Voorbeeld 5 – count() en find()
```python
zin = "Python is leuk. Python is krachtig."
print("Aantal keer:", zin.count("Python"))
print("Eerste positie:", zin.find("leuk"))
```

### Voorbeeld 6 – f-string formatting
```python
naam = "Ozgur"
leeftijd = 30
print(f"Mijn naam is {naam} en ik ben {leeftijd} jaar oud.")
```

### Voorbeeld 7 – format()
```python
print("Hallo {}, welkom bij {}!".format("Emma", "Python"))
```

### Voorbeeld 8 – Regex: patroon zoeken
```python
import re
tekst = "Mijn e-mail is test@example.com"
resultaat = re.findall(r"\S+@\S+", tekst)
print(resultaat)
```

### Voorbeeld 9 – Regex: cijfers vinden
```python
zin = "Er zijn 3 katten en 12 honden."
print(re.findall(r"\d+", zin))
```

### Voorbeeld 10 – Regex: vervanging
```python
tekst = "Ik hou van Java, maar Python is beter."
print(re.sub(r"Java", "Python", tekst))
```

---

## 🧠 Uitleg
- **Slicing** = tekstdelen pakken via `tekst[start:eind]`  
- **Stringmethoden** zoals `.upper()`, `.replace()`, `.split()` helpen bij manipulatie  
- **f-strings** en `.format()` = dynamisch tekst samenstellen  
- **Regex** (`import re`) laat toe om tekstpatronen te vinden  
- Gebruik `re.findall()`, `re.search()`, `re.sub()` voor patroonherkenning en vervanging  

---

## 🧩 Opdrachten
Zie `opdrachten.md` voor 10 oefeningen over stringbewerkingen.

---

## ✅ Oplossingen
Bekijk `oplossingen.py` voor de uitgewerkte antwoorden.
