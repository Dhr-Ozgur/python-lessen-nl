# ✅ Oplossingen – Les 13: Datum en Tijd

import datetime
from datetime import timedelta

# 1. Huidige datum
print(datetime.date.today())

# 2. Huidige datum en tijd
print(datetime.datetime.now())

# 3. Jaar, maand, dag
nu = datetime.datetime.now()
print("Jaar:", nu.year, "Maand:", nu.month, "Dag:", nu.day)

# 4. Format dd-mm-jjjj
print(nu.strftime("%d-%m-%Y"))

# 5. String naar datum
tekst = "10-05-2026"
datum = datetime.datetime.strptime(tekst, "%d-%m-%Y")
print(datum)

# 6. Dagen tot 1 januari
vandaag = datetime.date.today()
nieuwjaar = datetime.date(vandaag.year + 1, 1, 1)
print("Nog", (nieuwjaar - vandaag).days, "dagen tot nieuwjaar.")

# 7. Een week later
week_later = vandaag + timedelta(days=7)
print("Over een week is het:", week_later)

# 8. Tijdobject
tijd = datetime.time(9, 30, 0)
print("Afspraak om:", tijd)

# 9. Datums vergelijken
datum1 = datetime.date(2025, 5, 10)
datum2 = datetime.date(2025, 5, 12)
if datum1 < datum2:
    print("Datum1 komt eerder dan Datum2")

# 10. Leeftijd berekenen
geboorte = datetime.date(1995, 3, 10)
leeftijd_dagen = (vandaag - geboorte).days
print("Je bent ongeveer", leeftijd_dagen, "dagen oud.")
