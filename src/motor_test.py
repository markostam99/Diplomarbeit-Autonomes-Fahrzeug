import time

from hardware.motor import set_motors, stop, shutdown
from config import PWM_SL, PWM_RL


try:
    #Geradeausfahrt
    set_motors(PWM_SL, PWM_RL)
    time.sleep(3)

    #Motoren stoppen
    stop()

finally:
    shutdown()