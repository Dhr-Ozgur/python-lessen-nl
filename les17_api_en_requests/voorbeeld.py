# Voorbeelden – Les 17: Externe API’s gebruiken

import requests
import json

# 1. Basis API-aanroep
r = requests.get("https://api.github.com")
print(r.status_code)

# 2. JSON-data
print(r.json())

# 3. Publieke API: agify
r = requests.get("https://api.agify.io/?name=ozgur")
data = r.json()
print(data)

# 4. Statuscontrole
if r.status_code == 200:
    print("Succesvolle aanvraag!")

# 5. Queryparameters
params = {"name": "emma", "country_id": "NL"}
r = requests.get("https://api.nationalize.io/", params=params)
print(json.dumps(r.json(), indent=4))

# 6. API met foutafhandeling
try:
    fout = requests.get("https://foutieve-url.nl/data")
    fout.raise_for_status()
except requests.exceptions.RequestException as e:
    print("Foutmelding:", e)

# 7. JSON lijst uitlezen
r = requests.get("https://jsonplaceholder.typicode.com/users")
gebruikers = r.json()
for g in gebruikers[:5]:
    print(g["name"], "-", g["email"])

# 8. JSON opslaan
with open("gebruikers.json", "w") as f:
    json.dump(gebruikers, f, indent=4)

# 9. JSON lezen
with open("gebruikers.json", "r") as f:
    data = json.load(f)
print("Aantal gebruikers:", len(data))

# 10. Data filteren
for g in data:
    if g["address"]["city"].startswith("S"):
        print("Gebruiker uit stad met S:", g["name"])
