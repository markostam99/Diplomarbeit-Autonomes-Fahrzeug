import time
import cv2

from hardware.camera import start, capture_frame, shutdown
from vision.image_processing import preprocess


try:
    #Kamera starten
    start()
    time.sleep(2)

    #Kamerabild aufnehmen
    frame = capture_frame()

    #Bild vorverarbeiten
    hsv = preprocess(frame)

    #HSV-Bild für Kontrolle zurück in BGR umwandeln
    test_image = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)

    #Testbild speichern
    cv2.imwrite("image_processing_test.jpg", test_image)

    print("Bildvorverarbeitung erfolgreich.")

finally:
    shutdown()