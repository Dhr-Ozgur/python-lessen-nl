# 🕒 Les 13 – Werken met Datum en Tijd (datetime-module)

Welkom bij les 13 van de **Python Lessenreeks**!  
In deze les leer je hoe je met Python **datums en tijden** kunt werken via de module `datetime`.

---

## 🎯 Leerdoelen
- De module `datetime` gebruiken  
- Huidige datum en tijd opvragen  
- Datumformatten aanpassen met `strftime()`  
- Datumverschillen berekenen met `timedelta`  
- Strings omzetten naar datums met `strptime()`  

---

## 💻 Voorbeelden

### Voorbeeld 1 – Huidige datum
```python
import datetime
vandaag = datetime.date.today()
print(vandaag)
```

### Voorbeeld 2 – Huidige tijd
```python
import datetime
nu = datetime.datetime.now()
print("Het is nu:", nu)
```

### Voorbeeld 3 – Datumcomponenten
```python
print("Jaar:", nu.year)
print("Maand:", nu.month)
print("Dag:", nu.day)
```

### Voorbeeld 4 – Tijdcomponenten
```python
print("Uur:", nu.hour)
print("Minuut:", nu.minute)
print("Seconde:", nu.second)
```

### Voorbeeld 5 – Datum formatteren
```python
print(nu.strftime("%d-%m-%Y %H:%M:%S"))
```

### Voorbeeld 6 – String naar datum
```python
datum = datetime.datetime.strptime("21-10-2025", "%d-%m-%Y")
print("Omgezet:", datum)
```

### Voorbeeld 7 – Datumverschil
```python
vandaag = datetime.date.today()
verjaardag = datetime.date(2025, 12, 25)
verschil = verjaardag - vandaag
print("Nog", verschil.days, "dagen tot kerst!")
```

### Voorbeeld 8 – Tijd toevoegen met timedelta
```python
from datetime import timedelta
morgen = vandaag + timedelta(days=1)
print("Morgen is:", morgen)
```

### Voorbeeld 9 – Datum vergelijken
```python
if vandaag < verjaardag:
    print("Je verjaardag is nog niet geweest.")
```

### Voorbeeld 10 – Custom tijd maken
```python
tijd = datetime.time(14, 30, 0)
print("Afspraak om:", tijd)
```

---

## 🧠 Uitleg
- **`datetime.date`** = alleen datum  
- **`datetime.time`** = allee
