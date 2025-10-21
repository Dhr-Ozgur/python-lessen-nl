# 📚 Les 6 – Lijsten en Tuples

Welkom bij les 6 van de **Python Lessenreeks**!  
In deze les leer je werken met **lijsten (lists)** en **tuples**, twee belangrijke manieren om meerdere waarden op te slaan.

---

## 🎯 Leerdoelen
- Lijsten maken en bewerken  
- Items toevoegen, verwijderen en aanpassen  
- Itereren over lijsten met loops  
- Het verschil tussen `list` en `tuple` begrijpen  
- Basisfuncties zoals `len()`, `min()`, `max()` en `sum()` gebruiken  

---

## 💻 Voorbeelden

### Voorbeeld 1 – Een lijst maken
```python
dieren = ["kat", "hond", "vis"]
print(dieren)
```

### Voorbeeld 2 – Een item uit de lijst tonen
```python
dieren = ["kat", "hond", "vis"]
print(dieren[0])
```

### Voorbeeld 3 – Item toevoegen
```python
dieren = ["kat", "hond"]
dieren.append("vogel")
print(dieren)
```

### Voorbeeld 4 – Item verwijderen
```python
dieren = ["kat", "hond", "vis"]
dieren.remove("hond")
print(dieren)
```

### Voorbeeld 5 – Door lijst itereren
```python
dieren = ["kat", "hond", "vis"]
for dier in dieren:
    print("Ik heb een", dier)
```

### Voorbeeld 6 – Lijstlengte
```python
getallen = [10, 20, 30, 40]
print("Aantal:", len(getallen))
```

### Voorbeeld 7 – Som en gemiddelde
```python
getallen = [4, 6, 8]
print("Som:", sum(getallen))
print("Gemiddelde:", sum(getallen)/len(getallen))
```

### Voorbeeld 8 – Tuple gebruiken
```python
dagen = ("maandag", "dinsdag", "woensdag")
print(dagen)
```

### Voorbeeld 9 – Tuple itereren
```python
for dag in ("maandag", "dinsdag", "woensdag"):
    print("Vandaag is", dag)
```

### Voorbeeld 10 – Verschil tussen list en tuple
```python
lijst = [1, 2, 3]
tuple_data = (1, 2, 3)
lijst.append(4)
# tuple_data.append(4) ❌ fout – tuples zijn onveranderlijk
print(lijst)
print(tuple_data)
```

---

## 🧠 Uitleg
- **List** = veranderbare verzameling (`[]`)  
- **Tuple** = onveranderlijke verzameling (`()`)  
- Gebruik `append()` om aan een lijst toe te voegen.  
- Gebruik `remove()` om iets te verwijderen.  
- Gebruik `len()`, `sum()`, `min()`, `max()` om lijsten te analyseren.  

---

## 🧩 Opdrachten
Zie `opdrachten.md` voor 10 oefeningen over lijsten en tuples.

---

## ✅ Oplossingen
Bekijk `oplossingen.py` voor de uitwerkingen.
