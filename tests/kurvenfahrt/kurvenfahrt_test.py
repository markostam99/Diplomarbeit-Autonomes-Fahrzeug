import lgpio
import time

# -----------------------------
# GPIO-Belegung TB6612FNG
# -----------------------------

AIN1 = 5
AIN2 = 6
PWMA = 12

BIN1 = 23
BIN2 = 24
PWMB = 13

STBY = 22

PWM_FREQUENZ = 1000

# -----------------------------
# Fahrparameter
# -----------------------------

# Geradeausfahrt
PWM_GERADE_LINKS = 70
PWM_GERADE_RECHTS = 71
GERADE_DAUER = 2.0

# Linkskurve/ Rechtskurve
PWM_KURVE_LINKS = 73
PWM_KURVE_RECHTS = 10
KURVENDAUER = 1

# -----------------------------
# GPIO initialisieren
# -----------------------------

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

    # -----------------------------
    # 2 Sekunden geradeaus
    # -----------------------------

    print("Geradeausfahrt")

    lgpio.tx_pwm(
        h,
        PWMA,
        PWM_FREQUENZ,
        PWM_GERADE_LINKS
    )

    lgpio.tx_pwm(
        h,
        PWMB,
        PWM_FREQUENZ,
        PWM_GERADE_RECHTS
    )

    time.sleep(GERADE_DAUER)

    # -----------------------------
    # 90° Rechtskurve   
    # -----------------------------

    print("Rechtskurve")

    lgpio.tx_pwm(
        h,
        PWMA,
        PWM_FREQUENZ,
        PWM_KURVE_LINKS
    )

    lgpio.tx_pwm(
        h,
        PWMB,
        PWM_FREQUENZ,
        PWM_KURVE_RECHTS
    )

    time.sleep(KURVENDAUER)

    # -----------------------------
    # Wieder 2 Sekunden geradeaus
    # -----------------------------

    print("Geradeausfahrt nach Kurve")

    lgpio.tx_pwm(
        h,
        PWMA,
        PWM_FREQUENZ,
        PWM_GERADE_LINKS
    )

    lgpio.tx_pwm(
        h,
        PWMB,
        PWM_FREQUENZ,
        PWM_GERADE_RECHTS
    )

    time.sleep(GERADE_DAUER)

finally:

    # Motoren stoppen
    lgpio.tx_pwm(h, PWMA, PWM_FREQUENZ, 0)
    lgpio.tx_pwm(h, PWMB, PWM_FREQUENZ, 0)

    lgpio.gpio_write(h, AIN1, 0)
    lgpio.gpio_write(h, AIN2, 0)

    lgpio.gpio_write(h, BIN1, 0)
    lgpio.gpio_write(h, BIN2, 0)

    lgpio.gpio_write(h, STBY, 0)

    lgpio.gpiochip_close(h)

    print("Test beendet")