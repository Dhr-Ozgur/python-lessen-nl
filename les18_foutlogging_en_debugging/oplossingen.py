# ✅ Oplossingen – Les 18: Foutlogging en Debugging

import logging

# 1. Startmelding
logging.basicConfig(level=logging.INFO)
logging.info("Programma gestart.")

# 2. Drie niveaus
logging.warning("Waarschuwing!")
logging.error("Foutmelding!")
logging.critical("Kritieke fout!")

# 3. try/except met logging
try:
    5 / 0
except ZeroDivisionError:
    logging.exception("Delen door nul is niet toegestaan!")

# 4. Functie met logging
def deel(a, b):
    try:
        return a / b
    except Exception as e:
        logging.error(f"Fout: {e}")
        return None
print(deel(10, 0))

# 5. Logging naar bestand
logging.basicConfig(
    filename="app.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
logging.info("Logbestand gestart.")

# 6. Logbestand lezen
with open("app.log", "r") as f:
    regels = f.readlines()
print("Aantal regels:", len(regels))

# 7. Debugging
x, y = 10, 2
logging.debug(f"x={x}, y={y}, resultaat={x/y}")

# 8. Lus met fouten
for i in range(3):
    try:
        print(10 / (2 - i))
    except ZeroDivisionError as e:
        logging.error(f"Fout in iteratie {i}: {e}")

# 9. Custom format
logging.basicConfig(format="%(levelname)s | %(message)s", level=logging.WARNING)
logging.warning("Test waarschuwing met aangepast format.")

# 10. Einde
logging.info("Programma beëindigd.")
