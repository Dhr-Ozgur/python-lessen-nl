# 🧩 Les 18 – Foutlogging en Debugging (logging & try/except)

Welkom bij les 18 van de **Python Lessenreeks**!  
In deze les leer je hoe je fouten in je code kunt opsporen en bijhouden met de **logging-module**.  
Debugging is het proces van het vinden en oplossen van fouten in programma’s.

---

## 🎯 Leerdoelen
- Begrijpen wat debugging is  
- Logging gebruiken om fouten bij te houden  
- Logniveaus kennen: `DEBUG`, `INFO`, `WARNING`, `ERROR`, `CRITICAL`  
- Logs schrijven naar console én bestand  
- Foutafhandeling combineren met logging  

---

## 💻 Voorbeelden

### Voorbeeld 1 – Eenvoudige logging
```python
import logging
logging.basicConfig(level=logging.INFO)
logging.info("Programma gestart!")
```

### Voorbeeld 2 – Verschillende niveaus
```python
logging.debug("Debug info")
logging.info("Info bericht")
logging.warning("Waarschuwing!")
logging.error("Er is een fout opgetreden")
logging.critical("Kritieke fout!")
```

### Voorbeeld 3 – Logging configureren
```python
logging.basicConfig(
    filename="app.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
logging.info("Logbestand aangemaakt.")
```

### Voorbeeld 4 – Logging in try/except
```python
try:
    10 / 0
except ZeroDivisionError:
    logging.exception("Delen door nul is niet toegestaan!")
```

### Voorbeeld 5 – Debuggen met variabelen
```python
x = 10
y = 5
logging.debug(f"x={x}, y={y}, resultaat={x/y}")
```

### Voorbeeld 6 – Logs in bestand schrijven
```python
with open("app.log", "r") as f:
    print(f.read())
```

### Voorbeeld 7 – Logging in functies
```python
def bereken(a, b):
    try:
        return a / b
    except Exception as e:
        logging.error(f"Fout bij berekenen: {e}")
        return None
print(bereken(10, 0))
```

### Voorbeeld 8 – Fouten opslaan met ERROR-niveau
```python
for i in range(3):
    try:
        print(10 / (2 - i))
    except ZeroDivisionError as e:
        logging.error(f"Fout in iteratie {i}: {e}")
```

### Voorbeeld 9 – Logbestand analyseren
```python
with open("app.log", "r") as f:
    regels = f.readlines()
print("Aantal regels in log:", len(regels))
```

### Voorbeeld 10 – Custom logging formatter
```python
formatter = "%(levelname)s | %(message)s"
logging.basicConfig(format=formatter, level=logging.WARNING)
logging.warning("Test waarschuwing met aangepast format.")
```

---

## 🧠 Uitleg
- **Logging** = meldingen over wat je programma doet  
- Logniveaus:
  - DEBUG → gedetailleerde info voor ontwikkelaars  
  - INFO → algemene status  
  - WARNING → mogelijke problemen  
  - ERROR → fout tijdens uitvoering  
  - CRITICAL → ernstige fout  
- Gebruik **`logging.exception()`** om automatisch traceback toe te voegen  

---

## 🧩 Opdrachten
Zie `opdrachten.md` voor 10 oefeningen met logging en debugging.

---

## ✅ Oplossingen
Bekijk `oplossingen.py` voor de uitgewerkte antwoorden.
