# 📂 Les 10 – Bestandsbeheer (Files lezen & schrijven)

Welkom bij les 10 van de **Python Lessenreeks**!  
In deze les leer je hoe je met Python **bestanden kunt openen, lezen en schrijven**.  
We gebruiken functies zoals `open()`, `read()`, `write()`, en de contextmanager `with`.

---

## 🎯 Leerdoelen
- Tekstbestanden openen en sluiten  
- Inhoud lezen met `read()`, `readline()`, of `readlines()`  
- Tekst schrijven met `write()` of `writelines()`  
- De `with`-context gebruiken voor veilig bestandsbeheer  
- Foutafhandeling bij bestanden  

---

## 💻 Voorbeelden

### Voorbeeld 1 – Een bestand openen en lezen
```python
bestand = open("voorbeeld.txt", "r")
inhoud = bestand.read()
print(inhoud)
bestand.close()
```

### Voorbeeld 2 – Met `with` lezen (automatisch sluiten)
```python
with open("voorbeeld.txt", "r") as f:
    print(f.read())
```

### Voorbeeld 3 – Eén regel tegelijk lezen
```python
with open("voorbeeld.txt", "r") as f:
    regel = f.readline()
    print(regel)
```

### Voorbeeld 4 – Regels in lijst
```python
with open("voorbeeld.txt", "r") as f:
    regels = f.readlines()
print(regels)
```

### Voorbeeld 5 – Schrijven naar bestand
```python
with open("nieuw.txt", "w") as f:
    f.write("Hallo wereld!\n")
    f.write("Dit is een testbestand.")
```

### Voorbeeld 6 – Regels toevoegen (`a`-modus)
```python
with open("nieuw.txt", "a") as f:
    f.write("\nNog een regel toegevoegd.")
```

### Voorbeeld 7 – Lijst schrijven
```python
regels = ["Eerste regel\n", "Tweede regel\n", "Derde regel\n"]
with open("lijst.txt", "w") as f:
    f.writelines(regels)
```

### Voorbeeld 8 – Bestand lezen en tellen
```python
with open("lijst.txt", "r") as f:
    inhoud = f.readlines()
print("Aantal regels:", len(inhoud))
```

### Voorbeeld 9 – Bestand niet gevonden (try/except)
```python
try:
    with open("onbestaand.txt", "r") as f:
        print(f.read())
except FileNotFoundError:
    print("Bestand niet gevonden!")
```

### Voorbeeld 10 – Tekst bewerken en herschrijven
```python
with open("data.txt", "w") as f:
    f.write("Python is leuk!\n")
with open("data.txt", "r+") as f:
    tekst = f.read()
    f.write("\nJa, echt waar!")
```

---

## 🧠 Uitleg
- `"r"` = read (lezen)  
- `"w"` = write (nieuw bestand maken / overschrijven)  
- `"a"` = append (toevoegen aan bestaand bestand)  
- Gebruik **`with open()`** zodat Python het bestand automatisch sluit.  
- Gebruik `try/except` voor veilige foutafhandeling.  

---

## 🧩 Opdrachten
Zie `opdrachten.md` voor 10 oefeningen over bestandsbeheer.

---

## ✅ Oplossingen
Bekijk `oplossingen.py` voor de uitgewerkte antwoorden.
