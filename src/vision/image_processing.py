import cv2 
from config import ROI_START

def preprocess(frame):
    #Bildgrösse bestimmen
    height, width = frame.shape[:2]

    #Bildbereich bestimmen
    y_start = int(height * ROI_START)

    #ROI ausschneiden
    roi = frame[y_start:height, 0:width]

    #ROI in HSV umwandeln
    hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)

    return hsv 
