import time

from hardware.button import is_pressed, shutdown


print("Tastertest gestartet")

try:
    while True:
        if is_pressed():
            print("Taster gedrückt")
            time.sleep(0.3)

finally:
    shutdown()