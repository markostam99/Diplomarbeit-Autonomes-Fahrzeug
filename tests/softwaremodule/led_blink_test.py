from hardware.led import green_blink, red_blink, leds_off, shutdown
import time

try:
    print("Grüne LED blinkt")
    for _ in range(3):
        green_blink()

    leds_off()
    time.sleep(1)

    print("Rote LED blinkt")
    for _ in range(3):
        red_blink()

    leds_off()

finally:
    shutdown()