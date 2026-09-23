# GPIO Belegung
# Ultraschallsensoren
US_LEFT = 17
US_RIGHT = 27

# Motortreiber
AIN1 = 5
AIN2 = 6
PWMA = 12

BIN1 = 23
BIN2 = 24
PWMB = 13

STBY = 22

# Status-LED
LED_RED = 16
LED_GREEN = 20

# Starttaster
BUTTON = 21


# Fahrparameter
# PWM
PWM_FREQ = 1000

# Geradeausfahrt
PWM_SL = 70
PWM_RL = 71

# 90-Grad Kurve
# Linkskurve
PWM_CLL = 10
PWM_CLR = 73

# Rechtskurve
PWM_CRL = 73
PWM_CRR = 10

# Kurvendauer
C_TIME = 1.0

# Wandkorrektur
WALL_DIST = 10

# Ansteuerung High/Low
PWM_CORH = 75
PWM_CORL = 45

# Korrekturzeit
CORR_TIME = 0.25


# Ausweichmanöver
# Ausweichen links
# Links ausweichen
EV_L1_L = 40
EV_L1_R = 76
EV_L1_TIME = 1.0

# Rechts ausrichten
EV_L2_L = 75
EV_L2_R = 40
EV_L2_TIME = 1.9

# Endkorrektur
EV_L3_L = 40
EV_L3_R = 76
EV_L3_TIME = 1.0

# Ausweichen Rechts
# Rechts ausweichen
EV_R1_L = 75
EV_R1_R = 40
EV_R1_TIME = 1.0

# Links ausrichten
EV_R2_L = 40
EV_R2_R = 76
EV_R2_TIME = 1.9

# Endkorrektur
EV_R3_L = 75
EV_R3_R = 40
EV_R3_TIME = 1.0


# Kamera
# Auflösung
CAM_WIDTH = 640
CAM_HEIGHT = 480

# ROI
ROI_START = 0.33  


# Kurvenmarkierung
# Blau
BLUE_LOWER = [108, 80, 40]
BLUE_UPPER = [118, 255, 255]
BLUE_PX = 15000

# Orange
ORANGE_LOWER = [3, 120, 120]
ORANGE_UPPER = [12, 255, 255]
ORANGE_PX = 13000

# Verzögerung nach Erkennung
CURVE_DELAY = 0.8 


# Hinderniserkennung
# Rot
RED_LOWER1 = [0, 180, 70]
RED_UPPER1 = [5, 255, 180]

RED_LOWER2 = [175, 180, 70]
RED_UPPER2 = [179, 255, 180]

RED_PX = 12000

#Grün
GREEN_LOWER = [60, 100, 30]
GREEN_UPPER = [5, 255, 180]

GREEN_PX = 8000
