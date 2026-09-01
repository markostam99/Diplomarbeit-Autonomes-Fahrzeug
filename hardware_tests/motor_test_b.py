import lgpio
import time

BIN1 = 23
BIN2 = 24
PWMB = 13
STBY = 22

chip = lgpio.gpiochip_open(0)

lgpio.gpio_claim_output(chip, BIN1)
lgpio.gpio_claim_output(chip, BIN2)
lgpio.gpio_claim_output(chip, PWMB)
lgpio.gpio_claim_output(chip, STBY)

# Motortreiber aktivieren
lgpio.gpio_write(chip, STBY, 1)

# Drehrichtung Motor B
lgpio.gpio_write(chip, BIN1, 1)
lgpio.gpio_write(chip, BIN2, 0)

# Motor einschalten
lgpio.gpio_write(chip, PWMB, 1)

print("Motor B läuft für 2 Sekunden")
time.sleep(2)

# Motor stoppen
lgpio.gpio_write(chip, PWMB, 0)

# Motortreiber deaktivieren
lgpio.gpio_write(chip, STBY, 0)

print("Motor B gestoppt")

lgpio.gpiochip_close(chip)