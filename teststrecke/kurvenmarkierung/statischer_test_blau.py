from picamera2 import Picamera2
import cv2
import numpy as np
import time

# Kamera starten
picam2 = Picamera2()

config = picam2.create_still_configuration(
    main={"format": "RGB888", "size": (640, 480)}
)

picam2.configure(config)
picam2.start()

time.sleep(2)

# Einzelnes Bild aufnehmen
bild = picam2.capture_array()

picam2.stop()

# Kamera ist um 180° montiert
bild = cv2.rotate(bild, cv2.ROTATE_180)

# ROI: untere 67 % des Bildes
hoehe, breite = bild.shape[:2]
y_start = int(hoehe * 0.33)
roi = bild[y_start:hoehe, 0:breite]

# BGR -> HSV
hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)

# HSV-Bereich für Blau
blau_unten = np.array([108, 80, 40])
blau_oben = np.array([118, 255, 255])

# Farbmaske erstellen
maske_blau = cv2.inRange(hsv, blau_unten, blau_oben)

# Blaue Pixel zählen
blaue_pixel = cv2.countNonZero(maske_blau)

# HSV-Werte der erkannten blauen Pixel
erkannte_pixel = hsv[maske_blau > 0]

print("-----------------------------")
print(f"Erkannte blaue Pixel: {blaue_pixel}")

if len(erkannte_pixel) > 0:
    median = np.median(erkannte_pixel, axis=0)

    print(f"H: {median[0]:.1f}")
    print(f"S: {median[1]:.1f}")
    print(f"V: {median[2]:.1f}")
else:
    print("Keine blauen Pixel erkannt.")

print("-----------------------------")