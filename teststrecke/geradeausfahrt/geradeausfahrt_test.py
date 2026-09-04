import lgpio
import time

AIN1 = 5
AIN2 = 6
PWMA = 12

BIN1 = 23
BIN2 = 24
PWMB = 13

STBY = 22

PWM_LINKS = 65
PWM_RECHTS = 65
DAUER = 5

h = lgpio.gpiochip_open(0)

for pin in [AIN1, AIN2, PWMA, BIN1, BIN2, PWMB, STBY]:
    lgpio.gpio_claim_output(h, pin)

try:
    # Motortreiber aktivieren
    lgpio.gpio_write(h, STBY, 1)

    # Vorwärts
    lgpio.gpio_write(h, AIN1, 0)
    lgpio.gpio_write(h, AIN2, 1)

    lgpio.gpio_write(h, BIN1, 0)
    lgpio.gpio_write(h, BIN2, 1)

    # Motoren starten
    lgpio.tx_pwm(h, PWMA, 1000, PWM_LINKS)
    lgpio.tx_pwm(h, PWMB, 1000, PWM_RECHTS)

    time.sleep(DAUER)

finally:
    # NOTSTOPP / sicher stoppen
    lgpio.tx_pwm(h, PWMA, 1000, 0)
    lgpio.tx_pwm(h, PWMB, 1000, 0)

    lgpio.gpio_write(h, AIN1, 0)
    lgpio.gpio_write(h, AIN2, 0)
    lgpio.gpio_write(h, BIN1, 0)
    lgpio.gpio_write(h, BIN2, 0)

    lgpio.gpio_write(h, STBY, 0)

    lgpio.gpiochip_close(h)