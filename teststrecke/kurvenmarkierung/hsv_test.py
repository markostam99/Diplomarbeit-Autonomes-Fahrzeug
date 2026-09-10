import cv2
import numpy as np
import os

bild_pfad = "bilder/blau_mittel.jpg"

bild = cv2.imread(bild_pfad)

if bild is None:
    print("Bild konnte nicht geladen werden.")
    exit()

# Bild in HSV umwandeln
hsv = cv2.cvtColor(bild, cv2.COLOR_BGR2HSV)

# Kleiner Testbereich auf der blauen Linie
# Diese vier Werte verschieben, bis das Rechteck richtig liegt...
x1, y1 = 1400, 1050
x2, y2 = 1550, 1070

bereich = hsv[y1:y2, x1:x2]

# Nur deutlich gesättigte Pixel berücksichtigen
saettigung = bereich[:, :, 1]
farbige_pixel = bereich[saettigung > 80]

if len(farbige_pixel) == 0:
    print("Keine ausreichend farbigen Pixel gefunden.")
else:
    median = np.median(farbige_pixel, axis=0)

    print("HSV-Wert Blau")
    print("----------------")
    print(f"H: {median[0]:.1f}")
    print(f"S: {median[1]:.1f}")
    print(f"V: {median[2]:.1f}")

# Kontrollbild mit Rechteck speichern
kontrollbild = bild.copy()

cv2.rectangle(
    kontrollbild,
    (x1, y1),
    (x2, y2),
    (0, 255, 0),
    3
)

os.makedirs("bilder/hsv_test", exist_ok=True)

cv2.imwrite(
    "bilder/hsv_test/hsv_blau_mittel.jpg",
    kontrollbild
)

print("Kontrollbild gespeichert.")