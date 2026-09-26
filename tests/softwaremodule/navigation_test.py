import time

from control.navigation import correct_left, correct_right, evade_left, evade_right
from hardware.motor import stop, shutdown


try:
    #Korrektur nach links
    print("Korrektur nach links")
    correct_left()
    stop()
    time.sleep(2)

    #Korrektur nach rechts
    print("Korrektur nach rechts")
    correct_right()
    stop()
    time.sleep(2)

    #Ausweichen nach links
    print("Ausweichen nach links")
    evade_left()
    time.sleep(2)

    #Ausweichen nach rechts
    print("Ausweichen nach rechts")
    evade_right()

finally:
    stop()
    shutdown()