import time

from hardware.camera import start, capture_frame, shutdown
from vision.image_processing import preprocess
from vision.obstacle_detection import detect_red, detect_green


try:
    #Kamera starten
    start()
    time.sleep(2)

    print("Hinderniserkennungstest gestartet")

    while True:
        #Kamerabild aufnehmen
        frame = capture_frame()

        #Bild vorverarbeiten
        hsv = preprocess(frame)

        #Hindernisse prüfen
        if detect_red(hsv):
            print("Rot erkannt")

        elif detect_green(hsv):
            print("Grün erkannt")

        else:
            print("Kein Hindernis")

        time.sleep(0.1)

finally:
    shutdown()