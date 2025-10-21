# Voorbeelden – Les 9: Modules en Imports

# 1. import math
import math
print(math.pi)

# 2. from math import sqrt
from math import sqrt
print(sqrt(16))

# 3. alias gebruiken
import math as m
print(m.pow(2, 4))

# 4. meerdere functies
from math import sin, cos
print(sin(0))
print(cos(0))

# 5. eigen module (voorbeeld)
# bestand: mijn_module.py
# def groet():
#     print("Hallo uit mijn module!")

import mijn_module
mijn_module.groet()

# 6. alias met eigen module
import mijn_module as mm
mm.groet()

# 7. random-module
import random
print(random.randint(1, 10))

# 8. time-module
import time
print("Start...")
time.sleep(1)
print("Einde!")

# 9. os-module
import os
print("OS:", os.name)

# 10. combinatie van modules
getal = random.randint(1, 100)
wortel = math.sqrt(getal)
print(f"De wortel van {getal} is {round(wortel, 2)}")
