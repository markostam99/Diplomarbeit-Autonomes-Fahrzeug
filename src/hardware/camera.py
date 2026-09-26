from picamera2 import Picamera2
import cv2 
from config import CAM_WIDTH, CAM_HEIGHT

#Kamera initialisieren
picam2 = Picamera2()

config = picam2.create_preview_configuration(main={"format": "RGB888", "size": (CAM_WIDTH, CAM_HEIGHT)})

picam2.configure(config)

def start():
    #Kamera starten
    picam2.start()

def capture_frame():
    #Aktuelles Kamerabild aufnehmen
    frame = picam2.capture_array()

    #Bild um 180 Grad drehen
    frame = cv2.rotate(frame, cv2.ROTATE_180)

    return frame

def shutdown():
    #Kamera stoppen
    picam2.stop()

