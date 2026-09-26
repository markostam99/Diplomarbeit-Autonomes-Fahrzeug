import time
import cv2

from hardware.camera import start, capture_frame, shutdown


try:
    #Kamera starten
    start()
    time.sleep(2)

    #Kamerabild aufnehmen
    frame = capture_frame()

    #Bild speichern
    cv2.imwrite("camera_test.jpg", frame)

    print("Kamerabild erfolgreich aufgenommen.")

finally:
    shutdown()