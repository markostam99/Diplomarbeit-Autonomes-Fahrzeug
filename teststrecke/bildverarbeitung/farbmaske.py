import cv2
import numpy as np
import os

# Referenzbild laden
bild_pfad = "bilder/referenzbilder/gruen_hindernis4.jpg"
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

# Vorläufiger HSV-Bereich für Grün
gruen_unten = np.array([60, 100, 30])
gruen_oben = np.array([70, 255, 150])

# Farbmaske erstellen
maske_gruen = cv2.inRange(
    hsv,
    gruen_unten,
    gruen_oben
)

# Ausgabeordner erstellen
os.makedirs("bilder/farbmaske", exist_ok=True)

# Farbmaske speichern
ausgabe = "bilder/farbmaske/maske_gruen_hindernis4.jpg"
cv2.imwrite(ausgabe, maske_gruen)

print(f"Farbmaske erstellt: {ausgabe}")