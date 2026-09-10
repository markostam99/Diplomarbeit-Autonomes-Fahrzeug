import cv2
import numpy as np
import os

# Referenzbild laden
bild_pfad = "bilder/referenzbilder/orange_kurve4_nah.jpg"
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

# Vorläufiger HSV-Bereich für Orange
orange_unten = np.array([3, 120, 120])
orange_oben = np.array([12, 255, 255])

# Farbmaske erstellen
maske_orange = cv2.inRange(hsv, orange_unten, orange_oben)

# Ausgabeordner erstellen
os.makedirs("bilder/farbmaske", exist_ok=True)

# Farbmaske speichern
ausgabe = "bilder/farbmaske/maske_orange_kurve4_nah.jpg"
cv2.imwrite(ausgabe, maske_orange)

print(f"Farbmaske erstellt: {ausgabe}")