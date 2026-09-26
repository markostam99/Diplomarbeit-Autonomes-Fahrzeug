import time

from hardware.camera import start, capture_frame, shutdown
from vision.image_processing import preprocess
from vision.curve_detection import detect_blue, detect_orange


try:
    #Kamera starten
    start()
    time.sleep(2)

    print("Kurvenmarkierungstest gestartet")

    while True:
        #Kamerabild aufnehmen
        frame = capture_frame()

        #Bild vorverarbeiten
        hsv = preprocess(frame)

        #Kurvenmarkierungen prüfen
        if detect_blue(hsv):
            print("Blau erkannt")

        elif detect_orange(hsv):
            print("Orange erkannt")

        else:
            print("Keine Kurvenmarkierung")

        time.sleep(0.1)

finally:
    shutdown()