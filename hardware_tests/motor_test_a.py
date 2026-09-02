import lgpio
import time

AIN1 = 5
AIN2 = 6
PWMA = 12
STBY = 22

chip = lgpio.gpiochip_open(0)

lgpio.gpio_claim_output(chip, AIN1)
lgpio.gpio_claim_output(chip, AIN2)
lgpio.gpio_claim_output(chip, PWMA)
lgpio.gpio_claim_output(chip, STBY)

# Motortreiber aktivieren
lgpio.gpio_write(chip, STBY, 1)

# Drehrichtung Motor A/ AIN1 = 0 und AIN2 = 1 --> Rückwärtsbewegung Rad
lgpio.gpio_write(chip, AIN1, 1)
lgpio.gpio_write(chip, AIN2, 0)

# Motor einschalten
lgpio.gpio_write(chip, PWMA, 1)

print("Motor A läuft für 2 Sekunden")
time.sleep(2)

# Motor stoppen
lgpio.gpio_write(chip, PWMA, 0)

# Motortreiber deaktivieren
lgpio.gpio_write(chip, STBY, 0)

print("Motor A gestoppt")

lgpio.gpiochip_close(chip)
