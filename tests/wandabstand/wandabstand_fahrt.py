import lgpio
import time

# Motoren
AIN1 = 5
AIN2 = 6
PWMA = 12

BIN1 = 23
BIN2 = 24
PWMB = 13

STBY = 22

# Ultraschallsensoren
US_LINKS = 17
US_RECHTS = 27

PWM_LINKS = 70
PWM_RECHTS = 71
DAUER = 5

h = lgpio.gpiochip_open(0)

# Motor-Pins
for pin in [AIN1, AIN2, PWMA, BIN1, BIN2, PWMB, STBY]:
    lgpio.gpio_claim_output(h, pin)


def messen(pin):
    lgpio.gpio_claim_output(h, pin)

    lgpio.gpio_write(h, pin, 0)
    time.sleep(0.002)

    lgpio.gpio_write(h, pin, 1)
    time.sleep(0.00001)
    lgpio.gpio_write(h, pin, 0)

    lgpio.gpio_claim_input(h, pin)

    while lgpio.gpio_read(h, pin) == 0:
        start = time.time()

    while lgpio.gpio_read(h, pin) == 1:
        ende = time.time()

    return (ende - start) * 34300 / 2


try:
    # Vorwärtsfahrt
    lgpio.gpio_write(h, STBY, 1)

    lgpio.gpio_write(h, AIN1, 0)
    lgpio.gpio_write(h, AIN2, 1)

    lgpio.gpio_write(h, BIN1, 0)
    lgpio.gpio_write(h, BIN2, 1)

    lgpio.tx_pwm(h, PWMA, 1000, PWM_LINKS)
    lgpio.tx_pwm(h, PWMB, 1000, PWM_RECHTS)

    startzeit = time.time()

    while time.time() - startzeit < DAUER:

        links = messen(US_LINKS)
        time.sleep(0.05)

        rechts = messen(US_RECHTS)

        print(f"Links: {links:.1f} cm | Rechts: {rechts:.1f} cm")

        time.sleep(0.1)

finally:
    # Motoren stoppen
    lgpio.tx_pwm(h, PWMA, 1000, 0)
    lgpio.tx_pwm(h, PWMB, 1000, 0)

    lgpio.gpio_write(h, AIN1, 0)
    lgpio.gpio_write(h, AIN2, 0)
    lgpio.gpio_write(h, BIN1, 0)
    lgpio.gpio_write(h, BIN2, 0)
    lgpio.gpio_write(h, STBY, 0)

    lgpio.gpiochip_close(h)
