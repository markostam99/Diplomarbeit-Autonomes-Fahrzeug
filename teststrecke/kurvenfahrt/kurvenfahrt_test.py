import lgpio
import time

# Motorpins
AIN1 = 5
AIN2 = 6
PWMA = 12

BIN1 = 23
BIN2 = 24
PWMB = 13

STBY = 22

# Geradeausfahrt
PWM_GERADE_LINKS = 70
PWM_GERADE_RECHTS = 67
GERADE_DAUER = 2

# Linkskurve/ Rechtskurve
PWM_KURVE_LINKS = 20
PWM_KURVE_RECHTS = 70
KURVENDAUER = 0.8

h = lgpio.gpiochip_open(0)

for pin in [AIN1, AIN2, PWMA, BIN1, BIN2, PWMB, STBY]:
    lgpio.gpio_claim_output(h, pin)

try:
    # Motortreiber aktivieren
    lgpio.gpio_write(h, STBY, 1)

    # Vorwärtsrichtung
    lgpio.gpio_write(h, AIN1, 0)
    lgpio.gpio_write(h, AIN2, 1)

    lgpio.gpio_write(h, BIN1, 0)
    lgpio.gpio_write(h, BIN2, 1)

    # 2 Sekunden Geradeausfahrt
    lgpio.tx_pwm(h, PWMA, 1000, PWM_GERADE_LINKS)
    lgpio.tx_pwm(h, PWMB, 1000, PWM_GERADE_RECHTS)

    time.sleep(GERADE_DAUER)

    # Linkskurve/ Rechtskurve
    lgpio.tx_pwm(h, PWMA, 1000, PWM_KURVE_LINKS)
    lgpio.tx_pwm(h, PWMB, 1000, PWM_KURVE_RECHTS)

    time.sleep(KURVENDAUER)

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