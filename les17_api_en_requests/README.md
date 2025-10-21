# 🌍 Les 17 – Externe API’s gebruiken (Requests & JSON)

Welkom bij les 17 van de **Python Lessenreeks**!  
In deze les leer je **hoe Python met internet kan praten** via API’s (Application Programming Interfaces).  
We gebruiken de module `requests` om data van websites of online diensten op te halen.

---

## 🎯 Leerdoelen
- Begrijpen wat een API is  
- Data ophalen van een web-API met `requests.get()`  
- Antwoorden lezen en statuscodes begrijpen  
- JSON-data uit een API verwerken  
- Eenvoudige foutafhandeling bij API-aanroepen  

---

## 💻 Voorbeelden

### Voorbeeld 1 – Basis API-aanroep
```python
import requests
response = requests.get("https://api.github.com")
print(response.status_code)
print(response.text)
```

### Voorbeeld 2 – JSON-data ophalen
```python
data = response.json()
print(type(data))
print(list(data.keys()))
```

### Voorbeeld 3 – Een publieke API gebruiken
```python
url = "https://api.agify.io/?name=ozgur"
r = requests.get(url)
data = r.json()
print("Naam:", data["name"])
print("Geschatte leeftijd:", data["age"])
```

### Voorbeeld 4 – Controleer statuscode
```python
if r.status_code == 200:
    print("Succesvolle aanvraag!")
else:
    print("Fout:", r.status_code)
```

### Voorbeeld 5 – Queryparameters gebruiken
```python
params = {"name": "emma", "country_id": "NL"}
r = requests.get("https://api.nationalize.io/", params=params)
print(r.json())
```

### Voorbeeld 6 – JSON netjes afdrukken
```python
import json
print(json.dumps(r.json(), indent=4))
```

### Voorbeeld 7 – API met foutafhandeling
```python
try:
    r = requests.get("https://foutieve-url.nl/data")
    r.raise_for_status()
except requests.exceptions.RequestException as e:
    print("Er is een fout opgetreden:", e)
```

### Voorbeeld 8 – Werken met lijsten in JSON
```python
r = requests.get("https://jsonplaceholder.typicode.com/users")
gebruikers = r.json()
for g in gebruikers[:3]:
    print(g["name"], "-", g["email"])
```

### Voorbeeld 9 – Data opslaan als JSON-bestand
```python
import json
with open("gebruikers.json", "w") as f:
    json.dump(gebruikers, f, indent=4)
```

### Voorbeeld 10 – JSON-bestand teruglezen
```python
with open("gebruikers.json", "r") as f:
    data = json.load(f)
print("Aantal gebruikers:", len(data))
```

---

## 🧠 Uitleg
- **API** = een manier voor programma’s om met elkaar te communiceren  
- **`requests.get()`** haalt data van het internet op  
- **`response.status_code`** geeft de HTTP-status terug (200 = OK)  
- **`response.json()`** zet de API-data om naar Python-structuren  
- Gebruik `try/except` voor netwerkfouten  

---

## 🧩 Opdrachten
Zie `opdrachten.md` voor 10 oefeningen over API’s en JSON.

---

## ✅ Oplossingen
Bekijk `oplossingen.py` voor de uitgewerkte antwoorden.
