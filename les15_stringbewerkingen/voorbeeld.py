# Voorbeelden – Les 15: Geavanceerde Stringbewerkingen

import re

# 1. Slicing
tekst = "Python is geweldig"
print(tekst[:6])
print(tekst[-9:])

# 2. upper/lower
print(tekst.upper())
print(tekst.lower())

# 3. split/join
woorden = tekst.split()
print(woorden)
print(" - ".join(woorden))

# 4. replace
print(tekst.replace("geweldig", "fantastisch"))

# 5. count/find
zin = "Python is leuk. Python is krachtig."
print("Aantal:", zin.count("Python"))
print("Positie van 'leuk':", zin.find("leuk"))

# 6. f-string
naam = "Ozgur"
leeftijd = 30
print(f"Mijn naam is {naam} en ik ben {leeftijd} jaar oud.")

# 7. format
print("Hallo {}, welkom bij {}!".format("Emma", "Python"))

# 8. Regex e-mail
tekst = "Mijn e-mail is test@example.com"
print(re.findall(r"\S+@\S+", tekst))

# 9. Regex cijfers
zin = "Er zijn 3 katten en 12 honden."
print(re.findall(r"\d+", zin))

# 10. Regex vervangen
tekst = "Ik hou van Java, maar Python is beter."
print(re.sub(r"Java", "Python", tekst))
