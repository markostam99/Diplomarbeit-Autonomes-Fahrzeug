import time
from hardware.button import is_pressed, shutdown

DOUBLE_PRESS_TIME = 0.5

def wait_release():
    while is_pressed():
        time.sleep(0.01)

try:
    print("Bereit für Tastentest")
    print("1x oder 2x drücken")

    while True:
        if is_pressed():
            #Erste Tasterbetätigung
            wait_release()

            press_count = 1
            start_time = time.time()

            #Auf zweite Tasterbetätigung warten
            while time.time() - start_time < DOUBLE_PRESS_TIME:
                if is_pressed():
                    wait_release()
                    press_count = 2
                    break

                time.sleep(0.01)

            if press_count == 1:
                print("1x erkannt -> BLAU")

            elif press_count == 2:
                print("2x erkannt -> ORANGE")

            time.sleep(0.3)

        time.sleep(0.01)

except KeyboardInterrupt:
    print("\nTest beendet")

finally:
    shutdown()