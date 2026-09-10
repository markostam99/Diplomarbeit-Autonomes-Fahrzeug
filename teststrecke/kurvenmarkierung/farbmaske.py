import cv2
import numpy as np
import os

# Referenzbild laden
bild_pfad = "bilder/referenzbilder/blau_schraeg_rechts.jpg"
bild = cv2.imread(bild_pfad)

if bild is None:
    print("Bild konnte nicht geladen werden.")
    exit()

# Bildgrösse bestimmen
hoehe, breite = bild.shape[:2]

# Relevanter Bildbereich: untere 67 %
y_start = int(hoehe * 0.33)
roi = bild[y_start:hoehe, 0:breite]

# ROI von BGR nach HSV umwandeln
hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)

# Vorläufiger HSV-Bereich für Blau
blau_unten = np.array([108, 120, 70])
blau_oben = np.array([118, 255, 130])

# Farbmaske erstellen
maske_blau = cv2.inRange(hsv, blau_unten, blau_oben)

# Ausgabeordner erstellen
os.makedirs("bilder/farbmaske", exist_ok=True)

# Farbmaske speichern
ausgabe = "bilder/farbmaske/maske_blau_schraeg_rechts.jpg"
cv2.imwrite(ausgabe, maske_blau)

print(f"Farbmaske erstellt: {ausgabe}")