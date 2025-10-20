# 💡 Les 2 – Variabelen en Datatypes

Welkom bij de tweede les van de **Python Lessenreeks**!  
In deze les leer je hoe je gegevens kunt opslaan in **variabelen** en werken met verschillende **datatypes** zoals tekst, getallen en booleans.

---

## 🎯 Leerdoelen
- Begrijpen wat een variabele is  
- Werken met verschillende datatypes (`str`, `int`, `float`, `bool`)  
- Basis van berekeningen in Python  
- Strings combineren met variabelen  
- Data op een leesbare manier tonen  

---

## 💻 Voorbeelden

### Voorbeeld 1 – Eenvoudige variabele
```python
naam = "Emma"
print(naam)
```

### Voorbeeld 2 – Getallen gebruiken
```python
leeftijd = 25
print(leeftijd)
```

### Voorbeeld 3 – Tekst combineren
```python
naam = "Emma"
leeftijd = 25
print("Mijn naam is", naam, "en ik ben", leeftijd, "jaar oud.")
```

### Voorbeeld 4 – Float-waarde
```python
lengte = 1.75
print("Mijn lengte is", lengte, "meter.")
```

### Voorbeeld 5 – Boolean
```python
is_student = True
print("Ben ik student?", is_student)
```

### Voorbeeld 6 – Berekening
```python
x = 10
y = 5
resultaat = x + y
print("De som is:", resultaat)
```

### Voorbeeld 7 – Type controleren
```python
naam = "Emma"
print(type(naam))
```

### Voorbeeld 8 – Typeconversie
```python
leeftijd = "25"
leeftijd = int(leeftijd)
print(leeftijd + 5)
```

### Voorbeeld 9 – Samenvoegen met f-strings
```python
naam = "Ozgur"
leeftijd = 30
print(f"Hallo, ik ben {naam} en ik ben {leeftijd} jaar oud.")
```

### Voorbeeld 10 – Complex voorbeeld
```python
naam = "Sanne"
leeftijd = 28
is_student = False
print(f"Naam: {naam}\nLeeftijd: {leeftijd}\nStudent: {is_student}")
```

---

## 🧠 Uitleg
Een **variabele** is als een doos waarin je een waarde bewaart.  
Je kunt die waarde later gebruiken of veranderen.  
Python herkent automatisch het datatype: tekst (`str`), geheel getal (`int`), kommagetal (`float`) of waar/niet waar (`bool`).  

Gebruik `type()` om te zien welk datatype een variabele heeft.

---

## 🧩 Opdrachten
Zie `opdrachten.md` voor 10 oefeningen om met variabelen te oefenen.

---

## ✅ Oplossingen
De uitwerkingen vind je in `oplossingen.py`.
