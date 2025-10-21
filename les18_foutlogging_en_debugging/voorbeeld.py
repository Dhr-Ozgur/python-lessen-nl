# Voorbeelden – Les 18: Foutlogging en Debugging

import logging

# 1. Basis logging
logging.basicConfig(level=logging.INFO)
logging.info("Programma gestart.")

# 2. Niveaus
logging.debug("Debug info")
logging.info("Info bericht")
logging.warning("Waarschuwing!")
logging.error("Er is een fout opgetreden")
logging.critical("Kritieke fout!")

# 3. Logging naar bestand
logging.basicConfig(
    filename="app.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
logging.info("Bestand logging actief.")

# 4. try/except met logging
try:
    10 / 0
except ZeroDivisionError:
    logging.exception("Delen door nul fout!")

# 5. Variabelen debuggen
x, y = 10, 2
logging.debug(f"x={x}, y={y}, resultaat={x/y}")

# 6. Functie met logging
def deel(a, b):
    try:
        return a / b
    except Exception as e:
        logging.error(f"Fout in functie: {e}")
        return None
print(deel(10, 0))

# 7. Iteratie met foutlogging
for i in range(3):
    try:
        print(10 / (2 - i))
    except ZeroDivisionError as e:
        logging.error(f"Fout in iteratie {i}: {e}")

# 8. Logbestand lezen
with open("app.log", "r") as f:
    regels = f.readlines()
print("Aantal logregels:", len(regels))

# 9. Custom format
logging.basicConfig(format="%(levelname)s | %(message)s", level=logging.WARNING)
logging.warning("Aangepaste waarschuwing.")

# 10. Einde
logging.info("Programma beëindigd.")
