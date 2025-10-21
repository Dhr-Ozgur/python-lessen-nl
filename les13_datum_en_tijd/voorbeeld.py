# Voorbeelden – Les 13: Datum en Tijd

import datetime
from datetime import timedelta

# 1. Huidige datum
print(datetime.date.today())

# 2. Huidige tijd
nu = datetime.datetime.now()
print("Het is nu:", nu)

# 3. Componenten
print("Jaar:", nu.year, "Maand:", nu.month, "Dag:", nu.day)

# 4. Tijdcomponenten
print("Uur:", nu.hour, "Minuut:", nu.minute)

# 5. Format
print(nu.strftime("%A %d %B %Y, %H:%M:%S"))

# 6. String naar datum
tekst = "21-10-2025"
datum = datetime.datetime.strptime(tekst, "%d-%m-%Y")
print("Omgezet:", datum)

# 7. Verschil tussen datums
vandaag = datetime.date.today()
verjaardag = datetime.date(2025, 12, 25)
verschil = verjaardag - vandaag
print("Nog", verschil.days, "dagen tot kerst!")

# 8. timedelta gebruiken
morgen = vandaag + timedelta(days=1)
print("Morgen is:", morgen)

# 9. Vergelijken
if vandaag < verjaardag:
    print("Verjaardag komt nog!")

# 10. Tijd object
tijd = datetime.time(14, 45, 0)
print("Afspraak om:", tijd)
