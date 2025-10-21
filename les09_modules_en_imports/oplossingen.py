# ✅ Oplossingen – Les 9: Modules en Imports

# 1. math.pi
import math
print(math.pi)

# 2. sqrt
from math import sqrt
print(sqrt(64))

# 3. alias
import math as m
print(m.pow(5, 2))

# 4. random getal
import random
print(random.randint(1, 10))

# 5. time.sleep
import time
print("Start...")
time.sleep(2)
print("Einde!")

# 6. os.name
import os
print("Besturingssysteem:", os.name)

# 7. eigen module
# bestand: mijn_module.py
# def groet():
#     print("Hallo vanuit mijn module!")

import mijn_module
mijn_module.groet()

# 8. random choice
from random import choice
dieren = ["kat", "hond", "vis", "vogel"]
print("Willekeurig dier:", choice(dieren))

# 9. math + random
import math, random
getal = random.randint(1, 100)
print("Getal:", getal)
print("Wortel:", round(math.sqrt(getal), 2))

# 10. eigen module berekening.py
# bestand berekening.py:
# def som(a, b):
#     return a + b
from berekening import som
print("Som is:", som(5, 7))
