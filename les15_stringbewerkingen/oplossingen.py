# ✅ Oplossingen – Les 15: Stringbewerkingen

import re

# 1. Slicing
tekst = "Python is leuk"
print(tekst[:5])

# 2. Hoofdletters en kleine letters
print(tekst.upper())
print(tekst.lower())

# 3. Split
print(tekst.split())

# 4. Replace
print(tekst.replace("leuk", "geweldig"))

# 5. Count
zin = "Python is leuk. Python is krachtig. Python is geweldig."
print("Aantal keer Python:", zin.count("Python"))

# 6. f-string
naam = "Ozgur"
leeftijd = 30
print(f"Mijn naam is {naam} en ik ben {leeftijd} jaar oud.")

# 7. format()
print("Hallo {}, welkom bij {}!".format("Emma", "Python"))

# 8. Regex e-mail
tekst = "Contact: test@example.com of info@school.nl"
print(re.findall(r"\S+@\S+", tekst))

# 9. Regex cijfers
zin = "Er zijn 15 appels en 3 bananen."
print(re.findall(r"\d+", zin))

# 10. Regex vervangen
tekst = "Ik hou van Java, maar Python is beter."
print(re.sub(r"Java", "Python", tekst))
