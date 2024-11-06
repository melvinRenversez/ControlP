import subprocess
import pygetwindow as gw

def say(text):
    print(text)

def getIsRunning():
    print("Running")
    windows = gw.getAllTitles()

    # Filtrer et afficher les fenêtres visibles qui ont un titre non vide
    fenetres_ouvertes = [title for title in windows if title]
    return fenetres_ouvertes