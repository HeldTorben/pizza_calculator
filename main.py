import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.interpolate import interp1d

# Gegebene Daten (Durchmesser in cm, Preis in €)
durchmesser_daten = np.array([20, 26, 30, 45, 50])
preis_daten = np.array([4, 11, 12, 24, 29])

# Interpolation der Preise (kubisch für Glätte)
preis_funktion = interp1d(durchmesser_daten, preis_daten, kind='cubic', fill_value='extrapolate')

# Erzeugung von Werten für Durchmesser und Krustendicke
durchmesser = np.linspace(20, 50, 100)
kruste = np.linspace(0.5, 2.5, 100)

# Meshgrid für 3D-Daten
D, K = np.meshgrid(durchmesser, kruste)

# Preis für jeden Durchmesser
preise = preis_funktion(D)

# Radien
r_gesamt = D / 2
r_belag = np.maximum(r_gesamt - K, 0.00001)  # Sicherheitsgrenze, damit Fläche nicht 0 wird

# Belegte Fläche ohne Rand
fläche_belag = np.pi * r_belag**2

# Preis pro cm² belegter Fläche
P = preise / fläche_belag

# Plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
surf = ax.plot_surface(D, K, P, cmap='viridis')

ax.set_title('Preis pro cm² (nur belegte Fläche)')
ax.set_xlabel('Durchmesser (cm)')
ax.set_ylabel('Krustendicke (cm)')
ax.set_zlabel('Preis pro cm² (€)')

fig.colorbar(surf, shrink=0.5, aspect=10, label='€/cm²')
plt.show()
