import lgpio
import time

BUTTON = 21

h = lgpio.gpiochip_open(0)
lgpio.gpio_claim_input(h, BUTTON, lgpio.SET_PULL_UP)

print("Tastertest gestartet")

try:
    while True:
        if lgpio.gpio_read(h, BUTTON) == 0:
            print("Taster gedrückt")
            time.sleep(0.3)

finally:
    lgpio.gpiochip_close(h)