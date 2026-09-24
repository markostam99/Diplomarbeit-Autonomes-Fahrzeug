import time

from hardware.led import green_on, red_on, leds_off, shutdown


try:
    #Grüne LED einschalten
    green_on()
    print("Grüne LED leuchtet")
    time.sleep(3)

    #Rote LED einschalten
    red_on()
    print("Rote LED leuchtet")
    time.sleep(3)

    #LEDs ausschalten
    leds_off()
    print("LEDs ausgeschaltet")

finally:
    shutdown()