import time

from hardware.ultrasonic import get_left, get_right, shutdown


try:
    while True:
        #Linken Sensor auslesen
        left = get_left()

        time.sleep(0.05)

        #Rechten Sensor auslesen
        right = get_right()

        #Messwerte prüfen
        if left is None:
            left_text = "Kein Messwert"
        else:
            left_text = f"{left:.1f} cm"

        if right is None:
            right_text = "Kein Messwert"
        else:
            right_text = f"{right:.1f} cm"

        #Messwerte ausgeben
        print(f"Links: {left_text} | Rechts: {right_text}")

        time.sleep(0.5)

finally:
    shutdown()