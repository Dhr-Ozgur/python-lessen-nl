# 🧩 Les 9 – Modules en Imports

Welkom bij les 9 van de **Python Lessenreeks**!  
In deze les leer je hoe je **modules** kunt gebruiken om je code te organiseren en herbruikbaar te maken.  
Een module is gewoon een ander Python-bestand dat functies, variabelen of klassen bevat.

---

## 🎯 Leerdoelen
- Wat een module is begrijpen  
- De standaardmodules van Python gebruiken  
- De sleutelwoorden `import`, `from`, en `as` leren  
- Eigen modules maken en importeren  
- De voordelen van modulaire code begrijpen  

---

## 💻 Voorbeelden

### Voorbeeld 1 – Een module importeren
```python
import math
print(math.pi)
```

### Voorbeeld 2 – Een specifieke functie importeren
```python
from math import sqrt
print(sqrt(25))
```

### Voorbeeld 3 – Een alias gebruiken
```python
import math as m
print(m.pow(2, 3))
```

### Voorbeeld 4 – Meerdere functies importeren
```python
from math import sin, cos
print(sin(0))
print(cos(0))
```

### Voorbeeld 5 – Eigen module maken
**bestand:** `mijn_module.py`
```python
def groet():
    print("Hallo uit mijn module!")
```
**hoofdbestand:**
```python
import mijn_module
mijn_module.groet()
```

### Voorbeeld 6 – Alias met eigen module
```python
import mijn_module as mm
mm.groet()
```

### Voorbeeld 7 – Random-module
```python
import random
print(random.randint(1, 10))
```

### Voorbeeld 8 – Tijdmodule
```python
import time
print("Start...")
time.sleep(2)
print("Einde!")
```

### Voorbeeld 9 – OS-module
```python
import os
print(os.name)
```

### Voorbeeld 10 – Combinatie van modules
```python
import random, math
getal = random.randint(1, 100)
wortel = math.sqrt(getal)
print(f"De wortel van {getal} is {round(wortel, 2)}")
```

---

## 🧠 Uitleg
- **`import math`** laadt de hele module.  
- **`from math import sqrt`** laadt één specifieke functie.  
- **`as`** maakt een kortere alias voor gemak.  
- Eigen modules zijn gewoon `.py`-bestanden in dezelfde map.  

---

## 🧩 Opdrachten
Zie `opdrachten.md` voor 10 oefeningen met modules en imports.

---

## ✅ Oplossingen
Bekijk `oplossingen.py` voor de uitgewerkte antwoorden.
