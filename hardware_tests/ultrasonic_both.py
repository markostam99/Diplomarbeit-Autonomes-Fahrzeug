import lgpio
import time

PIN_LEFT = 17
PIN_RIGHT = 27
chip = lgpio.gpiochip_open(0)

def messen(pin):
    lgpio.gpio_claim_output(chip, pin)

    lgpio.gpio_write(chip, pin, 1)
    time.sleep(0.00001)
    lgpio.gpio_write(chip, pin, 0)

    lgpio.gpio_free(chip, pin)
    lgpio.gpio_claim_input(chip, pin)

    while lgpio.gpio_read(chip, pin) == 0:
        pass

    start = time.time()

    while lgpio.gpio_read(chip, pin) == 1:
        pass

    ende = time.time()

    return (ende - start) * 34300 / 2


while True:
    links = messen(PIN_LEFT)

    time.sleep(0.05)

    rechts = messen(PIN_RIGHT)

    print(f"Links: {links:.1f} cm | Rechts: {rechts:.1f} cm")

    time.sleep(0.5)