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

# Kamera 180° Rotation
bild = cv2.rotate(bild, cv2.ROTATE_180)

# ROI
hoehe, breite = bild.shape[:2]
y_start = int(hoehe * 0.33)
roi = bild[y_start:hoehe, 0:breite]

# BGR -> HSV
hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)

# HSV-Bereich Grün
gruen_unten = np.array([60, 100, 30])
gruen_oben = np.array([70, 255, 150])

# Farbmaske erstellen
maske_gruen = cv2.inRange(
    hsv,
    gruen_unten,
    gruen_oben
)

# Grüne Pixel zählen
gruen_pixel = cv2.countNonZero(maske_gruen)

# HSV-Werte der erkannten grünen Pixel
erkannte_pixel = hsv[maske_gruen > 0]

print("-----------------------------")
print(f"Erkannte grüne Pixel: {gruen_pixel}")

if len(erkannte_pixel) > 0:
    median = np.median(erkannte_pixel, axis=0)

    print(f"H: {median[0]:.1f}")
    print(f"S: {median[1]:.1f}")
    print(f"V: {median[2]:.1f}")
else:
    print("Keine grünen Pixel erkannt.")

print("-----------------------------")