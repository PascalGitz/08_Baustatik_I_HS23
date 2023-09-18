# -*- coding: utf-8 -*-
"""
Created on Fri Sep 15 13:32:44 2023

@author: Daniel Heinzmann, Pascal Gitz
"""
# Importieren der erforderlichen Programmbibliothek
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches




## Eingabewerte der gegebenen Kraft
F= 1 #[Krafteinheit]
phi_F= 70 # in Grad von Richtung x aus positiv zur Richtung y

## Gewünschte Richtungswinkel zur Richtung a und b der zerlegten Kraft
phi_a= 0 # in Grad von Richtung x aus positiv zur Richtung y
phi_b= 90 # in Grad von Richtung x aus positiv zur Richtung y




## Berechnete Komponenten F_a und F_b der zerlegten Kraft
F_a = F/(np.cos(phi_a*np.pi/180)*np.sin(phi_b*np.pi/180) - np.cos(phi_b*np.pi/180)*np.sin(phi_a*np.pi/180)) * (np.sin(phi_b*np.pi/180)*np.cos(phi_F*np.pi/180) - np.cos(phi_b*np.pi/180)*np.sin(phi_F*np.pi/180))
# print("F_a =",F_a, "[Krafteinheit]")

F_b = F/(np.cos(phi_a*np.pi/180)*np.sin(phi_b*np.pi/180) - np.cos(phi_b*np.pi/180)*np.sin(phi_a*np.pi/180)) * (-np.sin(phi_a*np.pi/180)*np.cos(phi_F*np.pi/180) + np.cos(phi_a*np.pi/180)*np.sin(phi_F*np.pi/180))
# print("F_b =",F_b, "[Krafteinheit]")




# Ploterstellung
fig, ax = plt.subplots()

# Kraft F
F_x = F * np.cos(np.radians(phi_F))
F_y = F * np.sin(np.radians(phi_F))

ax.quiver(0, 0, F_x, F_y, angles='xy', scale_units='xy', scale=1, color = 'green', label = f'$F = {round(F,1)}$')

# Zerlegte Kraft a
F_a_x = F_a * np.cos(np.radians(phi_a))
F_a_y = F_a * np.sin(np.radians(phi_a))

ax.quiver(0,0,F_a_x, F_a_y, angles='xy', scale_units='xy', scale=1, color= '0.2', label = f'$F_a = {round(F_a,1)}$')

# Zerlegte Kraft b
F_b_x = F_b * np.cos(np.radians(phi_b))
F_b_y = F_b * np.sin(np.radians(phi_b))

ax.quiver(0,0,F_b_x, F_b_y, angles='xy', scale_units='xy', scale=1, color= '0.5', label = f'$F_b = {round(F_b,1)}$')
## Versetzt an Endpunkt F_a
ax.quiver(F_a_x,F_a_y,F_b_x, F_b_y, angles='xy', scale_units='xy', scale=1, color= '0.8', label = '$F_b$ verschoben')

# Darstellung des Winkels
circle_radius = 0.2 * min(max(F_x, F_a_x, F_b_x), max(F_y, F_a_y, F_b_y))
ax.add_patch(patches.Wedge(center=(0, 0), r=circle_radius, theta1=0, theta2=phi_F, color='green', alpha=0.3))
ax.add_patch(patches.Wedge(center=(0, 0), r=circle_radius, theta1=0, theta2=phi_a, color='0.2', alpha=0.3))
ax.add_patch(patches.Wedge(center=(0, 0), r=circle_radius, theta1=0, theta2=phi_b, color='0.5', alpha=0.3))

# Plotgrenzen

if min(F,F_a,F_b) <= 0:
    ax.set_xlim(min(F,F_a,F_b)*1.1, max(F, F_a, F_b)*1.1)
    ax.set_ylim(min(F,F_a,F_b)*1.1, max(F, F_a, F_b)*1.1)

else:
    ax.set_xlim(0, max(F, F_a, F_b)*1.1)
    ax.set_ylim(0, max(F, F_a, F_b)*1.1)

# Optional: Beschriften Sie die Achsen
ax.set_xlabel('X-Achse')
ax.set_ylabel('Y-Achse')
ax.set_aspect('equal')
plt.legend()
plt.grid()
plt.show()

