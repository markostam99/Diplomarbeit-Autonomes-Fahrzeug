import time
from hardware.motor import set_motors, stop
from config import PWM_SL, PWM_SR
from config import PWM_CLL, PWM_CLR, PWM_CRL, PWM_CRR, C_TIME
from config import PWM_CORH, PWM_CORL, CORR_TIME
from config import EV_L1_L, EV_L1_R, EV_L1_TIME
from config import EV_L2_L, EV_L2_R, EV_L2_TIME
from config import EV_L3_L, EV_L3_R, EV_L3_TIME
from config import EV_R1_L, EV_R1_R, EV_R1_TIME
from config import EV_R2_L, EV_R2_R, EV_R2_TIME
from config import EV_R3_L, EV_R3_R, EV_R3_TIME

def drive_straight():
    #Geradeausfahrt
    set_motors(PWM_SL, PWM_SR)

def turn_left():
    #90 Grad Linkskurve
    set_motors(PWM_CLL, PWM_CLR)
    time.sleep(C_TIME)
    stop()

def turn_right():
    #90 Grad Rechtskurve
    set_motors(PWM_CRL, PWM_CRR)
    time.sleep(C_TIME)
    stop()

def correct_left():
    #Fahrtrichtung nach links korrigieren
    set_motors(PWM_CORL, PWM_CORH)
    time.sleep(CORR_TIME)

def correct_right():
    #Fahrtrichtung nach rechts korrigieren
    set_motors(PWM_CORH, PWM_CORL)
    time.sleep(CORR_TIME)

def evade_left():
    #Nach links ausweichen
    set_motors(EV_L1_L, EV_L1_R)
    time.sleep(EV_L1_TIME)

    #Nach rechts ausrichten
    set_motors(EV_L2_L, EV_L2_R)
    time.sleep(EV_L2_TIME)

    #Endkorrektur
    set_motors(EV_L3_L, EV_L3_R)
    time.sleep(EV_L3_TIME)

    stop()

def evade_right():
    #Nach rechts ausweichen
    set_motors(EV_R1_L, EV_R1_R)
    time.sleep(EV_R1_TIME)

    #Nach links ausrichten
    set_motors(EV_R2_L, EV_R2_R)
    time.sleep(EV_R2_TIME)

    #Endkorrektur
    set_motors(EV_R3_L, EV_R3_R)
    time.sleep(EV_R3_TIME)

    stop()
