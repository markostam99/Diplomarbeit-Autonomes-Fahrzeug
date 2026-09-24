import lgpio  

from config import AIN1, AIN2, PWMA, BIN1, BIN2, PWMB, STBY, PWM_FREQ

#GPIO Chip öffnen
lgpio.gpio_claim_output(h, AIN1)
lgpio.gpio_claim_output(h, AIN2)
lgpio.gpio_claim_output(h, BIN1)
lgpio.gpio_claim_output(h, BIN2)
lgpio.gpio_claim_output(h, STBY)

#Motortreiber aktivieren
lgpio.gpio_write(h, STBY, 1) 


def set_motors(left_speed, right_speed):
  #Geradeaus fahren
  lgpio.gpio_write(h, AIN1, 0)
  lgpio.gpio_write(h, AIN2, 1)
  lgpio.gpio_write(h, BIN1, 0)
  lgpio.gpio_write(h, BIN2, 1)
  
  #Motorgeschwindigkeit
  lgpio.tx_pwm(h, PWMA, PWMA_FREQ, left speed)
  lgpio.tx_pwm(h, PWMB, PWMA_FREQ, right speed)

