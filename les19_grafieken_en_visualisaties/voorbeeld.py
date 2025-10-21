# Voorbeelden – Les 19: Grafieken en Visualisaties

import matplotlib.pyplot as plt

# 1. Lijngrafiek
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
plt.plot(x, y)
plt.show()

# 2. Labels en titel
plt.plot(x, y)
plt.title("Eenvoudige Lijngrafiek")
plt.xlabel("X-as")
plt.ylabel("Y-as")
plt.show()

# 3. Meerdere lijnen
y2 = [1, 3, 5, 7, 9]
plt.plot(x, y, label="Lijn 1")
plt.plot(x, y2, label="Lijn 2")
plt.legend()
plt.show()

# 4. Staafdiagram
namen = ["Ozgur", "Emma", "Lars", "Sara"]
scores = [85, 90, 78, 95]
plt.bar(namen, scores)
plt.title("Scores per student")
plt.show()

# 5. Horizontaal
plt.barh(namen, scores, color="green")
plt.title("Horizontale staafdiagram")
plt.show()

# 6. Cirkeldiagram
labels = ["Python", "Java", "C++", "JavaScript"]
aandeel = [50, 20, 15, 15]
plt.pie(aandeel, labels=labels, autopct="%1.1f%%")
plt.title("Talenvoorkeur")
plt.show()

# 7. Scatter plot
x = [5, 7, 8, 10, 12]
y = [12, 14, 15, 18, 20]
plt.scatter(x, y)
plt.title("Puntenplot")
plt.show()

# 8. Opslaan
plt.plot([1, 2, 3], [3, 2, 5])
plt.savefig("grafiek.png")

# 9. Kleuren
plt.plot(x, y, color="red", linestyle="--", marker="o")
plt.title("Kleuren en markers")
plt.show()

# 10. Subplots
plt.subplot(1, 2, 1)
plt.plot([1, 2, 3], [3, 2, 1])
plt.title("Links")

plt.subplot(1, 2, 2)
plt.bar(["A", "B", "C"], [3, 7, 5])
plt.title("Rechts")

plt.tight_layout()
plt.show()
