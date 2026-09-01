import lgpio
import time

PIN = 17
chip = lgpio.gpiochip_open(0)

while True:
    lgpio.gpio_claim_output(chip, PIN)

    lgpio.gpio_write(chip, PIN, 1)
    time.sleep(0.00001)
    lgpio.gpio_write(chip, PIN, 0)

    lgpio.gpio_free(chip, PIN)
    lgpio.gpio_claim_input(chip, PIN)

    while lgpio.gpio_read(chip, PIN) == 0:
        pass

    start = time.time()

    while lgpio.gpio_read(chip, PIN) == 1:
        pass

    ende = time.time()

    distanz = (ende - start) * 34300 / 2
    print(f"Distanz: {distanz:.1f} cm")

    time.sleep(0.5)