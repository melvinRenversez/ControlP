import psutil
import pygetwindow as gw

print("Running")
windows = gw.getAllTitles()

# Filtrer et afficher les fenêtres visibles qui ont un titre non vide
fenetres_ouvertes = [title for title in windows if title]

print(fenetres_ouvertes)

for x in fenetres_ouvertes:
    print(x)