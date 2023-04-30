import numpy as np
import matplotlib.pyplot as plt

# Generiere 1000 Zufallszahlen im Bereich von [-100, -100] bis [100,100]
x = np.random.uniform(-100, 100, 1000)
y = np.random.uniform(-100, 100, 1000)

# Erstelle einen Farbverlauf von 0 bis 1 für die Farben
colors = np.random.rand(1000)

# Plotten der Zufallszahlen mit verschiedenen Farben
plt.scatter(x, y, c=colors, cmap='rainbow')
plt.xlabel('X-Achse')
plt.ylabel('Y-Achse')
plt.title('Zufallszahlen mit verschiedenen Farben')
plt.show()