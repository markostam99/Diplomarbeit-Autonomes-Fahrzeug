import lgpio
import time

AIN1 = 5
AIN2 = 6
PWMA = 12

BIN1 = 23
BIN2 = 24
PWMB = 13

STBY = 22

chip = lgpio.gpiochip_open(0)

for pin in [AIN1, AIN2, PWMA, BIN1, BIN2, PWMB, STBY]:
    lgpio.gpio_claim_output(chip, pin)

lgpio.gpio_write(chip, STBY, 1)

# Beide Motoren vorwärts
lgpio.gpio_write(chip, AIN1, 0)
lgpio.gpio_write(chip, AIN2, 1)

lgpio.gpio_write(chip, BIN1, 0)
lgpio.gpio_write(chip, BIN2, 1)

lgpio.gpio_write(chip, PWMA, 1)
lgpio.gpio_write(chip, PWMB, 1)

print("Beide Motoren laufen 2 Sekunden vorwärts")
time.sleep(2)

# Motoren stoppen
lgpio.gpio_write(chip, PWMA, 0)
lgpio.gpio_write(chip, PWMB, 0)

lgpio.gpio_write(chip, STBY, 0)

print("Beide Motoren gestoppt")

lgpio.gpiochip_close(chip)