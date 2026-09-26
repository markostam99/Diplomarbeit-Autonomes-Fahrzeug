import cv2 
import numpy as np
from config import RED_LOWER1, RED_UPPER1, RED_LOWER2, RED_UPPER2, RED_PX  
from config import GREEN_LOWER, GREEN_UPPER, GREEN_PX  

def detect_red(hsv):
    #Farbmasken für Rot erstellen
    mask1 = cv2.inRange(hsv, np.array(RED_LOWER1), np.array(RED_UPPER1))
    mask2 = cv2.inRange(hsv, np.array(RED_LOWER2), np.array(RED_UPPER2))

    #Farbmasken zusammenführen
    mask = cv2.bitwise_or(mask1, mask2)

    #Rote Pixel zählen
    pixels = cv2.countNonZero(mask)

    #Schwellenwert prüfen
    return pixels >= RED_PX

def detect_green(hsv):
    #Farbmaske für Grün erstellen
    mask = cv2.inRange(hsv, np.array(GREEN_LOWER), np.array(GREEN_UPPER))

    #Grüne Pixel zählen
    pixels = cv2.countNonZero(mask)

    #Schwellenwert prüfen
    return pixels >= GREEN_PX
