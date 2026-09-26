from hardware.motor import set_motors, stop
from config import PWM_SL, PWM_SR
from config import PWM_CLL, PWM_CLR, PWM_CRL, PWM_CRR, C_TIME

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
