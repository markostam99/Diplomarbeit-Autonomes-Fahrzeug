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

# HSV-Bereich Orange
orange_unten = np.array([3, 120, 120])
orange_oben = np.array([12, 255, 255])

# Farbmaske erstellen
maske_orange = cv2.inRange(hsv, orange_unten, orange_oben)

# Orange Pixel zählen
orange_pixel = cv2.countNonZero(maske_orange)

# HSV-Werte der erkannten orangen Pixel
erkannte_pixel = hsv[maske_orange > 0]

print("-----------------------------")
print(f"Erkannte orange Pixel: {orange_pixel}")

if len(erkannte_pixel) > 0:
    median = np.median(erkannte_pixel, axis=0)

    print(f"H: {median[0]:.1f}")
    print(f"S: {median[1]:.1f}")
    print(f"V: {median[2]:.1f}")
else:
    print("Keine orangen Pixel erkannt.")

print("-----------------------------")