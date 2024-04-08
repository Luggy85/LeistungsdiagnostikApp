from load_data import sorted_power_W
import matplotlib.pyplot as plt


plt.plot(sorted_power_W[::-1])
plt.xlabel('Dauerlinie in Sekunden')
plt.ylabel('Leistung in W')
plt.grid(True)
plt.show()

