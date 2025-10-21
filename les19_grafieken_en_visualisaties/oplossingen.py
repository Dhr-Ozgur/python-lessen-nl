# ✅ Oplossingen – Les 19: Grafieken en Visualisaties

import matplotlib.pyplot as plt

# 1. Lijngrafiek
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
plt.plot(x, y)
plt.show()

# 2. Labels
plt.plot(x, y)
plt.title("Voorbeeldgrafiek")
plt.xlabel("Tijd (s)")
plt.ylabel("Waarde")
plt.show()

# 3. Meerdere lijnen
y2 = [1, 3, 5, 7, 9]
plt.plot(x, y, label="Lijn 1")
plt.plot(x, y2, label="Lijn 2")
plt.legend()
plt.show()

# 4. Staafdiagram
producten = ["Appels", "Bananen", "Sinaasappels"]
prijzen = [3, 2, 4]
plt.bar(producten, prijzen)
plt.title("Prijzen per product")
plt.show()

# 5. Horizontale staafdiagram
plt.barh(producten, prijzen, color="purple")
plt.title("Horizontale weergave")
plt.show()

# 6. Cirkeldiagram
labels = ["Python", "Java", "C++", "JavaScript"]
aandeel = [40, 30, 20, 10]
plt.pie(aandeel, labels=labels, autopct="%1.1f%%")
plt.title("Talenverdeling")
plt.show()

# 7. Scatter plot
x = [2, 4, 6, 8]
y = [5, 7, 9, 11]
plt.scatter(x, y)
plt.title("Scatter plot")
plt.show()

# 8. Opslaan
plt.plot([1, 2, 3], [3, 4, 5])
plt.savefig("mijngrafiek.png")
print("Grafiek opgeslagen!")

# 9. Kleuren en stijl
plt.plot(x, y, color="red", linestyle="--", marker="s")
plt.title("Stijlvolle grafiek")
plt.show()

# 10. Subplots
plt.subplot(1, 2, 1)
plt.plot([1, 2, 3], [3, 4, 5])
plt.title("Lijn")

plt.subplot(1, 2, 2)
plt.bar(["A", "B", "C"], [5, 7, 3])
plt.title("Staafdiagram")

plt.tight_layout()
plt.show()
