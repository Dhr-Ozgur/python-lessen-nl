# ✅ Oplossingen – Les 17: Externe API’s gebruiken

import requests
import json

# 1. Basis-aanroep
r = requests.get("https://api.github.com")
print("Status:", r.status_code)

# 2. JSON bekijken
print(r.json())

# 3. Agify API
r = requests.get("https://api.agify.io/?name=emma")
data = r.json()
print("Naam:", data["name"], "- Leeftijd:", data["age"])

# 4. Succescontrole
if r.status_code == 200:
    print("Alles werkt goed!")
else:
    print("Fout:", r.status_code)

# 5. Nationalize.io
params = {"name": "emma", "country_id": "NL"}
r = requests.get("https://api.nationalize.io/", params=params)
print(r.json())

# 6. Mooie JSON
print(json.dumps(r.json(), indent=4))

# 7. Foutafhandeling
try:
    fout = requests.get("https://foute-url.nl/data")
    fout.raise_for_status()
except requests.exceptions.RequestException as e:
    print("Netwerkfout:", e)

# 8. Gebruikers tonen
r = requests.get("https://jsonplaceholder.typicode.com/users")
gebruikers = r.json()
for g in gebruikers[:5]:
    print(g["name"])

# 9. Opslaan als JSON
with open("gebruikers.json", "w") as f:
    json.dump(gebruikers, f, indent=4)

# 10. Herlezen en tellen
with open("gebruikers.json", "r") as f:
    data = json.load(f)
print("Totaal gebruikers:", len(data))
