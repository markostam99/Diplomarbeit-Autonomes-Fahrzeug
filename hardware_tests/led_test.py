import lgpio
import time

LED_ROT = 16
LED_GRUEN = 20

chip = lgpio.gpiochip_open(0)

lgpio.gpio_claim_output(chip, LED_ROT)
lgpio.gpio_claim_output(chip, LED_GRUEN)

# Beide LEDs zunächst ausschalten
lgpio.gpio_write(chip, LED_ROT, 0)
lgpio.gpio_write(chip, LED_GRUEN, 0)

# Rote LED einschalten
print("Rote LED leuchtet")
lgpio.gpio_write(chip, LED_ROT, 1)
time.sleep(3)
lgpio.gpio_write(chip, LED_ROT, 0)

# Grüne LED einschalten
print("Grüne LED leuchtet")
lgpio.gpio_write(chip, LED_GRUEN, 1)
time.sleep(3)
lgpio.gpio_write(chip, LED_GRUEN, 0)

print("LED-Test beendet")

lgpio.gpiochip_close(chip)