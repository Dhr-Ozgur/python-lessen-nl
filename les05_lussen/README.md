# 🔁 Les 5 – Lussen (for & while loops)

Welkom bij les 5 van de **Python Lessenreeks**!  
In deze les leer je hoe je **herhaling** gebruikt met `for`- en `while`-loops.

---

## 🎯 Leerdoelen
- Het verschil tussen `for` en `while` begrijpen  
- Itereren over reeksen (zoals lijsten of tekst)  
- Tel-lussen gebruiken met `range()`  
- De `break` en `continue` statements leren  
- Eindeloze lussen vermijden  

---

## 💻 Voorbeelden

### Voorbeeld 1 – Simpele for-loop
```python
for i in range(5):
    print("Hallo wereld!")
```

### Voorbeeld 2 – For-loop met teller
```python
for i in range(1, 6):
    print("Nummer:", i)
```

### Voorbeeld 3 – Door tekst itereren
```python
woord = "Python"
for letter in woord:
    print(letter)
```

### Voorbeeld 4 – Som berekenen
```python
som = 0
for i in range(1, 6):
    som += i
print("Som =", som)
```

### Voorbeeld 5 – Lijst doorlopen
```python
dieren = ["kat", "hond", "vis"]
for dier in dieren:
    print("Ik heb een", dier)
```

### Voorbeeld 6 – While-loop
```python
teller = 0
while teller < 5:
    print("Teller is", teller)
    teller += 1
```

### Voorbeeld 7 – Break gebruiken
```python
for i in range(10):
    if i == 5:
        break
    print(i)
```

### Voorbeeld 8 – Continue gebruiken
```python
for i in range(6):
    if i == 3:
        continue
    print("Nummer:", i)
```

### Voorbeeld 9 – Invoer met while
```python
woord = ""
while woord != "stop":
    woord = input("Typ iets (of 'stop' om te stoppen): ")
    print("Je typte:", woord)
```

### Voorbeeld 10 – Geneste for-loop
```python
for i in range(1, 4):
    for j in range(1, 4):
        print(i, "x", j, "=", i * j)
```

---

## 🧠 Uitleg
Een **for-loop** herhaalt een blok code een vast aantal keren.  
Een **while-loop** blijft doorgaan zolang de voorwaarde `True` is.  
Gebruik `break` om te stoppen, en `continue` om één iteratie over te slaan.  

---

## 🧩 Opdrachten
Zie `opdrachten.md` voor 10 oefeningen over for- en while-lussen.

---

## ✅ Oplossingen
Bekijk `oplossingen.py` voor de uitgewerkte antwoorden.
