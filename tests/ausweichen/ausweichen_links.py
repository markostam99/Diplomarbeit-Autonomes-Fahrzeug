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

PWM_LINKS_GERADE = 70
PWM_RECHTS_GERADE = 71

# Ausweichmanöver links
PWM_LINKS_LINKSBOGEN = 40
PWM_RECHTS_LINKSBOGEN = 76

ZEIT_LINKSBOGEN = 1

# Korrektur nach dem Linksbogen
PWM_LINKS_RECHTSBOGEN = 75
PWM_RECHTS_RECHTSBOGEN = 40


ZEIT_RECHTSBOGEN = 1.9

# Korrektur nach dem Rechtsbogen
PWM_LINKS_KORREKTUR = 40
PWM_RECHTS_KORREKTUR = 76

ZEIT_KORREKTUR = 1

# -----------------------------
# GPIO initialisieren
# -----------------------------

h = lgpio.gpiochip_open(0)

for gpio in [AIN1, AIN2, BIN1, BIN2, STBY]:
    lgpio.gpio_claim_output(h, gpio)

lgpio.gpio_claim_output(h, PWMA)
lgpio.gpio_claim_output(h, PWMB)

lgpio.gpio_write(h, STBY, 1)

# Vorwärtsrichtung
lgpio.gpio_write(h, AIN1, 0)
lgpio.gpio_write(h, AIN2, 1)

lgpio.gpio_write(h, BIN1, 0)
lgpio.gpio_write(h, BIN2, 1)

try:

    print("Ausweichmanöver links gestartet.")

    # -----------------------------
    # 1. Linksbogen
    # -----------------------------

    lgpio.tx_pwm(
        h, PWMA,
        PWM_FREQUENZ,
        PWM_LINKS_LINKSBOGEN
    )

    lgpio.tx_pwm(
        h, PWMB,
        PWM_FREQUENZ,
        PWM_RECHTS_LINKSBOGEN
    )

    time.sleep(ZEIT_LINKSBOGEN)

    # -----------------------------
    # 2. Rechtsbogen
    # -----------------------------

    lgpio.tx_pwm(
        h, PWMA,
        PWM_FREQUENZ,
        PWM_LINKS_RECHTSBOGEN
    )

    lgpio.tx_pwm(
        h, PWMB,
        PWM_FREQUENZ,
        PWM_RECHTS_RECHTSBOGEN
    )

    time.sleep(ZEIT_RECHTSBOGEN)

    # -----------------------------
    # 3. Korrektur nach links
    # -----------------------------

    lgpio.tx_pwm(
        h, PWMA,
        PWM_FREQUENZ,
        PWM_LINKS_KORREKTUR
    )

    lgpio.tx_pwm(
        h, PWMB,
        PWM_FREQUENZ,
        PWM_RECHTS_KORREKTUR
    )

    time.sleep(ZEIT_KORREKTUR)

    # -----------------------------
    # 4. Geradeausfahrt
    # -----------------------------

    lgpio.tx_pwm(
        h, PWMA,
        PWM_FREQUENZ,
        PWM_LINKS_GERADE
    )

    lgpio.tx_pwm(
        h, PWMB,
        PWM_FREQUENZ,
        PWM_RECHTS_GERADE
    )

    time.sleep(2)

finally:

    # Motoren stoppen
    lgpio.tx_pwm(
        h, PWMA,
        PWM_FREQUENZ, 0
    )

    lgpio.tx_pwm(
        h, PWMB,
        PWM_FREQUENZ, 0
    )

    lgpio.gpio_write(h, STBY, 0)
    lgpio.gpiochip_close(h)

    print("Test beendet.")