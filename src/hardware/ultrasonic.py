import lgpio
import time

from config import US_LEFT, US_RIGHT

#GPIO Chip öffnen
h = lgpio.gpiochip_open(0)

def measure(pin):
    lgpio.gpio_claim_output(h, pin)

    #Ultraschallimpuls senden
    lgpio.gpio_write(h, pin, 1)
    time.sleep(0.00001)
    lgpio.gpio_write(h, pin, 0)

    #GPIO als Eingang verwenden
    lgpio.gpio_free(h, pin)
    lgpio.gpio_claim_input(h, pin)

    while lgpio.gpio_read(h, pin) == 0:
        pass

    start = time.time()

    while lgpio.gpio_read(h, pin) == 1:
        pass

    end = time.time()

    return (end - start) * 34300 / 2 

def get_left():
    #Abstand links messen
    return measure(US_LEFT) 

def get_right():
    #Abstand rechts messen
    return measure(US_RIGHT)

def shutdown():
    #GPIO freigeben
    lgpio.gpio_free(h, US_LEFT)
    lgpio.gpio_free(h, US_RIGHT)

    #GPIO Chip schliessen
    lgpio.gpiochip_close(h) 
