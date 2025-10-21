# ✅ Oplossingen – Les 11: Foutafhandeling

# 1. ZeroDivisionError
try:
    print(5 / 0)
except ZeroDivisionError:
    print("Delen door nul is niet toegestaan!")

# 2. Ongeldige invoer
try:
    getal = int("abc")
except ValueError:
    print("Dat is geen geldig getal!")

# 3. try/except/else
try:
    getal = int(input("Voer een getal in: "))
except ValueError:
    print("Ongeldige invoer.")
else:
    print("Je invoer was:", getal)

# 4. finally
try:
    bestand = open("test.txt", "r")
except FileNotFoundError:
    print("Bestand niet gevonden.")
finally:
    print("Einde van programma.")

# 5. deel(a, b)
def deel(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Kan niet delen door nul!"
print(deel(10, 0))

# 6. raise bij negatieve leeftijd
try:
    leeftijd = int(input("Leeftijd: "))
    if leeftijd < 0:
        raise ValueError("Leeftijd mag niet negatief zijn!")
except ValueError as e:
    print("Fout:", e)

# 7. Meerdere excepties
try:
    x = int(input("Eerste getal: "))
    y = int(input("Tweede getal: "))
    print("Resultaat:", x / y)
except ZeroDivisionError:
    print("Delen door nul!")
except ValueError:
    print("Alleen cijfers invoeren aub.")

# 8. Exception als e
try:
    a = int("abc")
except Exception as e:
    print("Foutmelding:", e)

# 9. Bestand openen met fout
try:
    with open("onbestaand.txt", "r") as f:
        print(f.read())
except FileNotFoundError:
    print("Bestand niet gevonden!")

# 10. controleer_getal()
def controleer_getal(x):
    if x < 0:
        raise ValueError("Negatieve getallen niet toegestaan!")
    else:
        print("Getal is geldig:", x)
try:
    controleer_getal(-10)
except ValueError as e:
    print("Fout:", e)
