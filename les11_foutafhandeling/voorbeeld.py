# Voorbeelden – Les 11: Foutafhandeling

# 1. Eenvoudige fout
# print(10 / 0)

# 2. try/except
try:
    print(10 / 0)
except ZeroDivisionError:
    print("Delen door nul is niet toegestaan!")

# 3. Meerdere excepties
try:
    getal = int("abc")
except ValueError:
    print("Ongeldige invoer!")
except Exception as e:
    print("Onbekende fout:", e)

# 4. else-blok
try:
    getal = int(input("Voer een getal in: "))
except ValueError:
    print("Dat is geen getal!")
else:
    print("Je voerde in:", getal)

# 5. finally-blok
try:
    bestand = open("data.txt", "r")
except FileNotFoundError:
    print("Bestand niet gevonden!")
finally:
    print("Probeer voltooid.")

# 6. Eigen exceptie
try:
    leeftijd = int(input("Leeftijd: "))
    if leeftijd < 0:
        raise ValueError("Leeftijd kan niet negatief zijn!")
except ValueError as e:
    print("Fout:", e)

# 7. Combinatie
try:
    x = int(input("Eerste getal: "))
    y = int(input("Tweede getal: "))
    print("Resultaat:", x / y)
except ZeroDivisionError:
    print("Je kunt niet door nul delen!")
except ValueError:
    print("Alleen cijfers zijn toegestaan.")

# 8. try in functie
def deel(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Kan niet delen door nul!"
print(deel(10, 0))

# 9. foutmelding tonen
try:
    a = int("abc")
except Exception as e:
    print("Foutmelding:", e)

# 10. raise gebruiken
def controleer_getal(x):
    if x < 0:
        raise ValueError("Negatieve getallen niet toegestaan!")
    else:
        print("Getal is geldig:", x)
try:
    controleer_getal(-5)
except ValueError as e:
    print("Fout:", e)
