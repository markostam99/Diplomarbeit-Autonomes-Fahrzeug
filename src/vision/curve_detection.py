import cv2 
import numpy as np
from config import BLUE_LOWER, BLUE_UPPER, BLUE_PX
from config import ORANGE_LOWER, ORANGE_UPPER, ORANGE_PX

def detect_blue(hsv):
    #Farbmaske für Blau erstellen
    mask = cv2.inRange(hsv, np.array(BLUE_LOWER), np.array(BLUE_UPPER))

    #Blaue Pixel zählen
    pixels = cv2.countNonZero(mask)

    #Schwellenwert prüfen
    return pixels >= BLUE_PX 

def detect_orange(hsv):
    #Farbmaske für Orange erstellen
    mask = cv2.inRange(hsv, np.array(ORANGE_LOWER), np.array(ORANGE_UPPER))

    #Orange Pixel zählen
    pixels = cv2.countNonZero(mask)

    #Schwellenwert prüfen
    return pixels >= ORANGE_PX
