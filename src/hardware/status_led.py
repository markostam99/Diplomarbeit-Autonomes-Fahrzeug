import lgpio

from config import LED_RED, LED_GREEN

#GPIO Chip öffnen
h = lgpio.gpiochip_open(0)

#LED GPIOs als Ausgang
lgpio.gpio_claim_output(h, LED_RED)
lgpio.gpio_claim_output(h, LED_GREEN)

def green_on():
    #Grüne LED einschalten
    lgpio.gpio_write(h, LED_RED, 0)
    lgpio.gpio_write(h, LED_GREEN, 1)

def red_on():
    #Rote LED einschalten
    lgpio.gpio_write(h, LED_RED, 1)
    lgpio.gpio_write(h, LED_GREEN, 0)

def leds_off():
    #LEDs ausschalten
    lgpio.gpio_write(h, LED_RED, 0)
    lgpio.gpio_write(h, LED_GREEN, 0)

def shutdown():
    #LEDs ausschalten
    leds_off()

    #GPIOs freigeben
    lgpio.gpio_free(h, LED_RED)
    lgpio.gpio_free(h, LED_GREEN)

    #GPIO Chip schliessen
    lgpio.gpiochip_close(h)
