# 📥 Les 3 – Invoer en Uitvoer

Welkom bij les 3 van de **Python Lessenreeks**!  
In deze les leer je hoe je gegevens kunt **invoeren met de functie `input()`** en hoe je die informatie kunt **weergeven met `print()`**.

---

## 🎯 Leerdoelen
- De functie `input()` gebruiken  
- Gebruikersinvoer opslaan in variabelen  
- `print()` en `input()` combineren  
- Typeconversie toepassen (tekst → getal)  
- Dynamische uitvoer maken  

---

## 💻 Voorbeelden

### Voorbeeld 1 – Eenvoudige invoer
```python
naam = input("Wat is je naam? ")
print("Hallo", naam)
```

### Voorbeeld 2 – Leeftijd vragen
```python
leeftijd = input("Hoe oud ben je? ")
print("Je bent", leeftijd, "jaar oud.")
```

### Voorbeeld 3 – Getallen optellen (met typeconversie)
```python
a = int(input("Voer een getal in: "))
b = int(input("Voer nog een getal in: "))
print("De som is:", a + b)
```

### Voorbeeld 4 – Tekst combineren
```python
stad = input("Waar woon je? ")
print("Je woont in", stad, "🌆")
```

### Voorbeeld 5 – Meerdere inputs in één programma
```python
naam = input("Wat is je naam? ")
leeftijd = input("Hoe oud ben je? ")
print("Hallo", naam + ", je bent", leeftijd, "jaar oud.")
```

### Voorbeeld 6 – Lengte berekenen
```python
lengte = float(input("Wat is je lengte in meters? "))
print("Je lengte is", lengte, "m.")
```

### Voorbeeld 7 – Berekening met input
```python
getal = int(input("Voer een getal in: "))
print("Het dubbele van jouw getal is:", getal * 2)
```

### Voorbeeld 8 – Boolean input
```python
antwoord = input("Ben je student? (ja/nee): ")
is_student = antwoord.lower() == "ja"
print("Studentstatus:", is_student)
```

### Voorbeeld 9 – Gebruiker begroeten
```python
naam = input("Wat is je naam? ")
print(f"Welkom bij de cursus, {naam}! 🎓")
```

### Voorbeeld 10 – Klein programma
```python
naam = input("Naam: ")
leeftijd = int(input("Leeftijd: "))
stad = input("Woonplaats: ")
print(f"{naam}, {leeftijd} jaar, woont in {stad}.")
```

---

## 🧠 Uitleg
Met **`input()`** kun je gegevens van de gebruiker vragen.  
Standaard wordt invoer als **tekst (string)** opgeslagen.  
Gebruik `int()` of `float()` om getallen te kunnen berekenen.  
Combineer `input()` en `print()` om interactieve programma’s te maken.

---

## 🧩 Opdrachten
Zie `opdrachten.md` voor 10 oefeningen met gebruikersinvoer.

---

## ✅ Oplossingen
Bekijk `oplossingen.py` voor de uitgewerkte antwoorden.
