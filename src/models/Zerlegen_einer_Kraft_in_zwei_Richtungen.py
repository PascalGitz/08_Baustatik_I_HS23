# -*- coding: utf-8 -*-
"""
Created on Fri Sep 15 13:32:44 2023

@author: Daniel Heinzmann, Pascal Gitz
"""
# Importieren der erforderlichen Programmbibliothek
import numpy as np

## Eingabewerte der gegebenen Kraft
F= 631.24 #[Krafteinheit]
phi_F= 346.62 # in Grad von Richtung x aus positiv zur Richtung y

## Gewünschte Richtungswinkel zur Richtung a und b der zerlegten Kraft
phi_a= 19.5 # in Grad von Richtung x aus positiv zur Richtung y
phi_b= 55 # in Grad von Richtung x aus positiv zur Richtung y

## Berechnete Komponenten F_a und F_b der zerlegten Kraft
F_a = F/(np.cos(phi_a*np.pi/180)*np.sin(phi_b*np.pi/180) - np.cos(phi_b*np.pi/180)*np.sin(phi_a*np.pi/180)) * (np.sin(phi_b*np.pi/180)*np.cos(phi_F*np.pi/180) - np.cos(phi_b*np.pi/180)*np.sin(phi_F*np.pi/180))
print("F_a =",F_a, "[Krafteinheit]")

F_b = F/(np.cos(phi_a*np.pi/180)*np.sin(phi_b*np.pi/180) - np.cos(phi_b*np.pi/180)*np.sin(phi_a*np.pi/180)) * (-np.sin(phi_a*np.pi/180)*np.cos(phi_F*np.pi/180) + np.cos(phi_a*np.pi/180)*np.sin(phi_F*np.pi/180))
print("F_b =",F_b, "[Krafteinheit]")