# 📈 Les 19 – Grafieken en Visualisaties (Matplotlib)

Welkom bij les 19 van de **Python Lessenreeks**!  
In deze les leer je hoe je **grafieken en visualisaties** kunt maken met de module `matplotlib`.  
Met visualisaties kun je data beter begrijpen en presenteren.

---

## 🎯 Leerdoelen
- De bibliotheek `matplotlib.pyplot` gebruiken  
- Lijn-, staaf- en cirkeldiagrammen maken  
- Labels en titels toevoegen  
- Meerdere datasets combineren in één grafiek  
- Grafieken opslaan als afbeelding  

---

## 💻 Voorbeelden

### Voorbeeld 1 – Een eenvoudige lijn
```python
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

plt.plot(x, y)
plt.show()
```

### Voorbeeld 2 – Met labels en titel
```python
plt.plot(x, y)
plt.title("Eenvoudige Lijngrafiek")
plt.xlabel("X-as")
plt.ylabel("Y-as")
plt.show()
```

### Voorbeeld 3 – Meerdere lijnen
```python
x = [1, 2, 3, 4, 5]
y1 = [1, 2, 3, 4, 5]
y2 = [2, 3, 4, 5, 6]
plt.plot(x, y1, label="Dataset 1")
plt.plot(x, y2, label="Dataset 2")
plt.legend()
plt.show()
```

### Voorbeeld 4 – Staafdiagram
```python
namen = ["Ozgur", "Emma", "Lars", "Sara"]
scores = [85, 90, 78, 95]
plt.bar(namen, scores)
plt.title("Scores per student")
plt.show()
```

### Voorbeeld 5 – Horizontale staafdiagram
```python
plt.barh(namen, scores, color="orange")
plt.title("Horizontale staafdiagram")
plt.show()
```

### Voorbeeld 6 – Cirkeldiagram (pie chart)
```python
labels = ["Python", "Java", "C++", "JavaScript"]
aandeel = [50, 20, 15, 15]
plt.pie(aandeel, labels=labels, autopct="%1.1f%%")
plt.title("Programmeertaalvoorkeur")
plt.show()
```

### Voorbeeld 7 – Puntenplot (scatter)
```python
x = [5, 7, 8, 10, 12]
y = [12, 14, 15, 18, 20]
plt.scatter(x, y)
plt.title("Puntenplot")
plt.show()
```

### Voorbeeld 8 – Grafiek opslaan
```python
plt.plot([1, 2, 3], [4, 5, 6])
plt.savefig("grafiek.png")
print("Grafiek opgeslagen als grafiek.png")
```

### Voorbeeld 9 – Kleuren en stijlen
```python
plt.plot(x, y, color="red", linestyle="--", marker="o")
plt.title("Aangepaste stijl")
plt.show()
```

### Voorbeeld 10 – Subplots (meerdere grafieken)
```python
plt.subplot(1, 2, 1)
plt.plot([1, 2, 3], [3, 2, 1])
plt.title("Links")

plt.subplot(1, 2, 2)
plt.bar(["A", "B", "C"], [3, 7, 5])
plt.title("Rechts")

plt.tight_layout()
plt.show()
```

---

## 🧠 Uitleg
- **`plt.plot()`** → lijngrafiek  
- **`plt.bar()` / `plt.barh()`** → staafdiagram  
- **`plt.pie()`** → cirkeldiagram  
- **`plt.scatter()`** → puntenplot  
- **`plt.savefig()`** → grafiek opslaan als afbeelding  
- **`plt.legend()`, `plt.title()`, `plt.xlabel()`, `plt.ylabel()`** → grafieklabels  

---

## 🧩 Opdrachten
Zie `opdrachten.md` voor 10 oefeningen met visualisaties.

---

## ✅ Oplossingen
Bekijk `oplossingen.py` voor de uitgewerkte antwoorden.
